# Integracja z lokalnym agentem sterującym

## 🤖 Przegląd rozwiązań

Jeśli chcesz sterować GPT-Pilot poprzez własnego lokalnego agenta zamiast VS Code, masz kilka opcji wykorzystujących istniejące mechanizmy.

## 🔧 Rozwiązanie 1: Rozszerzenie IPC Client (Zalecane)

### Wykorzystanie istniejącego protokołu IPC

Możesz stworzyć własnego agenta, który będzie działał jako "mock VS Code extension":

```python
# custom_agent_server.py
import asyncio
import json
from typing import Dict, Any, Optional

class LocalAgentServer:
    """
    Lokalny agent sterujący GPT-Pilot przez protokół IPC
    """
    
    def __init__(self, host="localhost", port=8125):
        self.host = host
        self.port = port
        self.server = None
        self.writer = None
        self.message_handlers = {}
        self.conversation_state = {}
        
    def add_handler(self, message_type: str, handler):
        """Dodaj handler dla konkretnego typu wiadomości"""
        self.message_handlers[message_type] = handler
        
    async def handle_connection(self, reader, writer):
        """Obsługa połączenia z GPT-Pilot"""
        self.writer = writer
        print("🔗 GPT-Pilot connected")
        
        try:
            while True:
                # Odczytaj długość wiadomości (4 bajty)
                length_data = await reader.read(4)
                if not length_data:
                    break
                    
                message_length = int.from_bytes(length_data, byteorder="big")
                
                # Odczytaj wiadomość JSON
                message_data = await reader.read(message_length)
                message = json.loads(message_data.decode("utf-8"))
                
                print(f"📨 Received: {message['type']}")
                
                # Przetwórz wiadomość
                await self.process_message(message)
                
        except Exception as e:
            print(f"❌ Connection error: {e}")
        finally:
            writer.close()
            await writer.wait_closed()
            print("🔌 GPT-Pilot disconnected")
    
    async def process_message(self, message: Dict[str, Any]):
        """Przetwórz otrzymaną wiadomość"""
        msg_type = message.get("type")
        
        if msg_type in self.message_handlers:
            response = await self.message_handlers[msg_type](message)
            if response:
                await self.send_response(response)
        else:
            # Domyślna obsługa
            await self.default_handler(message)
    
    async def send_response(self, response: str):
        """Wyślij odpowiedź do GPT-Pilot"""
        if self.writer:
            response_json = json.dumps({
                "type": "response",
                "content": response
            })
            response_bytes = response_json.encode("utf-8")
            self.writer.write(response_bytes)
            await self.writer.drain()
    
    async def default_handler(self, message: Dict[str, Any]):
        """Domyślna obsługa wiadomości"""
        msg_type = message.get("type")
        content = message.get("content", "")
        
        if msg_type == "user_input_request":
            # GPT-Pilot pyta o coś
            question = content
            print(f"❓ Question: {question}")
            
            # Tutaj Twój agent może:
            # 1. Analizować pytanie
            # 2. Sprawdzić stan konwersacji
            # 3. Podjąć autonomiczną decyzję
            # 4. Lub zapytać zewnętrzny system
            
            response = await self.ai_decision_maker(question, message)
            await self.send_response(response)
            
        elif msg_type == "stream":
            # GPT-Pilot streamuje tekst
            print(f"💬 Stream: {content}", end="")
            
        elif msg_type == "verbose":
            # Zwykła wiadomość
            category = message.get("category", "system")
            print(f"📢 [{category}] {content}")
            
        elif msg_type == "progress":
            # Informacja o postępie
            task_info = content.get("task", {})
            print(f"⏳ Progress: {task_info.get('description', 'Unknown task')}")
    
    async def ai_decision_maker(self, question: str, context: Dict[str, Any]) -> str:
        """
        Twój AI agent podejmuje decyzje
        """
        # Przykład prostej logiki decyzyjnej
        question_lower = question.lower()
        
        # Analiza kontekstu
        category = context.get("category", "")
        
        if "project name" in question_lower:
            return "MyAwesomeApp"
            
        elif "continue" in question_lower or "proceed" in question_lower:
            return "yes"
            
        elif "technology" in question_lower or "template" in question_lower:
            return "vite_react"  # Wybierz szablon
            
        elif "description" in question_lower:
            return "A modern web application built with React and TypeScript"
            
        # Dla bardziej złożonych pytań - integracja z LLM
        elif "agent:architect" in category:
            return await self.consult_llm_for_architecture(question)
            
        elif "agent:developer" in category:
            return await self.consult_llm_for_development(question)
        
        # Domyślna odpowiedź
        return "continue"
    
    async def consult_llm_for_architecture(self, question: str) -> str:
        """Skonsultuj się z LLM dla pytań architektonicznych"""
        # Tutaj możesz zintegrować z OpenAI, Anthropic, etc.
        # Przykład:
        """
        import openai
        
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert software architect."},
                {"role": "user", "content": f"GPT-Pilot asks: {question}. Provide a brief, practical answer."}
            ]
        )
        return response.choices[0].message.content
        """
        return "continue"  # Placeholder
    
    async def consult_llm_for_development(self, question: str) -> str:
        """Skonsultuj się z LLM dla pytań deweloperskich"""
        # Podobnie jak wyżej, ale z kontekstem deweloperskim
        return "continue"  # Placeholder
    
    async def start(self):
        """Uruchom serwer agenta"""
        print(f"🚀 Starting Local Agent Server on {self.host}:{self.port}")
        self.server = await asyncio.start_server(
            self.handle_connection,
            self.host,
            self.port
        )
        
        print(f"✅ Agent ready! GPT-Pilot can now connect to {self.host}:{self.port}")
        async with self.server:
            await self.server.serve_forever()

# Przykład użycia
async def main():
    agent = LocalAgentServer()
    
    # Dodaj własne handlery
    async def custom_progress_handler(message):
        print(f"🎯 Custom progress handler: {message}")
        return None
    
    agent.add_handler("progress", custom_progress_handler)
    
    # Uruchom serwer
    await agent.start()

if __name__ == "__main__":
    asyncio.run(main())
```

