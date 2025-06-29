# System interfejsu użytkownika (UI)

## 🖥️ Przegląd systemu UI

GPT-Pilot posiada elastyczny system interfejsu użytkownika oparty na wzorcu adaptera, który pozwala na obsługę różnych typów interfejsów: konsoli, rozszerzenia VS Code oraz trybu testowego.

## 🏗️ Architektura systemu UI

### Klasa bazowa (`base.py`)

System UI jest oparty na abstrakcyjnej klasie `UIBase`, która definiuje jednolity interfejs dla wszystkich implementacji:

```python
class UIBase:
    async def start(self) -> bool:
        """Uruchomienie adaptera UI"""
        
    async def stop(self):
        """Zatrzymanie adaptera UI"""
        
    async def send_message(self, message: str, *, source: UISource = None):
        """Wysłanie wiadomości do użytkownika"""
        
    async def ask_question(self, question: str, **kwargs) -> UserInput:
        """Zadanie pytania użytkownikowi"""
```

### Kluczowe komponenty

#### 1. UISource - Źródło wiadomości
```python
class UISource:
    display_name: str  # Nazwa wyświetlana (np. "Product Owner")
    type_name: str     # Typ źródła (np. "agent:product-owner")

class AgentSource(UISource):
    # Specjalizacja dla agentów
    def __init__(self, display_name: str, agent_type: str):
        super().__init__(display_name, f"agent:{agent_type}")
```

#### 2. UserInput - Odpowiedź użytkownika
```python
class UserInput(BaseModel):
    text: Optional[str] = None      # Tekst wprowadzony przez użytkownika
    button: Optional[str] = None    # Naciśnięty przycisk
    cancelled: bool = False         # Czy użytkownik anulował
```

#### 3. ProjectStage - Etapy projektu
```python
class ProjectStage(str, Enum):
    PROJECT_NAME = "project_name"
    PROJECT_DESCRIPTION = "project_description"
    BREAKDOWN_CHAT = "breakdown_chat"
    TEST_APP = "test_app"
    # ... inne etapy
```

## 🔌 Implementacje UI

### 1. Console UI (`console.py`)
**Przeznaczenie:** Interfejs konsolowy dla użytkowników terminala

**Kluczowe cechy:**
- Prosty interfejs tekstowy
- Używa `prompt_toolkit` do interakcji
- Obsługuje przyciski jako opcje wyboru
- Wsparcie dla kolorów i formatowania

**Przykład użycia:**
```python
ui = PlainConsoleUI()
await ui.start()
response = await ui.ask_question(
    "Czy chcesz kontynuować?",
    buttons={"yes": "Tak", "no": "Nie"}
)
```

### 2. IPC Client UI (`ipc_client.py`)
**Przeznaczenie:** Komunikacja z rozszerzeniem VS Code

**Kluczowe cechy:**
- Protokół IPC przez TCP/IP (domyślnie port 8125)
- Asynchroniczna komunikacja
- Obsługuje streaming wiadomości
- Kompleksne typy wiadomości (progress, diff, debugowanie)

**Protokół komunikacji:**
```python
class MessageType(str, Enum):
    STREAM = "stream"              # Streaming tekstu
    VERBOSE = "verbose"            # Zwykłe wiadomości
    USER_INPUT_REQUEST = "user_input_request"  # Pytania
    PROGRESS = "progress"          # Postęp zadań
    GENERATE_DIFF = "generateDiff" # Generowanie diff-ów
    # ... inne typy
```

**Struktura wiadomości:**
```python
class Message(BaseModel):
    type: MessageType
    category: Optional[str] = None    # Kategoria źródła
    content: Union[str, dict, None] = None
    project_state_id: Optional[str] = None
    extra_info: Optional[str] = None
```

### 3. Virtual UI (`virtual.py`)
**Przeznaczenie:** Testowanie i automatyzacja

**Kluczowe cechy:**
- Symuluje interakcję użytkownika
- Predefiniowane odpowiedzi
- Brak rzeczywistej interakcji
- Idealne do testów automatycznych

**Przykład konfiguracji:**
```python
virtual_inputs = [
    {"text": "My Todo App"},
    {"button": "yes"},
    {"text": "Simple task management"}
]
ui = VirtualUI(virtual_inputs)
```

## 📊 Funkcjonalności UI

### Podstawowe operacje
- **Wysyłanie wiadomości** - `send_message()`
- **Streaming tekstu** - `send_stream_chunk()`
- **Zadawanie pytań** - `ask_question()`
- **Pokazywanie postępu** - `send_task_progress()`

### Zaawansowane funkcje
- **Generowanie diff-ów** - `generate_diff()`
- **Otwieranie plików** - `open_editor()`
- **Debugowanie** - `send_data_about_logs()`
- **Statystyki projektu** - `send_project_stats()`
- **Instrukcje testowe** - `send_test_instructions()`

