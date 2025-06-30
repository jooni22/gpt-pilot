"""
IPC Web Broker - Minimalny broker dla gemini-cli

TCP Server dla GPT-Pilot (port 8125) + HTTP API dla gemini-cli (port 8126)
"""

import asyncio
import json
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, Optional
from collections import deque
import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response
import uvicorn


@dataclass
class BrokerConfig:
    gpt_pilot_host: str = "127.0.0.1"
    gpt_pilot_port: int = 8125
    web_host: str = "127.0.0.1"
    web_port: int = 8126
    max_queue_size: int = 100
    log_level: str = "INFO"


class MessageType(str, Enum):
    EXIT = "exit"
    STREAM = "stream"
    VERBOSE = "verbose"
    BUTTONS = "button"
    BUTTONS_ONLY = "buttons-only"
    RESPONSE = "response"
    USER_INPUT_REQUEST = "user_input_request"
    INFO = "info"
    PROGRESS = "progress"
    DEBUGGING_LOGS = "debugging_logs"
    RUN_COMMAND = "run_command"
    APP_LINK = "appLink"
    OPEN_FILE = "openFile"
    PROJECT_FOLDER_NAME = "project_folder_name"
    PROJECT_STATS = "projectStats"
    HINT = "hint"
    KEY_EXPIRED = "keyExpired"
    INPUT_PREFILL = "inputPrefill"
    LOADING_FINISHED = "loadingFinished"
    PROJECT_DESCRIPTION = "projectDescription"
    FEATURES_LIST = "featuresList"
    IMPORT_PROJECT = "importProject"
    APP_FINISHED = "appFinished"
    FEATURE_FINISHED = "featureFinished"
    GENERATE_DIFF = "generateDiff"
    CLOSE_DIFF = "closeDiff"
    FILE_STATUS = "fileStatus"
    BUG_HUNTER_STATUS = "bugHunterStatus"
    EPICS_AND_TASKS = "epicsAndTasks"
    MODIFIED_FILES = "modifiedFiles"
    IMPORTANT_STREAM = "importantStream"
    BREAKDOWN_STREAM = "breakdownStream"
    TEST_INSTRUCTIONS = "testInstructions"
    KNOWLEDGE_BASE_UPDATE = "updatedKnowledgeBase"
    STOP_APP = "stopApp"