## 🔧 Rozwiązanie 2: Nowy adapter UI

Alternatywnie, możesz stworzyć nowy adapter UI bezpośrednio w GPT-Pilot:

```python
# core/ui/agent_ui.py
from typing import Optional
import asyncio
import json
from core.ui.base import UIBase, UISource, UserInput
from core.log import get_logger

log = get_logger(__name__)

class LocalAgentUI(UIBase):
    """
    UI adapter dla lokalnego agenta sterującego
    """
    
    def __init__(self, agent_endpoint: str = "http://localhost:9000"):
        self.agent_endpoint = agent_endpoint
        self.session = None
        
    async def start(self) -> bool:
        """Połącz z lokalnym agentem"""
        try:
            # Tutaj możesz użyć HTTP, WebSocket, lub innego protokołu
            import aiohttp
            self.session = aiohttp.ClientSession()
            
            # Test connection
            async with self.session.get(f"{self.agent_endpoint}/health") as resp:
                if resp.status == 200:
                    log.info("Connected to local agent")
                    return True
                    
        except Exception as e:
            log.error(f"Failed to connect to local agent: {e}")
            return False
    
    async def stop(self):
        """Rozłącz z agentem"""
        if self.session:
            await self.session.close()
    
    async def ask_question(
        self,
        question: str,
        *,
        buttons: Optional[dict[str, str]] = None,
        **kwargs
    ) -> UserInput:
        """Zadaj pytanie lokalnemu agentowi"""
        
        payload = {
            "type": "question",
            "question": question,
            "buttons": buttons,
            "context": kwargs
        }
        
        try:
            async with self.session.post(
                f"{self.agent_endpoint}/decide",
                json=payload
            ) as resp:
                result = await resp.json()
                
                if result.get("button"):
                    return UserInput(button=result["button"])
                else:
                    return UserInput(text=result.get("text", ""))
                    
        except Exception as e:
            log.error(f"Agent decision failed: {e}")
            # Fallback - zwróć domyślną odpowiedź
            if buttons:
                return UserInput(button=list(buttons.keys())[0])
            return UserInput(text="continue")
    
    async def send_message(
        self,
        message: str,
        *,
        source: Optional[UISource] = None,
        **kwargs
    ):
        """Wyślij wiadomość do agenta (dla obserwacji)"""
        payload = {
            "type": "message",
            "content": message,
            "source": source.type_name if source else None,
            "context": kwargs
        }
        
        try:
            async with self.session.post(
                f"{self.agent_endpoint}/observe",
                json=payload
            ) as resp:
                pass  # Agent może logować lub analizować
        except Exception as e:
            log.debug(f"Failed to send observation to agent: {e}")
    
    # Implementuj pozostałe metody...
    async def send_stream_chunk(self, chunk: Optional[str], **kwargs):
        # Możesz streamować do agenta lub ignorować
        pass
```

## 🔧 Rozwiązanie 3: WebSocket Agent

Dla bardziej zaawansowanej komunikacji dwukierunkowej:

