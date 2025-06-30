import asyncio
import json
import time
from enum import Enum
from typing import Dict, Any, Optional


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


class IntelligentAgent:
    """
    Inteligentny agent sterujący GPT-Pilot
    """
    
    def __init__(self):
        self.conversation_history = []
        self.project_state = {
            "name": None,
            "description": None,
            "current_phase": "initialization",
            "decisions_made": []
        }
        self.auto_responses = {
            # Automatyczne odpowiedzi dla typowych pytań
            "project_name": "MyAIApp",
            "project_description": "Nowoczesna aplikacja webowa z React i TypeScript",
            "template_choice": "vite_react",
            "continue_development": "yes",
            "technology_stack": "React, TypeScript, Node.js, Express"
        }
    
    def log_interaction(self, message_type: str, content: str, response: str = None):
        """Loguj interakcję dla analizy"""
        interaction = {
            "timestamp": time.time(),
            "type": message_type,
            "content": content[:100] + "..." if len(content) > 100 else content,
            "response": response,
            "phase": self.project_state["current_phase"]
        }
        self.conversation_history.append(interaction)
        print(f"📝 [{message_type}] {content[:50]}{'...' if len(content) > 50 else ''}")
        if response:
            print(f"🤖 Response: {response}")
    
    def analyze_question(self, question: str, context: Dict[str, Any]) -> str:
        """
        Analizuj pytanie i podejmij inteligentną decyzję
        """
        question_lower = question.lower()
        category = context.get("category", "")
        
        # Aktualizuj fazę projektu na podstawie kategorii agenta
        if "architect" in category:
            self.project_state["current_phase"] = "architecture"
        elif "developer" in category:
            self.project_state["current_phase"] = "development"
        elif "tech-lead" in category:
            self.project_state["current_phase"] = "planning"
        
        # Logika podejmowania decyzji
        decision = self._make_decision(question_lower, context)
        
        # Zapisz decyzję
        self.project_state["decisions_made"].append({
            "question": question,
            "decision": decision,
            "timestamp": time.time(),
            "context": category
        })
        
        return decision
    
    def _make_decision(self, question_lower: str, context: Dict[str, Any]) -> str:
        """Logika podejmowania decyzji"""
        
        # 1. Pytania o nazwę projektu
        if any(keyword in question_lower for keyword in ["project name", "nazwa projektu", "app name"]):
            return self.auto_responses["project_name"]
        
        # 2. Pytania o opis projektu
        if any(keyword in question_lower for keyword in ["description", "opis", "what should", "co ma"]):
            return self.auto_responses["project_description"]
        
        # 3. Wybór szablonu/technologii
        if any(keyword in question_lower for keyword in ["template", "szablon", "technology", "technologia"]):
            return self.auto_responses["template_choice"]
        
        # 4. Pytania o kontynuację
        if any(keyword in question_lower for keyword in ["continue", "kontynuować", "proceed", "dalej"]):
            return self.auto_responses["continue_development"]
        
        # 5. Pytania tak/nie
        if any(keyword in question_lower for keyword in ["are you sure", "czy jesteś pewien", "confirm"]):
            return "yes"
        
        # 6. Pytania o stos technologiczny
        if any(keyword in question_lower for keyword in ["stack", "stos", "technologies", "technologie"]):
            return self.auto_responses["technology_stack"]
        
        # 7. Pytania architektoniczne (od Architect agenta)
        if "architect" in context.get("category", ""):
            return self._architectural_decision(question_lower)
        
        # 8. Pytania deweloperskie (od Developer agenta)
        if "developer" in context.get("category", ""):
            return self._development_decision(question_lower)
        
        # 9. Domyślna odpowiedź
        return "continue"
    
    def _architectural_decision(self, question: str) -> str:
        """Decyzje architektoniczne"""
        if "database" in question:
            return "SQLite for development, PostgreSQL for production"
        elif "authentication" in question:
            return "JWT with refresh tokens"
        elif "api" in question:
            return "REST API with Express.js"
        return "continue"
    
    def _development_decision(self, question: str) -> str:
        """Decyzje deweloperskie"""
        if "implement" in question:
            return "yes"
        elif "test" in question:
            return "continue with implementation"
        elif "error" in question or "błąd" in question:
            return "please fix the error and continue"
        return "continue"
    
    def update_project_info(self, message_type: str, content: Any):
        """Aktualizuj informacje o projekcie"""
        if message_type == MessageType.PROJECT_DESCRIPTION:
            self.project_state["description"] = content
        elif message_type == MessageType.PROJECT_FOLDER_NAME:
            self.project_state["name"] = content
        elif message_type == MessageType.PROGRESS:
            # Analizuj postęp i aktualizuj fazę
            if isinstance(content, dict):
                task_info = content.get("task", {})
                source = task_info.get("source", "")
                if source:
                    self.project_state["current_phase"] = source
    
    def get_status_summary(self) -> str:
        """Zwróć podsumowanie stanu agenta"""
        return f"""
🤖 Agent Status:
📁 Project: {self.project_state.get('name', 'Unknown')}
📝 Description: {self.project_state.get('description', 'Not set')}
🔄 Phase: {self.project_state['current_phase']}
💭 Decisions made: {len(self.project_state['decisions_made'])}
📊 Interactions: {len(self.conversation_history)}
        """.strip()


