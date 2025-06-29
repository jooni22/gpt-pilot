# Szybki start z GPT-Pilot

## 🚀 Instalacja

### Wymagania systemowe
- Python 3.8+
- Node.js 16+ (dla projektów JavaScript/TypeScript)
- Git
- Klucz API do jednego z obsługiwanych LLM

### 1. Klonowanie repozytorium
```bash
git clone https://github.com/Pythagora-io/gpt-pilot.git
cd gpt-pilot
```

### 2. Instalacja zależności Python
```bash
# Tworzenie środowiska wirtualnego
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate     # Windows

# Instalacja zależności
pip install -r requirements.txt
```

### 3. Konfiguracja
Skopiuj i edytuj plik konfiguracyjny:
```bash
cp example-config.json config.json
```

Edytuj `config.json`:
```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key": "your-api-key-here"
  }
}
```

### 4. Konfiguracja zmiennych środowiskowych
```bash
# Dodaj do ~/.bashrc lub ~/.zshrc
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"  # opcjonalnie
```

## 🎯 Pierwszy projekt

### Uruchomienie GPT-Pilot
```bash
python main.py
```

### Proces tworzenia projektu
1. **Opis projektu** - Opisz swoją aplikację w języku naturalnym
2. **Wybór technologii** - GPT-Pilot zaproponuje odpowiedni stos technologiczny
3. **Potwierdzenie** - Przejrzyj i zatwierdź plan
4. **Generowanie** - Obserwuj jak AI tworzy Twoją aplikację

### Przykład opisu projektu
```
Chcę stworzyć aplikację do zarządzania zadaniami (todo app) z następującymi funkcjami:
- Dodawanie, edycja i usuwanie zadań
- Oznaczanie zadań jako wykonane
- Filtrowanie zadań (wszystkie, aktywne, zakończone)
- Prosty i nowoczesny interfejs użytkownika
- Zapisywanie danych lokalnie
```## 📁 Struktura wygenerowanego projektu

Po zakończeniu generowania otrzymasz strukturę podobną do:
```
my-todo-app/
├── client/                 # Frontend React
│   ├── src/
│   │   ├── components/     # Komponenty React
│   │   ├── pages/         # Strony aplikacji
│   │   ├── hooks/         # Custom hooks
│   │   └── lib/           # Utilities
│   ├── public/
│   └── package.json
├── server/                # Backend Node.js
│   ├── routes/            # API endpoints
│   ├── models/            # Modele danych
│   ├── services/          # Logika biznesowa
│   └── package.json
└── README.md              # Instrukcje uruchomienia
```

## 🏃‍♂️ Uruchomienie projektu

### 1. Instalacja zależności
```bash
cd my-todo-app

# Instalacja zależności serwera
cd server
pnpm install

# Instalacja zależności klienta
cd ../client
pnpm install
```

### 2. Uruchomienie w trybie deweloperskim
```bash
# Terminal 1 - Backend
cd server
pnpm run dev

# Terminal 2 - Frontend
cd client
pnpm run dev
```

### 3. Otwórz aplikację
- Frontend: http://localhost:5173
- Backend API: http://localhost:3000

## 🔧 Podstawowe komendy

### Zarządzanie projektem GPT-Pilot
```bash
# Uruchomienie GPT-Pilot
python main.py

# Uruchomienie z konkretną konfiguracją
python main.py --config custom-config.json

# Tryb interaktywny
python main.py --interactive

# Pomoc
python main.py --help
```

### Zarządzanie bazą danych
```bash
# Migracje bazy danych
python -m alembic upgrade head

# Tworzenie nowej migracji
python -m alembic revision --autogenerate -m "opis_zmiany"
```

## 🎨 Dostosowywanie

### Zmiana modelu LLM
Edytuj `config.json`:
```json
{
  "llm": {
    "provider": "anthropic",
    "model": "claude-3-sonnet-20240229",
    "api_key": "your-anthropic-key"
  }
}
```

### Zmiana szablonu projektu
Podczas tworzenia projektu możesz wybrać różne szablony:
- Vite + React + TypeScript (zalecany)
- React + Express
- Node.js + Express + MongoDB
- Vanilla JavaScript + React

## 🐛 Rozwiązywanie problemów

### Typowe problemy i rozwiązania

**Problem:** `ModuleNotFoundError: No module named 'openai'`
```bash
# Rozwiązanie: Zainstaluj zależności
pip install -r requirements.txt
```

**Problem:** `API key not found`
```bash
# Rozwiązanie: Ustaw zmienną środowiskową
export OPENAI_API_KEY="your-api-key"
```

**Problem:** Port już zajęty
```bash
# Rozwiązanie: Zmień port w konfiguracji
# client/vite.config.ts
server: {
  port: 5174  // Zmień na inny port
}
```

**Problem:** Błąd instalacji zależności
```bash
# Rozwiązanie: Wyczyść cache i zainstaluj ponownie
rm -rf node_modules package-lock.json
pnpm install
```

## 📚 Następne kroki

Po utworzeniu pierwszego projektu:

1. **Przeczytaj [Architekturę](architecture.md)** - Zrozum jak działa GPT-Pilot
2. **Sprawdź [System agentów](agents.md)** - Poznaj różne typy agentów
3. **Zobacz [Szablony projektów](project-templates.md)** - Dowiedz się o dostępnych szablonach
4. **Przejrzyj [Integrację LLM](llm-integration.md)** - Konfiguracja różnych modeli AI

## 💡 Wskazówki

- **Bądź precyzyjny w opisie** - Im bardziej szczegółowy opis, tym lepsza aplikacja
- **Używaj GPT-4** - Daje najlepsze rezultaty (choć jest droższy)
- **Monitoruj koszty** - Sprawdzaj zużycie API w dashboardzie dostawcy
- **Zapisuj postęp** - GPT-Pilot automatycznie zapisuje stan projektu
- **Testuj często** - Uruchamiaj aplikację podczas rozwoju

## 🎯 Przykłady projektów do wypróbowania

### Prosty blog
```
Aplikacja blog z możliwością dodawania postów, komentarzy i tagów. 
Interfejs administratora do zarządzania treścią.
```

### E-commerce
```
Sklep internetowy z katalogiem produktów, koszykiem, 
płatnościami i panelem administracyjnym.
```

### Chat aplikacja
```
Aplikacja do czatowania w czasie rzeczywistym z pokojami, 
prywatnym wiadomościami i powiadomieniami.
```