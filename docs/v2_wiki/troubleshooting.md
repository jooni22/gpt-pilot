# Rozwiązywanie problemów

## 🚨 Najczęstsze problemy

### 1. Problemy z API
#### Problem: "API key not found" lub "Invalid API key"
**Przyczyny:**
- Brak ustawionego klucza API
- Nieprawidłowy format klucza
- Klucz wygasł lub został odwołany

**Rozwiązania:**
```bash
# Sprawdź zmienne środowiskowe
echo $OPENAI_API_KEY

# Ustaw klucz w pliku konfiguracyjnym
{
  "llm": {
    "api_key": "sk-your-actual-key-here"
  }
}

# Test klucza
python -c "
from core.llm.openai_client import OpenAIClient
client = OpenAIClient({'api_key': 'your-key'})
print('Key valid')
"
```

#### Problem: "Rate limit exceeded"
**Przyczyny:**
- Zbyt wiele żądań w krótkim czasie
- Przekroczenie limitów API

**Rozwiązania:**
- Poczekaj kilka minut
- Sprawdź limity w dashboardzie dostawcy API
- Zmień model na mniej popularny (np. GPT-3.5 zamiast GPT-4)

### 2. Problemy z instalacją
#### Problem: "ModuleNotFoundError"
```bash
# Sprawdź czy środowisko wirtualne jest aktywne
which python

# Reinstalacja zależności
pip install -r requirements.txt --force-reinstall

# Sprawdź wersję Python
python --version  # Musi być 3.8+
```

#### Problem: Błędy kompilacji podczas instalacji
```bash
# Linux: Zainstaluj narzędzia deweloperskie
sudo apt-get install build-essential python3-dev

# Mac: Zainstaluj Xcode command line tools
xcode-select --install

# Windows: Zainstaluj Visual Studio Build Tools
```

### 3. Problemy z bazą danych
#### Problem: "Database locked" (SQLite)
```bash
# Sprawdź procesy blokujące bazę
lsof data/database/pythagora.db

# Usuń lock file jeśli istnieje
rm data/database/pythagora.db-lock

# Restart aplikacji
```

#### Problem: Błędy migracji
```bash
# Sprawdź aktualną wersję
python -m alembic current

# Wymuś migrację
python -m alembic upgrade head --sql

# W ostateczności - reset bazy (UWAGA: usuwa dane!)
rm data/database/pythagora.db
python -m alembic upgrade head
```