# Globalny agent
agent = IntelligentAgent()


async def handle_client(reader, writer):
    client_addr = writer.get_extra_info('peername')
    print(f"🔗 GPT-Pilot connected from {client_addr}")
    print(agent.get_status_summary())
    
    try:
        while True:
            # Read message length (4 bytes)
            try:
                data = await reader.readexactly(4)
                msg_len = int.from_bytes(data, byteorder='big')
            except asyncio.IncompleteReadError:
                break
            
            # Read message content
            try:
                data = await reader.readexactly(msg_len)
                message = json.loads(data.decode('utf-8'))
            except (asyncio.IncompleteReadError, json.JSONDecodeError) as e:
                print(f"❌ Error reading message: {e}")
                break
            
            # Process message
            await process_message(message, writer)
            
    except Exception as e:
        print(f"❌ Error handling client: {e}")
    finally:
        print(f"🔌 GPT-Pilot disconnected from {client_addr}")
        writer.close()
        await writer.wait_closed()


async def process_message(message: Dict[str, Any], writer):
    """Przetwórz wiadomość od GPT-Pilot"""
    msg_type = message.get('type')
    content = message.get('content', '')
    category = message.get('category', '')
    
    # Aktualizuj informacje o projekcie
    agent.update_project_info(msg_type, content)
    
    # Obsłuż różne typy wiadomości
    if msg_type == MessageType.USER_INPUT_REQUEST:
        # GPT-Pilot zadaje pytanie - podejmij decyzję
        question = str(content)
        decision = agent.analyze_question(question, message)
        
        agent.log_interaction("QUESTION", question, decision)
        
        # Wyślij odpowiedź
        await send_response(writer, decision)
        
    elif msg_type == MessageType.STREAM:
        # Streaming tekstu - loguj dla kontekstu
        agent.log_interaction("STREAM", str(content))
        
    elif msg_type == MessageType.VERBOSE:
        # Zwykła wiadomość - loguj
        agent.log_interaction("MESSAGE", f"[{category}] {content}")
        
    elif msg_type == MessageType.PROGRESS:
        # Informacja o postępie
        if isinstance(content, dict):
            task_info = content.get("task", {})
            description = task_info.get("description", "Unknown task")
            status = task_info.get("status", "unknown")
            agent.log_interaction("PROGRESS", f"{description} ({status})")
        
    elif msg_type == MessageType.EXIT:
        # GPT-Pilot kończy pracę
        print("👋 GPT-Pilot is exiting")
        print("\n" + "="*50)
        print("📊 FINAL SUMMARY:")
        print(agent.get_status_summary())
        print("="*50)
        
    else:
        # Inne typy wiadomości - loguj
        agent.log_interaction("OTHER", f"{msg_type}: {str(content)[:100]}")


async def send_response(writer, response_content: str):
    """Wyślij odpowiedź do GPT-Pilot"""
    response = {
        "type": MessageType.RESPONSE,
        "content": response_content
    }
    
    response_data = json.dumps(response).encode('utf-8')
    writer.write(response_data)
    await writer.drain()


async def main():
    print("🚀 Starting Intelligent GPT-Pilot Agent Server")
    print("=" * 50)
    
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8125)

    addr = server.sockets[0].getsockname()
    print(f'✅ Server running on {addr[0]}:{addr[1]}')
    print(f'💡 GPT-Pilot can now connect with IPC configuration')
    print("=" * 50)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        print("\n📊 FINAL AGENT SUMMARY:")
        print(agent.get_status_summary())
