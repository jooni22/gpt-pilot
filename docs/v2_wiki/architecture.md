# Architektura GPT-Pilot

## 🏗️ Ogólny przegląd

GPT-Pilot to system oparty na architekturze agentów, gdzie każdy agent ma specjalizację w konkretnym obszarze tworzenia oprogramowania. System koordynuje pracę tych agentów, aby automatycznie generować kompletne aplikacje.

## 📊 Diagram architektury

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   main.py       │───▶│   Orchestrator   │───▶│   UI/Console    │
│ (Entry Point)   │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │     Agents       │
                       │                  │
                       │ • Architect      │
                       │ • Developer      │
                       │ • Code Monkey    │
                       │ • Tech Lead      │
                       │ • Bug Hunter     │
                       │ • Troubleshooter │
                       └──────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   LLM System     │
                       │                  │
                       │ • OpenAI         │
                       │ • Anthropic      │
                       │ • Groq           │
                       │ • Azure          │
                       └──────────────────┘
```

## 🔧 Główne komponenty

### 1. Entry Point (`main.py`)
- **Rola:** Punkt wejścia aplikacji
- **Odpowiedzialności:**
  - Parsowanie argumentów wiersza poleceń
  - Inicjalizacja konfiguracji
  - Uruchomienie orchestratora

### 2. Orchestrator (`core/agents/orchestrator.py`)
- **Rola:** Koordynator całego procesu
- **Odpowiedzialności:**
  - Zarządzanie przepływem pracy między agentami
  - Decydowanie, który agent powinien być aktywny
  - Monitorowanie stanu projektu### 3. System Agentów (`core/agents/`)
- **Architect** - Projektuje architekturę aplikacji i wybiera technologie
- **Developer** - Implementuje funkcjonalności i pisze kod
- **Code Monkey** - Wykonuje szczegółowe zmiany w kodzie
- **Tech Lead** - Planuje zadania i zarządza projektem
- **Bug Hunter** - Znajduje i naprawia błędy
- **Troubleshooter** - Rozwiązuje problemy techniczne

### 4. System LLM (`core/llm/`)
- **Rola:** Interfejs do komunikacji z modelami AI
- **Obsługiwane modele:**
  - OpenAI (GPT-3.5, GPT-4)
  - Anthropic (Claude)
  - Groq
  - Azure OpenAI

### 5. System Promptów (`core/prompts/`)
- **Rola:** Zarządzanie szablonami promptów dla każdego agenta
- **Struktura:** Każdy agent ma swój katalog z dedykowanymi promptami

### 6. Szablony Projektów (`core/templates/`)
- **Rola:** Gotowe struktury projektów dla różnych technologii
- **Dostępne szablony:**
  - React + Express
  - Vite + React + TypeScript
  - Node.js + Express + MongoDB
  - Vanilla JavaScript + React

## 🔄 Przepływ pracy

1. **Inicjalizacja:** `main.py` uruchamia orchestrator
2. **Analiza:** Architect analizuje wymagania użytkownika
3. **Planowanie:** Tech Lead tworzy plan implementacji
4. **Implementacja:** Developer i Code Monkey piszą kod
5. **Testowanie:** Bug Hunter sprawdza jakość kodu
6. **Rozwiązywanie problemów:** Troubleshooter naprawia błędy

## 💾 Zarządzanie stanem

- **Baza danych:** SQLite (`data/database/pythagora.db`)
- **Modele:** Zdefiniowane w `core/db/models/`
- **Migracje:** Zarządzane przez Alembic w `core/db/migrations/`

## 🎯 Kluczowe wzorce projektowe

### Agent Pattern
Każdy agent implementuje interfejs bazowy i ma specjalizację:
```python
class BaseAgent:
    def execute(self, task):
        # Wspólna logika
        pass
    
    def get_llm_response(self, prompt):
        # Komunikacja z LLM
        pass
```

### Template Method Pattern
Prompty używają szablonów z placeholderami:
```
You are a {agent_role}. 
Your task is to {task_description}.
Project context: {project_context}
```

### Strategy Pattern
Różne implementacje klientów LLM:
```python
class LLMClient:
    def send_request(self, prompt):
        pass

class OpenAIClient(LLMClient):
    # Implementacja dla OpenAI
    pass
```

## 📈 Skalowalność

System jest zaprojektowany z myślą o:
- **Dodawaniu nowych agentów** - poprzez dziedziczenie z `BaseAgent`
- **Dodawaniu nowych LLM** - poprzez implementację interfejsu `LLMClient`
- **Dodawaniu nowych szablonów** - poprzez rozszerzenie `core/templates/`

## 🔒 Bezpieczeństwo

- **Izolacja procesów** - każdy agent działa w kontrolowanym środowisku
- **Walidacja promptów** - wszystkie prompty są walidowane przed wysłaniem
- **Zarządzanie kluczami API** - bezpieczne przechowywanie credentials