### Funkcje specjalne VS Code
- **Import projektu** - `import_project()`
- **Status plików** - `send_file_status()`
- **Baza wiedzy** - `knowledge_base_update()`
- **Bug Hunter status** - `send_bug_hunter_status()`

## 🔄 Przepływ komunikacji

### Typowy scenariusz:
1. **Inicjalizacja:** `await ui.start()`
2. **Wysłanie wiadomości:** `await ui.send_message("Starting project...")`
3. **Zadanie pytania:** `response = await ui.ask_question("Project name?")`
4. **Pokazanie postępu:** `await ui.send_task_progress(1, 5, "Creating files")`
5. **Zakończenie:** `await ui.stop()`

### Obsługa błędów:
```python
try:
    response = await ui.ask_question("Continue?")
except UIClosedError:
    # Użytkownik zamknął interfejs
    log.info("User closed the interface")
    return
```

## 🧪 System testowy

### Struktura testów UI (`tests/ui/`)

#### 1. Testy Console UI (`test_console.py`)
**Testowane scenariusze:**
- Wysyłanie wiadomości z różnymi źródłami
- Streaming tekstu po fragmentach
- Zadawanie prostych pytań
- Pytania z przyciskami
- Obsługa przerwania (Ctrl+C)

**Przykład testu:**
```python
@pytest.mark.asyncio
async def test_send_message(capsys):
    src = AgentSource("Product Owner", "product-owner")
    ui = PlainConsoleUI()
    
    await ui.start()
    await ui.send_message("Hello!", source=src)
    
    captured = capsys.readouterr()
    assert captured.out == "[Product Owner] Hello!\n"
```

#### 2. Testy IPC Client (`test_ipc_client.py`)
**Testowane scenariusze:**
- Komunikacja z mock serverem
- Wysyłanie różnych typów wiadomości
- Obsługa odpowiedzi z przyciskami
- Obsługa błędów połączenia
- Protokół IPC (długość wiadomości + JSON)

**Mock Server:**
```python
class IPCServer:
    """Symuluje rozszerzenie VS Code"""
    def __init__(self, responses: list[dict]):
        self.responses = responses
        self.messages = []  # Zapisuje otrzymane wiadomości
```

**Przykład testu protokołu:**
```python
@pytest.mark.asyncio
async def test_ask_question_buttons():
    server_responses = [{
        "type": "response",
        "content": "Yes, I'm sure"
    }]
    
    async with IPCServer(server_responses) as (port, messages):
        ui = IPCClientUI(LocalIPCConfig(port=port))
        answer = await ui.ask_question(
            "Are you sure?",
            buttons={"yes": "Yes, I'm sure", "no": "No"}
        )
        
        assert answer.button == "yes"
```

### Pokrycie testowe:
- **Console UI:** 100% głównych funkcji
- **IPC Client:** 95% protokołu komunikacji
- **Virtual UI:** Podstawowe funkcje (używane w innych testach)

## ⚙️ Konfiguracja

### Console UI
Nie wymaga konfiguracji - działa out-of-the-box.

### IPC Client UI
```python
from core.config import LocalIPCConfig

config = LocalIPCConfig(
    host="localhost",  # Domyślnie localhost
    port=8125         # Domyślny port VS Code
)
ui = IPCClientUI(config)
```

### Virtual UI
```python
# Predefiniowane odpowiedzi
inputs = [
    {"text": "My App"},
    {"button": "continue"},
    {"text": "Description"}
]
ui = VirtualUI(inputs)
```

## 🚀 Rozszerzanie systemu UI

### Dodawanie nowego adaptera UI:
1. Dziedzicz z `UIBase`
2. Implementuj wszystkie abstrakcyjne metody
3. Dodaj specyficzną logikę dla swojego interfejsu
4. Utwórz testy w `tests/ui/`

### Przykład nowego adaptera:
```python
class WebUI(UIBase):
    async def start(self) -> bool:
        # Uruchom serwer web
        pass
        
    async def ask_question(self, question: str, **kwargs) -> UserInput:
        # Wyślij pytanie przez WebSocket
        # Czekaj na odpowiedź z przeglądarki
        pass
```

## 📈 Metryki i monitoring

System UI loguje:
- Liczbę wysłanych wiadomości
- Czas odpowiedzi użytkownika
- Błędy połączenia (IPC)
- Statystyki użycia przycisków vs. tekst

## 🔒 Bezpieczeństwo

### IPC Client:
- Ograniczenie rozmiaru wiadomości (512KB)
- Tylko localhost connections
- Walidacja JSON-a
- Timeout dla połączeń

### Console UI:
- Sanityzacja wejścia użytkownika
- Obsługa przerwań (Ctrl+C)
- Bezpieczne logowanie (bez API keys)