```python
# websocket_agent.py
import asyncio
import websockets
import json
from typing import Dict, Any

class WebSocketAgent:
    """
    Agent komunikujący się przez WebSocket
    """
    
    def __init__(self, port=9001):
        self.port = port
        self.clients = set()
        self.conversation_state = {}
        
    async def register_client(self, websocket, path):
        """Zarejestruj nowego klienta (GPT-Pilot)"""
        self.clients.add(websocket)
        print(f"🔗 Client connected: {websocket.remote_address}")
        
        try:
            async for message in websocket:
                data = json.loads(message)
                response = await self.handle_message(data)
                
                if response:
                    await websocket.send(json.dumps(response))
                    
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            self.clients.remove(websocket)
            print(f"🔌 Client disconnected")
    
    async def handle_message(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Obsłuż wiadomość od GPT-Pilot"""
        msg_type = data.get("type")
        
        if msg_type == "question":
            # Autonomiczna decyzja
            question = data.get("question", "")
            decision = await self.make_decision(question, data)
            
            return {
                "type": "answer",
                "content": decision
            }
            
        elif msg_type == "status":
            # Aktualizacja statusu
            await self.update_status(data)
            
        return None
    
    async def make_decision(self, question: str, context: Dict[str, Any]) -> str:
        """Podejmij autonomiczną decyzję"""
        # Twoja logika AI/ML
        # Możesz tutaj:
        # 1. Analizować historię konwersacji
        # 2. Używać reguł biznesowych
        # 3. Konsultować z zewnętrznym LLM
        # 4. Używać modeli ML do predykcji
        
        return "continue"  # Placeholder
    
    async def start_server(self):
        """Uruchom serwer WebSocket"""
        print(f"🚀 WebSocket Agent starting on port {self.port}")
        
        start_server = websockets.serve(
            self.register_client,
            "localhost",
            self.port
        )
        
        await start_server
        print(f"✅ WebSocket Agent ready on ws://localhost:{self.port}")
        
        # Utrzymuj serwer
        await asyncio.Future()  # Run forever

# Uruchomienie
if __name__ == "__main__":
    agent = WebSocketAgent()
    asyncio.run(agent.start_server())
```

## 🚀 Integracja z GPT-Pilot

### Konfiguracja dla IPC Agent:

```json
{
  "ui": {
    "type": "ipc",
    "host": "localhost",
    "port": 8125
  }
}
```

### Konfiguracja dla HTTP Agent:

```json
{
  "ui": {
    "type": "agent",
    "endpoint": "http://localhost:9000"
  }
}
```

## 🧠 Zaawansowane możliwości agenta

### 1. Analiza kontekstu
```python
class ContextAnalyzer:
    def __init__(self):
        self.conversation_history = []
        self.project_state = {}
    
    def analyze_question(self, question: str, context: dict) -> str:
        """Analizuj pytanie w kontekście całej konwersacji"""
        
        # Dodaj do historii
        self.conversation_history.append({
            "question": question,
            "context": context,
            "timestamp": time.time()
        })
        
        # Analiza wzorców
        if self.is_repetitive_question(question):
            return self.get_cached_response(question)
            
        # Analiza fazy projektu
        if context.get("category") == "agent:architect":
            return self.architectural_decision(question)
            
        return "continue"
```

### 2. Integracja z LLM
```python
async def llm_consultation(self, question: str, context: dict) -> str:
    """Skonsultuj decyzję z zewnętrznym LLM"""
    
    system_prompt = f"""
    Jesteś agentem sterującym GPT-Pilot. 
    Projekt: {context.get('project_name', 'Unknown')}
    Faza: {context.get('category', 'Unknown')}
    
    Odpowiedz krótko i konkretnie na pytanie GPT-Pilot.
    """
    
    # Użyj swojego ulubionego LLM API
    response = await your_llm_client.chat(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    
    return response.content
```

## 🎯 Zalecenia

1. **Zacznij od Rozwiązania 1** - wykorzystaj gotowy protokół IPC
2. **Dodaj logikę decyzyjną** - reguły biznesowe + LLM consultation
3. **Monitoruj stan** - śledź postęp i podejmuj inteligentne decyzje
4. **Testuj stopniowo** - zacznij od prostych odpowiedzi, rozbudowuj

## 🔧 Przykład uruchomienia

```bash
# Terminal 1: Uruchom agenta
python custom_agent_server.py

# Terminal 2: Uruchom GPT-Pilot z konfiguracją IPC
python main.py --config config-with-ipc.json
```

Ten sposób pozwala na pełną kontrolę nad GPT-Pilot przez Twojego lokalnego agenta, wykorzystując istniejące, przetestowane mechanizmy komunikacji.