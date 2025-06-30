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
class PendingQuestion:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    question: str = ""
    context: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)
    writer: Any = None


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


class IPCWebBroker:
    """Minimalny broker dla gemini-cli"""
    
    def __init__(self, config: BrokerConfig = None):
        self.config = config or BrokerConfig()
        self.stats = BrokerStats()
        self.gpt_pilot_writer: Optional[asyncio.StreamWriter] = None
        self.pending_questions: deque[PendingQuestion] = deque(maxlen=self.config.max_queue_size)
        self.current_question: Optional[PendingQuestion] = None
        self.tcp_server: Optional[asyncio.Server] = None
        self.web_app = self._create_web_app()
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
                "pending_questions": len(self.pending_questions),
                "current_question": self.current_question.id if self.current_question else None,
                "stats": {
                    "messages_received": self.stats.messages_received,
                    "messages_sent": self.stats.messages_sent,
                    "questions_processed": self.stats.questions_processed,
                    "errors": self.stats.errors,
                    "uptime": self.stats.uptime
                }
            }
        
        @app.get("/api/question")
        async def get_current_question():
            if not self.current_question:
                return Response(status_code=204)
            
            return {
                "id": self.current_question.id,
                "question": self.current_question.question,
                "context": self.current_question.context,
                "timestamp": self.current_question.timestamp,
                "age": time.time() - self.current_question.timestamp
            }
        
        @app.post("/api/answer")
        async def answer_question(payload: dict):
            if not self.current_question:
                raise HTTPException(status_code=404, detail="No current question")
            
            response_text = payload.get("response", "continue")
            
            try:
                await self._send_response_to_gpt_pilot(response_text)
                question_id = self.current_question.id
                self.stats.questions_processed += 1
                self.current_question = None
                await self._process_next_question()
                
                return {
                    "status": "answered", 
                    "response": response_text,
                    "question_id": question_id
                }
                
            except Exception as e:
                self.logger.error(f"Error sending response: {e}")
                raise HTTPException(status_code=500, detail=str(e))
        
        @app.get("/api/questions/pending")
        async def get_pending_questions():
            return [
                {
                    "id": q.id,
                    "question": q.question,
                    "timestamp": q.timestamp,
                    "age": time.time() - q.timestamp
                }
                for q in self.pending_questions
            ]
        
        return app
    
    async def _send_response_to_gpt_pilot(self, response: str):
        if not self.gpt_pilot_writer:
            raise Exception("GPT-Pilot not connected")
        
        response_msg = {
            "type": MessageType.RESPONSE,
            "content": response
        }
        
        response_data = json.dumps(response_msg).encode('utf-8')
        self.gpt_pilot_writer.write(len(response_data).to_bytes(4, byteorder='big'))
        self.gpt_pilot_writer.write(response_data)
        await self.gpt_pilot_writer.drain()
        
        self.stats.messages_sent += 1
        self.logger.info(f"Response sent to GPT-Pilot: {response}")
    
    async def _process_next_question(self):
        if self.current_question or not self.pending_questions:
            return
        
        self.current_question = self.pending_questions.popleft()
        self.logger.info(f"New question available: {self.current_question.id}")
    
    async def handle_gpt_pilot_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        client_addr = writer.get_extra_info('peername')
        self.logger.info(f"GPT-Pilot connected from {client_addr}")
        self.gpt_pilot_writer = writer
        
        try:
            while True:
                try:
                    data = await reader.readexactly(4)
                    msg_len = int.from_bytes(data, byteorder='big')
                except asyncio.IncompleteReadError:
                    break
                
                try:
                    data = await reader.readexactly(msg_len)
                    message = json.loads(data.decode('utf-8'))
                except (asyncio.IncompleteReadError, json.JSONDecodeError) as e:
                    self.logger.error(f"Error reading message: {e}")
                    self.stats.errors += 1
                    break
                
                await self._process_gpt_pilot_message(message)
                
        except Exception as e:
            self.logger.error(f"Error handling GPT-Pilot client: {e}")
            self.stats.errors += 1
        finally:
            self.logger.info(f"GPT-Pilot disconnected from {client_addr}")
            self.gpt_pilot_writer = None
            writer.close()
            await writer.wait_closed()
    
    async def _process_gpt_pilot_message(self, message: Dict[str, Any]):
        msg_type = message.get('type')
        content = message.get('content', '')
        
        self.stats.messages_received += 1
        self.logger.debug(f"Received from GPT-Pilot: {msg_type}")
        
        if msg_type == MessageType.USER_INPUT_REQUEST:
            question = PendingQuestion(
                question=str(content),
                context=message,
                writer=self.gpt_pilot_writer
            )
            
            self.pending_questions.append(question)
            self.logger.info(f"Question queued: {question.id}")
            
            if not self.current_question:
                await self._process_next_question()
        
        elif msg_type == MessageType.EXIT:
            self.logger.info("GPT-Pilot is exiting")
    
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