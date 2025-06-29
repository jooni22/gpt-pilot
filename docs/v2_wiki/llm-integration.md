# Integracja z modelami LLM

## 🧠 Przegląd systemu LLM

GPT-Pilot obsługuje różne modele językowe poprzez ujednolicony interfejs. System jest zaprojektowany tak, aby łatwo dodawać nowe dostawców LLM bez wpływu na resztkę aplikacji.

## 🔌 Obsługiwane dostawcy

### 1. OpenAI (`openai_client.py`)
**Obsługiwane modele:**
- GPT-4 (zalecany)
- GPT-4 Turbo
- GPT-3.5 Turbo

**Konfiguracja:**
```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key": "your-api-key",
    "temperature": 0.7
  }
}
```

### 2. Anthropic (`anthropic_client.py`)
**Obsługiwane modele:**
- Claude-3 Opus
- Claude-3 Sonnet
- Claude-3 Haiku

**Konfiguracja:**
```json
{
  "llm": {
    "provider": "anthropic",
    "model": "claude-3-sonnet-20240229",
    "api_key": "your-api-key"
  }
}
```

### 3. Groq (`groq_client.py`)
**Obsługiwane modele:**
- Llama 3.1 70B
- Mixtral 8x7B
- Gemma 7B

**Konfiguracja:**
```json
{
  "llm": {
    "provider": "groq",
    "model": "llama-3.1-70b-versatile",
    "api_key": "your-api-key"
  }
}
```### 4. Azure OpenAI (`azure_client.py`)
**Obsługiwane modele:**
- GPT-4 (Azure deployment)
- GPT-3.5 Turbo (Azure deployment)

**Konfiguracja:**
```json
{
  "llm": {
    "provider": "azure",
    "endpoint": "https://your-resource.openai.azure.com/",
    "api_key": "your-api-key",
    "deployment_name": "your-deployment-name"
  }
}
```

## 🏗️ Architektura systemu LLM

### Klasa bazowa (`base.py`)
Wszystkie klienty LLM implementują interfejs `BaseLLMClient`:

```python
class BaseLLMClient:
    def __init__(self, config):
        self.config = config
    
    def send_request(self, messages, **kwargs):
        """Wysyła żądanie do modelu LLM"""
        raise NotImplementedError
    
    def stream_request(self, messages, **kwargs):
        """Wysyła żądanie ze streamingiem odpowiedzi"""
        raise NotImplementedError
```

### Zarządzanie konwersacją (`convo.py`)
Klasa `Conversation` zarządza historią rozmowy:
- Przechowuje historię wiadomości
- Zarządza kontekstem
- Optymalizuje długość promptów

### Parsowanie odpowiedzi (`parser.py`)
System parsowania odpowiedzi od LLM:
- Ekstraktuje kod z odpowiedzi
- Parsuje instrukcje JSON
- Waliduje format odpowiedzi

## 📝 System promptów

### Struktura promptu (`prompt.py`)
```python
class Prompt:
    def __init__(self, template_path):
        self.template = self.load_template(template_path)
    
    def render(self, **kwargs):
        """Renderuje prompt z danymi"""
        return self.template.format(**kwargs)
```

### Typy promptów:
- **System prompts** - Definiują rolę agenta
- **Task prompts** - Opisują konkretne zadanie
- **Context prompts** - Dostarczają kontekst projektu

## 🔧 Konfiguracja

### Plik konfiguracyjny (`config.json`)
```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key": "your-api-key",
    "temperature": 0.7,
    "max_tokens": 4096,
    "timeout": 60,
    "retry_attempts": 3
  }
}
```

### Zmienne środowiskowe
```bash
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
export GROQ_API_KEY="your-groq-key"
```

## 📊 Logowanie i monitoring

### Request logging (`request_log.py`)
System loguje wszystkie żądania do LLM:
- Timestamp żądania
- Użyty model
- Długość promptu
- Czas odpowiedzi
- Koszt żądania (jeśli dostępny)

### Metryki wydajności:
- Średni czas odpowiedzi
- Liczba tokenów użytych
- Współczynnik sukcesu żądań
- Koszty API

## 🚀 Optymalizacje

### Cachowanie odpowiedzi
- Cache lokalny dla powtarzających się promptów
- Inteligentne zarządzanie pamięcią cache

### Zarządzanie kontekstem
- Automatyczne skracanie długich konwersacji
- Priorytetyzacja ważnych informacji

### Retry logic
- Automatyczne ponowne próby przy błędach
- Exponential backoff dla rate limiting

## 🔒 Bezpieczeństwo

### Zarządzanie kluczami API
- Bezpieczne przechowywanie credentials
- Rotacja kluczy API
- Walidacja uprawnień

### Filtrowanie treści
- Walidacja promptów przed wysłaniem
- Filtrowanie potencjalnie szkodliwych treści
- Monitoring nietypowych żądań

## 🛠️ Rozwiązywanie problemów

### Typowe błędy:
1. **Rate limiting** - Zbyt wiele żądań
2. **Token limit exceeded** - Prompt zbyt długi
3. **Authentication failed** - Nieprawidłowy klucz API
4. **Model not available** - Model niedostępny

### Debugowanie:
```python
# Włączenie szczegółowego logowania
logging.getLogger('llm').setLevel(logging.DEBUG)

# Test połączenia z LLM
client = OpenAIClient(config)
response = client.send_request([{"role": "user", "content": "Hello"}])
```