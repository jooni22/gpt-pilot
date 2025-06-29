# System Agentów GPT-Pilot

## 🤖 Przegląd agentów

GPT-Pilot wykorzystuje system specjalizowanych agentów, z których każdy ma konkretną rolę w procesie tworzenia aplikacji. Każdy agent dziedziczy z klasy bazowej `BaseAgent` i implementuje specyficzną logikę.

## 👥 Lista agentów

### 1. Architect (`architect.py`)
**Rola:** Architekt systemu  
**Odpowiedzialności:**
- Analiza wymagań użytkownika
- Wybór odpowiednich technologii
- Projektowanie architektury aplikacji
- Konfiguracja szablonów projektów

**Kluczowe prompty:**
- `system.prompt` - Definicja roli architekta
- `select_templates.prompt` - Wybór szablonu projektu
- `configure_template.prompt` - Konfiguracja wybranego szablonu

### 2. Developer (`developer.py`)
**Rola:** Główny deweloper  
**Odpowiedzialności:**
- Implementacja funkcjonalności
- Pisanie kodu aplikacji
- Strukturyzacja projektu
- Podział zadań na mniejsze części
- Zarządzanie cyklem rozwoju z możliwością interwencji użytkownika

**Szczegółowy przepływ pracy:**
1. `execute_task` - Rozpoczęcie wykonywania zadania
2. `step_human_intervention` - Sprawdzenie czy potrzebna interwencja użytkownika
3. `send_message` - Komunikacja z użytkownikiem/systemem
4. `development_task_check` - Weryfikacja postępu zadania
5. `task_post_processing` - Przetwarzanie wyników
6. `continue_development` - Decyzja o kontynuacji lub zakończeniu

**Kluczowe prompty:**
- `system.prompt` - Definicja roli developera
- `breakdown.prompt` - Podział zadań na części
- `filter_files.prompt` - Filtrowanie plików do modyfikacji
- `iteration.prompt` - Iteracyjne ulepszanie kodu

### 3. Code Monkey (`code_monkey.py`)
**Rola:** Wykonawca szczegółowych zmian w kodzie  
**Odpowiedzialności:**
- Implementacja konkretnych zmian w plikach
- Refaktoryzacja kodu
- Dodawanie nowych funkcji
- Modyfikacja istniejącego kodu

**Kluczowe prompty:**
- `implement_changes.prompt` - Implementacja zmian
- `describe_file.prompt` - Opis zawartości pliku
- `review_changes.prompt` - Przegląd wprowadzonych zmian### 4. Tech Lead (`tech_lead.py`)
**Rola:** Kierownik techniczny projektu  
**Odpowiedzialności:**
- Planowanie zadań i epików
- Zarządzanie przepływem pracy
- Podział funkcjonalności na zadania
- Koordynacja pracy innych agentów

**Kluczowe prompty:**
- `system.prompt` - Definicja roli tech leada
- `epic_breakdown.prompt` - Podział epików na zadania
- `plan.prompt` - Tworzenie planów implementacji

### 5. Bug Hunter (`bug_hunter.py`)
**Rola:** Specjalista od znajdowania i naprawiania błędów  
**Odpowiedzialności:**
- Analiza błędów w kodzie
- Debugowanie aplikacji
- Tworzenie raportów o błędach
- Sugerowanie poprawek

**Kluczowe prompty:**
- `system.prompt` - Definicja roli bug huntera
- `bug_found_or_add_logs.prompt` - Analiza znalezionych błędów
- `ask_a_question.prompt` - Zadawanie pytań o błędy

### 6. Troubleshooter (`troubleshooter.py`)
**Rola:** Rozwiązywacz problemów technicznych  
**Odpowiedzialności:**
- Diagnozowanie problemów systemowych
- Rozwiązywanie błędów konfiguracji
- Naprawianie problemów z zależnościami
- Optymalizacja wydajności

**Kluczowe prompty:**
- `system.prompt` - Definicja roli troubleshootera
- `bug_report.prompt` - Tworzenie raportów o problemach
- `iteration.prompt` - Iteracyjne rozwiązywanie problemów

### 7. Orchestrator (`orchestrator.py`)
**Rola:** Koordynator wszystkich agentów  
**Odpowiedzialności:**
- Zarządzanie przepływem pracy
- Decydowanie o kolejności działań
- Koordynacja komunikacji między agentami
- Monitorowanie postępu projektu

## 🔄 Współpraca agentów

### Typowy przepływ pracy:
1. **Orchestrator** inicjuje projekt
2. **Architect** analizuje wymagania i wybiera technologie
3. **Tech Lead** tworzy plan implementacji
4. **Developer** implementuje główne funkcjonalności z możliwością:
   - Interwencji użytkownika w kluczowych momentach
   - Weryfikacji każdego kroku implementacji
   - Iteracyjnego ulepszania kodu
5. **Code Monkey** wykonuje szczegółowe zmiany
6. **Bug Hunter** testuje i znajduje błędy
7. **Troubleshooter** rozwiązuje problemy techniczne
8. **Debugger** (zintegrowany) - diagnostyka i rozwiązywanie błędów w czasie rzeczywistym

### Komunikacja między agentami:
- Każdy agent może przekazać kontrolę innemu agentowi
- Stan projektu jest współdzielony przez bazę danych
- Orchestrator monitoruje i koordynuje działania

## 🛠️ Implementacja bazowa

Wszyscy agenci dziedziczą z klasy `BaseAgent`:

```python
class BaseAgent:
    def __init__(self, project):
        self.project = project
        self.llm = self.get_llm_client()
    
    def execute(self, task):
        # Główna logika agenta
        pass
    
    def get_llm_response(self, prompt_template, **kwargs):
        # Komunikacja z LLM
        pass
```

## 📝 Dodawanie nowego agenta

Aby dodać nowego agenta:
1. Utwórz nowy plik w `core/agents/`
2. Dziedzicz z `BaseAgent`
3. Zaimplementuj metodę `execute()`
4. Dodaj prompty w `core/prompts/[nazwa_agenta]/`
5. Zarejestruj agenta w orchestratorze

## 🎯 Specjalizacja agentów

Każdy agent ma swoją specjalizację:
- **Frontend** - Specjalista od interfejsu użytkownika
- **External Docs** - Integracja z zewnętrzną dokumentacją
- **Importer** - Import istniejących projektów
- **Spec Writer** - Tworzenie specyfikacji projektów

## 📊 Metryki i monitoring

Każdy agent loguje swoje działania:
- Czas wykonania zadań
- Liczba wywołań LLM
- Sukces/porażka operacji
- Błędy i ostrzeżenia