@dataclass
class QuestionContext:
    """Kontekst pytania budowany z wielu wiadomości IPC"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    question: str = ""
    hint: str = ""
    buttons: Dict[str, str] = field(default_factory=dict)
    buttons_only: bool = False
    initial_text: str = ""
    placeholder: str = ""
    full_screen: bool = False
    allow_empty: bool = True
    default: str = ""
    category: str = ""
    project_state_id: str = ""
    extra_info: str = ""
    timestamp: float = field(default_factory=time.time)
    is_complete: bool = False


@dataclass
class BrokerStats:
    messages_received: int = 0
    messages_sent: int = 0
    questions_processed: int = 0
    errors: int = 0
    uptime_start: float = field(default_factory=time.time)
    
    @property
    def uptime(self) -> float:
        return time.time() - self.uptime_start


from core.ui.base import UIBase, UserInput


class IPCWebBroker:
    """Broker IPC dla WebSocket UI"""
    
    def __init__(self, config: BrokerConfig = None, ui: UIBase = None):
        self.config = config or BrokerConfig()
        self.stats = BrokerStats()
        self.gpt_pilot_writer: Optional[asyncio.StreamWriter] = None
        self.ui = ui
        self.tcp_server: Optional[asyncio.Server] = None
        self.web_app = self._create_web_app()
        self.current_question: Optional[QuestionContext] = None
        self.question_timeout = 2.0  # sekund na oczekiwanie na kolejne części pytania
        self._setup_logging()
        
    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, self.config.log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def _create_web_app(self) -> FastAPI:
        app = FastAPI(title="GPT-Pilot IPC Broker", version="1.0.0")
        
        @app.get("/api/status")
        async def get_status():
            return {
                "status": "running",
                "gpt_pilot_connected": self.gpt_pilot_writer is not None,
                "current_question": self.current_question.id if self.current_question else None,
                "stats": {
                    "messages_received": self.stats.messages_received,
                    "messages_sent": self.stats.messages_sent,
                    "questions_processed": self.stats.questions_processed,
                    "errors": self.stats.errors,
                    "uptime": self.stats.uptime
                }
            }
        
        return app
    
    async def _send_response_to_gpt_pilot(self, response: str):
        if not self.gpt_pilot_writer:
            self.logger.error("❌ GPT-Pilot not connected, cannot send response")
            raise Exception("GPT-Pilot not connected")
        
        response_msg = {
            "type": MessageType.RESPONSE,
            "content": response
        }
        
        self.logger.info(f"📤 Preparing response message: {response_msg}")
        
        try:
            response_data = json.dumps(response_msg).encode('utf-8')
            
            # Sprawdź czy writer nie jest zamknięty
            if self.gpt_pilot_writer.is_closing():
                self.logger.error("❌ GPT-Pilot writer is closing, cannot send response")
                raise Exception("GPT-Pilot connection is closing")
                
            self.gpt_pilot_writer.write(len(response_data).to_bytes(4, byteorder='big'))
            self.gpt_pilot_writer.write(response_data)
            await self.gpt_pilot_writer.drain()
            
            self.stats.messages_sent += 1
            self.logger.info(f"✅ Response sent to GPT-Pilot: '{response}' ({len(response_data)} bytes)")
            self.logger.info(f"🔄 Continuing to wait for next message from GPT-Pilot...")
            
        except (ConnectionResetError, BrokenPipeError) as e:
            self.logger.error(f"❌ Connection lost while sending response: {e}")
            self.gpt_pilot_writer = None
            raise Exception(f"Connection lost: {e}")
        except Exception as e:
            self.logger.error(f"❌ Error sending response: {e}")
            raise
    
    async def _process_question_complete(self):
        """Przetwarza kompletne pytanie gdy wszystkie części są zebrane"""
        if not self.current_question or not self.ui:
            self.logger.warning("⚠️  No current question or UI available")
            return
            
        self.logger.info(f"🔄 Processing complete question:")
        self.logger.info(f"   📝 Question: {self.current_question.question}")
        self.logger.info(f"   🔘 Buttons: {self.current_question.buttons}")
        self.logger.info(f"   ⚡ Buttons only: {self.current_question.buttons_only}")
        self.logger.info(f"   💡 Hint: {self.current_question.hint}")
        self.logger.info(f"   📄 Full screen: {self.current_question.full_screen}")
        
        try:
            # Parsuj buttony z formatu "val1/val2/val3" na dict
            buttons = None
            if self.current_question.buttons:
                # buttons są już w formacie dict
                buttons = self.current_question.buttons
            
            user_input = await self.ui.ask_question(
                self.current_question.question,
                buttons=buttons,
                default=self.current_question.default,
                buttons_only=self.current_question.buttons_only,
                allow_empty=self.current_question.allow_empty,
                full_screen=self.current_question.full_screen,
                hint=self.current_question.hint or None,
                initial_text=self.current_question.initial_text or None,
                placeholder=self.current_question.placeholder or None
            )
            
            self.logger.info(f"✅ Received user input:")
            self.logger.info(f"   📝 Text: '{user_input.text}'")
            self.logger.info(f"   🔘 Button: '{user_input.button}'")
            self.logger.info(f"   ❌ Cancelled: {user_input.cancelled}")
            
            # Wyślij odpowiedź do GPT-Pilot
            response = user_input.text or user_input.button or ""
            self.logger.info(f"📤 Sending response to GPT-Pilot: '{response}'")
            await self._send_response_to_gpt_pilot(response)
            
            self.stats.questions_processed += 1
            self.current_question = None
            
        except Exception as e:
            self.logger.error(f"❌ Error processing question: {e}")
            self.stats.errors += 1
            # Wyślij pustą odpowiedź aby nie zablokować GPT-Pilot
            await self._send_response_to_gpt_pilot("")
            self.current_question = None

    def _parse_buttons_string(self, buttons_str: str) -> Dict[str, str]:
        """Parsuje string buttonów w formacie 'value1/value2/value3' na dict"""
        if not buttons_str:
            self.logger.debug("🔘 No buttons string provided")
            return {}
        
        self.logger.info(f"🔘 Parsing buttons string: '{buttons_str}'")
        
        # Protokół IPC wysyła tylko wartości buttonów, nie klucze
        # Musimy odgadnąć klucze na podstawie wartości
        values = buttons_str.split('/')
        buttons = {}
        
        for val in values:
            val = val.strip()
            if not val:
                continue
                
            # Mapowanie znanych wartości na klucze
            if val == "Node.js":
                buttons["node"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'node'")
            elif val == "Other (coming soon)":
                buttons["other"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'other'")
            elif val == "Yes":
                buttons["yes"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'yes'")
            elif val == "No":
                buttons["no"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'no'")
            elif val == "Continue":
                buttons["continue"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'continue'")
            elif val == "Exit":
                buttons["exit"] = val
                self.logger.info(f"   ➤ Mapped '{val}' → 'exit'")
            else:
                # Fallback - stwórz klucz z wartości
                key = val.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
                buttons[key] = val
                self.logger.info(f"   ➤ Auto-mapped '{val}' → '{key}'")
        
        self.logger.info(f"🔘 Final buttons dict: {buttons}")
        return buttons

    async def handle_gpt_pilot_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        client_addr = writer.get_extra_info('peername')
        self.logger.info(f"GPT-Pilot connected from {client_addr}")
        self.gpt_pilot_writer = writer
        
        try:
            while True:
                try:
                    # Czytaj prefiks długości (4 bajty)
                    self.logger.debug(f"🔄 Waiting for message from GPT-Pilot...")
                    data = await reader.readexactly(4)
                    msg_len = int.from_bytes(data, byteorder='big')
                    self.logger.debug(f"📏 Message length: {msg_len} bytes")
                except asyncio.IncompleteReadError:
                    self.logger.info(f"🔌 GPT-Pilot closed connection (EOF)")
                    break
                
                try:
                    # Czytaj dane wiadomości
                    data = await reader.readexactly(msg_len)
                    message = json.loads(data.decode('utf-8'))
                    self.logger.debug(f"📥 Raw message received: {message}")
                except (asyncio.IncompleteReadError, json.JSONDecodeError) as e:
                    self.logger.error(f"❌ Error reading message: {e}")
                    self.stats.errors += 1
                    break
                
                await self._process_gpt_pilot_message(message)
                
        except Exception as e:
            self.logger.error(f"❌ Error handling GPT-Pilot client: {e}")
            self.stats.errors += 1
        finally:
            self.logger.info(f"🔌 GPT-Pilot disconnected from {client_addr}")
            self.gpt_pilot_writer = None
            if not writer.is_closing():
                writer.close()
                try:
                    await writer.wait_closed()
                    self.logger.info(f"✅ Connection to GPT-Pilot properly closed")
                except Exception as e:
                    self.logger.error(f"❌ Error closing connection: {e}")
    
    async def _process_gpt_pilot_message(self, message: Dict[str, Any]):
        msg_type = message.get('type')
        content = message.get('content', '')
        
        self.stats.messages_received += 1
        self.logger.info(f"📨 Received from GPT-Pilot: {msg_type} - content: {str(content)[:100]}")
        
        # Przekaż inne typy wiadomości do UI jeśli możliwe
        if self.ui and msg_type not in [
            MessageType.USER_INPUT_REQUEST, 
            MessageType.VERBOSE, 
            MessageType.BUTTONS, 
            MessageType.BUTTONS_ONLY,
            MessageType.HINT,
            MessageType.INPUT_PREFILL
        ]:
            await self._forward_message_to_ui(message)
        
        # Obsługa pytań - budowanie kontekstu
        if msg_type == MessageType.VERBOSE:
            self.logger.info(f"🗣️  VERBOSE: Starting new question context")
            # Rozpocznij nowe pytanie lub użyj istniejącego
            if not self.current_question:
                self.current_question = QuestionContext()
            # VERBOSE zawiera tekst pytania
            self.current_question.question = str(content)
            self.current_question.category = message.get('category', '')
            self.current_question.project_state_id = message.get('project_state_id', '')
            self.logger.info(f"💬 Question set: {self.current_question.question}")
            
        elif msg_type == MessageType.USER_INPUT_REQUEST:
            self.logger.info(f"❓ USER_INPUT_REQUEST: Confirming question")
            # USER_INPUT_REQUEST potwierdza pytanie
            if not self.current_question:
                self.current_question = QuestionContext()
                self.current_question.question = str(content)
                self.logger.info(f"💬 Question from USER_INPUT_REQUEST: {self.current_question.question}")
            
            self.current_question.extra_info = message.get('extra_info', '')
            self.current_question.placeholder = message.get('placeholder', '')
            
            # Zaplanuj przetworzenie pytania za chwilę (czekamy na buttony)
            self.logger.info(f"⏰ Scheduling question processing in {self.question_timeout}s")
            asyncio.create_task(self._schedule_question_processing())
            
        elif msg_type == MessageType.BUTTONS:
            self.logger.info(f"🔘 BUTTONS: {content}")
            if self.current_question:
                buttons = self._parse_buttons_string(str(content))
                self.logger.info(f"🔘 Parsed buttons: {buttons}")
                self.current_question.buttons = buttons
                self.current_question.buttons_only = False
                self.current_question.full_screen = message.get('full_screen', False)
                
        elif msg_type == MessageType.BUTTONS_ONLY:
            self.logger.info(f"🔘 BUTTONS_ONLY: {content}")
            if self.current_question:
                buttons = self._parse_buttons_string(str(content))
                self.logger.info(f"🔘 Parsed buttons_only: {buttons}")
                self.current_question.buttons = buttons
                self.current_question.buttons_only = True
                self.current_question.full_screen = message.get('full_screen', False)
                
        elif msg_type == MessageType.HINT:
            self.logger.info(f"💡 HINT: {content}")
            if self.current_question:
                self.current_question.hint = str(content)
                
        elif msg_type == MessageType.INPUT_PREFILL:
            self.logger.info(f"📝 INPUT_PREFILL: {content}")
            if self.current_question:
                self.current_question.initial_text = str(content)
        
        elif msg_type == MessageType.EXIT:
            self.logger.info("🚪 GPT-Pilot is exiting")

    async def _schedule_question_processing(self):
        """Zaplanuj przetworzenie pytania z opóźnieniem na oczekiwanie na buttony"""
        await asyncio.sleep(self.question_timeout)
        if self.current_question and not self.current_question.is_complete:
            self.current_question.is_complete = True
            await self._process_question_complete()

    async def _forward_message_to_ui(self, message: Dict[str, Any]):
        """Przekaż wiadomość do UI jeśli ma odpowiednią metodę"""
        msg_type = message.get('type')
        content = message.get('content', '')
        
        try:
            if msg_type == MessageType.STREAM and hasattr(self.ui, 'send_stream_chunk'):
                await self.ui.send_stream_chunk(content)
            elif msg_type == MessageType.INFO and hasattr(self.ui, 'send_message'):
                await self.ui.send_message(str(content))
            elif msg_type == MessageType.RUN_COMMAND and hasattr(self.ui, 'send_run_command'):
                await self.ui.send_run_command(str(content))
            elif msg_type == MessageType.APP_LINK and hasattr(self.ui, 'send_app_link'):
                await self.ui.send_app_link(str(content))
            # Dodaj więcej przekierowań w razie potrzeby
        except Exception as e:
            self.logger.error(f"Error forwarding message to UI: {e}")
    
    async def start_tcp_server(self):
        self.tcp_server = await asyncio.start_server(
            self.handle_gpt_pilot_client,
            self.config.gpt_pilot_host,
            self.config.gpt_pilot_port
        )
        
        addr = self.tcp_server.sockets[0].getsockname()
        self.logger.info(f"TCP server started on {addr[0]}:{addr[1]}")
    
    async def start_web_server(self):
        config = uvicorn.Config(
            self.web_app,
            host=self.config.web_host,
            port=self.config.web_port,
            log_level=self.config.log_level.lower()
        )
        server = uvicorn.Server(config)
        await server.serve()
    
    async def start(self):
        self.logger.info("Starting IPC Web Broker")
        await asyncio.gather(
            self.start_tcp_server(),
            self.start_web_server()
        )


async def main():
    config = BrokerConfig()
    broker = IPCWebBroker(config)
    
    try:
        await broker.start()
    except KeyboardInterrupt:
        print("\n👋 Broker stopped by user")


if __name__ == '__main__':
    asyncio.run(main())