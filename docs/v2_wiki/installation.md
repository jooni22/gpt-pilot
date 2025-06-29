# Instalacja i konfiguracja GPT-Pilot

## 📋 Wymagania systemowe

### Minimalne wymagania
- **Python:** 3.8 lub nowszy
- **Node.js:** 16.0 lub nowszy (dla projektów JavaScript/TypeScript)
- **Git:** Najnowsza wersja
- **RAM:** Minimum 4GB, zalecane 8GB+
- **Dysk:** 2GB wolnego miejsca

### Zalecane wymagania
- **Python:** 3.10+
- **Node.js:** 18.0+
- **pnpm:** Zamiast npm (szybszy)
- **RAM:** 16GB+
- **SSD:** Dla lepszej wydajności

## 🔑 Klucze API

Potrzebujesz klucza API do jednego z obsługiwanych dostawców LLM:

### OpenAI (zalecany)
1. Idź na https://platform.openai.com/api-keys
2. Utwórz nowy klucz API
3. Skopiuj klucz (zaczyna się od `sk-`)

### Anthropic
1. Idź na https://console.anthropic.com/
2. Utwórz konto i klucz API
3. Skopiuj klucz (zaczyna się od `sk-ant-`)

### Groq (darmowy)
1. Idź na https://console.groq.com/
2. Utwórz konto
3. Wygeneruj klucz API

## 🚀 Instalacja krok po kroku

### 1. Klonowanie repozytorium
```bash
# HTTPS
git clone https://github.com/Pythagora-io/gpt-pilot.git

# SSH (jeśli masz skonfigurowany SSH)
git clone git@github.com:Pythagora-io/gpt-pilot.git

cd gpt-pilot
```

### 2. Tworzenie środowiska wirtualnego
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```### 3. Instalacja zależności Python
```bash
# Aktualizacja pip
pip install --upgrade pip

# Instalacja zależności
pip install -r requirements.txt

# Weryfikacja instalacji
python -c "import openai; print('OpenAI installed successfully')"
```

### 4. Instalacja Node.js i pnpm (opcjonalnie)
```bash
# Instalacja pnpm (zalecane zamiast npm)
npm install -g pnpm

# Weryfikacja
pnpm --version
node --version
```

## ⚙️ Konfiguracja

### 1. Plik konfiguracyjny
```bash
# Skopiuj przykładową konfigurację
cp example-config.json config.json
```

Edytuj `config.json`:
```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key": "your-api-key-here",
    "temperature": 0.7,
    "max_tokens": 4096
  },
  "database": {
    "url": "sqlite:///data/database/pythagora.db"
  },
  "workspace": {
    "path": "./workspace"
  },
  "logging": {
    "level": "INFO"
  }
}
```

### 2. Zmienne środowiskowe
Utwórz plik `.env` w katalogu głównym:
```bash
# .env
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
GROQ_API_KEY=your-groq-api-key

# Opcjonalne
DATABASE_URL=sqlite:///data/database/pythagora.db
WORKSPACE_PATH=./workspace
LOG_LEVEL=INFO
```

### 3. Konfiguracja dla różnych dostawców LLM

#### OpenAI
```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key": "sk-...",
    "temperature": 0.7,
    "max_tokens": 4096,
    "timeout": 60
  }
}
```

#### Anthropic
```json
{
  "llm": {
    "provider": "anthropic",
    "model": "claude-3-sonnet-20240229",
    "api_key": "sk-ant-...",
    "max_tokens": 4096
  }
}
```

#### Groq
```json
{
  "llm": {
    "provider": "groq",
    "model": "llama-3.1-70b-versatile",
    "api_key": "gsk_...",
    "temperature": 0.7
  }
}
```

#### Azure OpenAI
```json
{
  "llm": {
    "provider": "azure",
    "endpoint": "https://your-resource.openai.azure.com/",
    "api_key": "your-azure-key",
    "deployment_name": "gpt-4",
    "api_version": "2024-02-01"
  }
}
```

## 🗄️ Konfiguracja bazy danych

### SQLite (domyślnie)
```json
{
  "database": {
    "url": "sqlite:///data/database/pythagora.db"
  }
}
```

### PostgreSQL
```bash
# Instalacja dodatkowych zależności
pip install psycopg2-binary
```

```json
{
  "database": {
    "url": "postgresql://user:password@localhost:5432/gpt_pilot"
  }
}
```

### MySQL
```bash
# Instalacja dodatkowych zależności
pip install mysql-connector-python
```

```json
{
  "database": {
    "url": "mysql://user:password@localhost:3306/gpt_pilot"
  }
}
```

## 🔧 Inicjalizacja bazy danych

```bash
# Uruchomienie migracji
python -m alembic upgrade head

# Weryfikacja
python -c "from core.db.session import get_session; print('Database connected successfully')"
```

## ✅ Weryfikacja instalacji

### Test podstawowy
```bash
python main.py --help
```

### Test połączenia z LLM
```bash
python -c "
from core.llm.openai_client import OpenAIClient
from core.config.user_settings import get_config

config = get_config()
client = OpenAIClient(config['llm'])
response = client.send_request([{'role': 'user', 'content': 'Hello'}])
print('LLM connection successful:', response[:50])
"
```

### Test pełnej konfiguracji
```bash
# Uruchomienie w trybie testowym
python main.py --test-config
```

## 🐛 Rozwiązywanie problemów instalacji

### Problem: `pip install` kończy się błędem
```bash
# Rozwiązanie 1: Aktualizacja pip
pip install --upgrade pip setuptools wheel

# Rozwiązanie 2: Instalacja bez cache
pip install --no-cache-dir -r requirements.txt

# Rozwiązanie 3: Instalacja z verbose
pip install -v -r requirements.txt
```

### Problem: Błąd importu modułów
```bash
# Sprawdź czy środowisko wirtualne jest aktywne
which python  # Linux/Mac
where python  # Windows

# Reaktywacja środowiska
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Problem: Błąd połączenia z bazą danych
```bash
# Sprawdź czy katalog istnieje
mkdir -p data/database

# Uprawnienia (Linux/Mac)
chmod 755 data/database

# Test połączenia
python -c "
import sqlite3
conn = sqlite3.connect('data/database/test.db')
print('SQLite working')
conn.close()
"
```

### Problem: Błąd API key
```bash
# Sprawdź zmienne środowiskowe
echo $OPENAI_API_KEY  # Linux/Mac
echo %OPENAI_API_KEY% # Windows

# Test klucza API
python -c "
import openai
openai.api_key = 'your-key'
print('API key format correct')
"
```

## 🔄 Aktualizacja

### Aktualizacja kodu
```bash
git pull origin main
pip install -r requirements.txt
python -m alembic upgrade head
```

### Migracja konfiguracji
```bash
# Backup starej konfiguracji
cp config.json config.json.backup

# Porównaj z nowym przykładem
diff config.json example-config.json
```

## 🏃‍♂️ Pierwsze uruchomienie

```bash
# Aktywacja środowiska
source venv/bin/activate

# Uruchomienie
python main.py

# Pierwszy projekt
# Postępuj zgodnie z instrukcjami na ekranie
```

## 📝 Logowanie i debugowanie

### Włączenie szczegółowego logowania
```json
{
  "logging": {
    "level": "DEBUG",
    "file": "pythagora.log"
  }
}
```

### Monitorowanie logów
```bash
# Linux/Mac
tail -f pythagora.log

# Windows
Get-Content pythagora.log -Wait
```