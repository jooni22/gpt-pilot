import asyncio
import json
import time
import uuid
from typing import Optional, List, Dict, Any
import websockets
from websockets.exceptions import ConnectionClosed

from core.log import get_logger
from core.ui.base import UIBase, UIClosedError, UISource, UserInput

log = get_logger(__name__)


class WebSocketUIConfig:
    """Konfiguracja dla WebSocket UI"""
    def __init__(self, port: int = 8127, host: str = "localhost"):
        self.port = port
        self.host = host


class WebSocketMessage:
    """Struktura wiadomości WebSocket"""
    def __init__(self, type: str, content: Any = None, **kwargs):
        self.type = type
        self.content = content
        self.timestamp = time.time()
        self.id = str(uuid.uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "content": self.content,
            "timestamp": self.timestamp,
            **{k: v for k, v in self.__dict__.items() 
               if k not in ['id', 'type', 'content', 'timestamp']}
        }


class WebSocketUI(UIBase):
    """
    UI adapter używający WebSocket do komunikacji z interfejsem webowym.
    
    Wystawia serwer WebSocket na którym nasłuchuje połączeń od klientów webowych.
    Wszystkie wiadomości i pytania są przekazywane przez WebSocket.
    """

    def __init__(self, config: WebSocketUIConfig):
        self.config = config
        self.server = None
        self.clients: List[websockets.WebSocketServerProtocol] = []
        self.pending_question = None
        self.question_response_future = None
        self.conversation_history: List[Dict[str, Any]] = []

    async def start(self) -> bool:
        """Uruchom serwer WebSocket"""
        try:
            log.info(f"Starting WebSocket server on {self.config.host}:{self.config.port}")
            self.server = await websockets.serve(
                self._handle_client,
                self.config.host,
                self.config.port
            )
            log.info(f"WebSocket server started on ws://{self.config.host}:{self.config.port}")
            return True
        except Exception as e:
            log.error(f"Failed to start WebSocket server: {e}")
            return False

    async def stop(self):
        """Zatrzymaj serwer WebSocket"""
        if self.server:
            log.info("Stopping WebSocket server")
            self.server.close()
            await self.server.wait_closed()
            
            # Zamknij wszystkie połączenia klientów
            for client in self.clients[:]:
                await client.close()
            self.clients.clear()

    async def _handle_client(self, websocket):
        """Obsłuż nowego klienta WebSocket"""
        client_addr = websocket.remote_address
        log.info(f"New WebSocket client connected: {client_addr}")
        self.clients.append(websocket)
        
        try:
            # Wyślij historię konwersacji do nowego klienta
            await self._send_to_client(websocket, WebSocketMessage(
                "conversation_history",
                content=self.conversation_history
            ))
            
            # Jeśli jest oczekujące pytanie, wyślij je
            if self.pending_question:
                await self._send_to_client(websocket, self.pending_question)
            
            # Nasłuchuj odpowiedzi od klienta
            async for message in websocket:
                try:
                    data = json.loads(message)
                    await self._handle_client_message(data)
                except json.JSONDecodeError:
                    log.error(f"Invalid JSON from client {client_addr}: {message}")
                except Exception as e:
                    log.error(f"Error handling message from {client_addr}: {e}")
                    
        except ConnectionClosed:
            log.info(f"WebSocket client disconnected: {client_addr}")
        except Exception as e:
            log.error(f"Error handling WebSocket client {client_addr}: {e}")
        finally:
            if websocket in self.clients:
                self.clients.remove(websocket)

    async def _handle_client_message(self, data: Dict[str, Any]):
        """Obsłuż wiadomość od klienta"""
        msg_type = data.get("type")
        
        if msg_type == "user_response" and self.question_response_future:
            # Odpowiedź na oczekujące pytanie
            response_data = data.get("content", {})
            user_input = UserInput(
                text=response_data.get("text"),
                button=response_data.get("button"),
                cancelled=response_data.get("cancelled", False)
            )
            
            # Zwróć odpowiedź do ask_question
            if not self.question_response_future.done():
                self.question_response_future.set_result(user_input)
            
            self.pending_question = None
            
        elif msg_type == "ping":
            # Odpowiedź na ping
            await self._broadcast_to_clients(WebSocketMessage("pong"))

    async def _send_to_client(self, client: websockets.WebSocketServerProtocol, message: WebSocketMessage):
        """Wyślij wiadomość do konkretnego klienta"""
        try:
            await client.send(json.dumps(message.to_dict()))
        except ConnectionClosed:
            if client in self.clients:
                self.clients.remove(client)
        except Exception as e:
            log.error(f"Error sending message to client: {e}")

    async def _broadcast_to_clients(self, message: WebSocketMessage):
        """Wyślij wiadomość do wszystkich klientów"""
        if not self.clients:
            return
            
        # Dodaj do historii konwersacji
        self.conversation_history.append(message.to_dict())
        
        # Ogranicz historię do ostatnich 1000 wiadomości
        if len(self.conversation_history) > 1000:
            self.conversation_history = self.conversation_history[-1000:]
        
        # Wyślij do wszystkich klientów
        for client in self.clients[:]:  # Kopia listy
            await self._send_to_client(client, message)

    async def send_stream_chunk(
        self, chunk: Optional[str], *, source: Optional[UISource] = None, project_state_id: Optional[str] = None
    ):
        """Wyślij fragment tekstu (streaming)"""
        if chunk is None:
            # Koniec streamu
            message = WebSocketMessage(
                "stream_end",
                source=source.type_name if source else None,
                project_state_id=project_state_id
            )
        else:
            message = WebSocketMessage(
                "stream_chunk",
                content=chunk,
                source=source.type_name if source else None,
                project_state_id=project_state_id
            )
        
        await self._broadcast_to_clients(message)

    async def send_message(
        self,
        message: str,
        *,
        source: Optional[UISource] = None,
        project_state_id: Optional[str] = None,
        extra_info: Optional[str] = None,
    ):
        """Wyślij wiadomość"""
        ws_message = WebSocketMessage(
            "message",
            content=message,
            source=source.type_name if source else None,
            project_state_id=project_state_id,
            extra_info=extra_info
        )
        
        await self._broadcast_to_clients(ws_message)

    async def ask_question(
        self,
        question: str,
        *,
        buttons: Optional[dict[str, str]] = None,
        default: Optional[str] = None,
        buttons_only: bool = False,
        allow_empty: bool = False,
        full_screen: Optional[bool] = False,
        hint: Optional[str] = None,
        verbose: bool = True,
        initial_text: Optional[str] = None,
        source: Optional[UISource] = None,
        project_state_id: Optional[str] = None,
        extra_info: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> UserInput:
        """Zadaj pytanie i czekaj na odpowiedź przez WebSocket"""
        
        if not self.clients:
            raise UIClosedError("No WebSocket clients connected")
        
        # Stwórz pytanie
        question_data = {
            "question": question,
            "buttons": buttons,
            "default": default,
            "buttons_only": buttons_only,
            "allow_empty": allow_empty,
            "full_screen": full_screen,
            "hint": hint,
            "initial_text": initial_text,
            "placeholder": placeholder
        }
        
        self.pending_question = WebSocketMessage(
            "user_input_request",
            content=question_data,
            source=source.type_name if source else None,
            project_state_id=project_state_id,
            extra_info=extra_info
        )
        
        # Wyślij pytanie do wszystkich klientów
        await self._broadcast_to_clients(self.pending_question)
        
        # Stwórz Future dla odpowiedzi
        self.question_response_future = asyncio.Future()
        
        try:
            # Czekaj na odpowiedź (z timeoutem 300 sekund)
            user_input = await asyncio.wait_for(self.question_response_future, timeout=300)
            return user_input
        except asyncio.TimeoutError:
            self.pending_question = None
            raise UIClosedError("Question timeout - no response received")
        except Exception as e:
            self.pending_question = None
            raise UIClosedError(f"Error waiting for response: {e}")

    # Implementacje pozostałych metod z UIBase
    
    async def send_key_expired(self, message: Optional[str] = None):
        await self._broadcast_to_clients(WebSocketMessage("key_expired", content=message))

    async def send_app_finished(
        self,
        app_id: Optional[str] = None,
        app_name: Optional[str] = None,
        folder_name: Optional[str] = None,
    ):
        await self._broadcast_to_clients(WebSocketMessage(
            "app_finished",
            content={"app_id": app_id, "app_name": app_name, "folder_name": folder_name}
        ))

    async def send_feature_finished(
        self,
        app_id: Optional[str] = None,
        app_name: Optional[str] = None,
        folder_name: Optional[str] = None,
    ):
        await self._broadcast_to_clients(WebSocketMessage(
            "feature_finished",
            content={"app_id": app_id, "app_name": app_name, "folder_name": folder_name}
        ))

    async def send_project_stage(self, data: dict):
        await self._broadcast_to_clients(WebSocketMessage("project_stage", content=data))

    async def send_epics_and_tasks(self, epics: list[dict], tasks: list[dict]):
        await self._broadcast_to_clients(WebSocketMessage(
            "epics_and_tasks",
            content={"epics": epics, "tasks": tasks}
        ))

    async def send_task_progress(
        self,
        index: int,
        n_tasks: int,
        description: str,
        source: str,
        status: str,
        source_index: int = 1,
        tasks: list[dict] = None,
    ):
        await self._broadcast_to_clients(WebSocketMessage(
            "task_progress",
            content={
                "index": index,
                "n_tasks": n_tasks,
                "description": description,
                "source": source,
                "status": status,
                "source_index": source_index,
                "tasks": tasks
            }
        ))

    async def send_step_progress(
        self,
        index: int,
        n_steps: int,
        step: dict,
        task_source: str,
    ):
        await self._broadcast_to_clients(WebSocketMessage(
            "step_progress",
            content={
                "index": index,
                "n_steps": n_steps,
                "step": step,
                "task_source": task_source
            }
        ))

    async def send_modified_files(self, modified_files: dict[str, str, str]):
        await self._broadcast_to_clients(WebSocketMessage("modified_files", content=modified_files))

    async def send_data_about_logs(self, data_about_logs: dict):
        await self._broadcast_to_clients(WebSocketMessage("debugging_logs", content=data_about_logs))

    async def send_run_command(self, run_command: str):
        await self._broadcast_to_clients(WebSocketMessage("run_command", content=run_command))

    async def send_app_link(self, app_link: str):
        await self._broadcast_to_clients(WebSocketMessage("app_link", content=app_link))

    async def open_editor(self, file: str, line: Optional[int] = None):
        await self._broadcast_to_clients(WebSocketMessage(
            "open_editor",
            content={"file": file, "line": line}
        ))

    async def send_project_root(self, path: str):
        await self._broadcast_to_clients(WebSocketMessage("project_root", content=path))

    async def start_important_stream(self):
        await self._broadcast_to_clients(WebSocketMessage("important_stream_start"))

    async def start_breakdown_stream(self):
        await self._broadcast_to_clients(WebSocketMessage("breakdown_stream_start"))

    async def send_project_stats(self, stats: dict):
        await self._broadcast_to_clients(WebSocketMessage("project_stats", content=stats))

    async def send_test_instructions(self, test_instructions: str, project_state_id: Optional[str] = None):
        await self._broadcast_to_clients(WebSocketMessage(
            "test_instructions",
            content=test_instructions,
            project_state_id=project_state_id
        ))

    async def knowledge_base_update(self, knowledge_base: dict):
        await self._broadcast_to_clients(WebSocketMessage("knowledge_base_update", content=knowledge_base))

    async def send_file_status(self, file_path: str, file_status: str, source: Optional[UISource] = None):
        await self._broadcast_to_clients(WebSocketMessage(
            "file_status",
            content={"file_path": file_path, "file_status": file_status},
            source=source.type_name if source else None
        ))

    async def send_bug_hunter_status(self, status: str, num_cycles: int):
        await self._broadcast_to_clients(WebSocketMessage(
            "bug_hunter_status",
            content={"status": status, "num_cycles": num_cycles}
        ))

    async def generate_diff(
        self,
        file_path: str,
        file_old: str,
        file_new: str,
        n_new_lines: int = 0,
        n_del_lines: int = 0,
        source: Optional[UISource] = None,
    ):
        await self._broadcast_to_clients(WebSocketMessage(
            "generate_diff",
            content={
                "file_path": file_path,
                "file_old": file_old,
                "file_new": file_new,
                "n_new_lines": n_new_lines,
                "n_del_lines": n_del_lines
            },
            source=source.type_name if source else None
        ))

    async def stop_app(self):
        await self._broadcast_to_clients(WebSocketMessage("stop_app"))

    async def close_diff(self):
        await self._broadcast_to_clients(WebSocketMessage("close_diff"))

    async def loading_finished(self):
        await self._broadcast_to_clients(WebSocketMessage("loading_finished"))

    async def send_project_description(self, description: str):
        await self._broadcast_to_clients(WebSocketMessage("project_description", content=description))

    async def send_features_list(self, features: list[str]):
        await self._broadcast_to_clients(WebSocketMessage("features_list", content=features))

    async def import_project(self, project_dir: str):
        await self._broadcast_to_clients(WebSocketMessage("import_project", content=project_dir))


__all__ = ["WebSocketUI", "WebSocketUIConfig"]