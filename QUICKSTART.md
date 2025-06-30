# 🚀 GPT-Pilot QuickStart z WebSocket UI

Kompletny przewodnik uruchamiania GPT-Pilot z nowoczesnym interfejsem webowym.

## 📋 Wymagania

- Python 3.8+
- Node.js (dla LiteLLM)
- Konfiguracja API kluczy w `litellm_config.yaml`

## ⚡ Szybkie uruchomienie

### 1. Przygotowanie środowiska (jednorazowo)
```bash
# Zainstaluj Python dependencies
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub: venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Zainstaluj LiteLLM
pip install litellm

# Ustaw uprawnienia dla skryptów
chmod +x run.sh monitor.sh
```

### 2. Uruchomienie kompletnego systemu
```bash
# Uruchom wszystkie komponenty automatycznie
./run.sh
```

Skrypt automatycznie:
- ✅ Sprawdzi dostępność portów
- 🚀 Uruchomi LiteLLM proxy (port 4000)
- 🌐 Uruchomi WebSocket UI & IPC Broker (porty 8125-8127)
- 📱 Wyświetli linki do interfejsów
- 🎯 Poczeka na połączenie klienta WebSocket
- 🤖 Uruchomi główny proces GPT-Pilot

### 3. Korzystanie z interfejsu webowego

Po uruchomieniu `./run.sh`:

1. **Otwórz interfejs w przeglądarce:**
   ```
   file:///path/to/gpt-pilot/websocket_client.html
   ```

2. **Sprawdź połączenie** - powinien pojawić się zielony wskaźnik "Połączono"

3. **Naciśnij dowolny klawisz** w terminalu aby kontynuować

4. **Korzystaj z GPT-Pilot** przez elegancki interfejs webowy!

## 🔧 Monitorowanie i debugowanie

### Monitor systemu
```bash
# Sprawdź status wszystkich komponentów
./monitor.sh
```

### Ręczne sprawdzanie statusu
```bash
# Status API
curl localhost:8126/api/status

# Sprawdź porty
lsof -i :8125  # IPC Server
lsof -i :8126  # Broker API  
lsof -i :8127  # WebSocket UI
lsof -i :4000  # LiteLLM

# Logi w czasie rzeczywistym
tail -f logs/broker.log    # Broker + WebSocket UI
tail -f logs/litellm.log   # LiteLLM proxy
```

### Zatrzymanie systemu
```bash
# Zatrzymaj przez Ctrl+C w głównym terminalu
# LUB użyj monitora:
./monitor.sh  # wybierz opcję 5
```

## 🎯 Interfejsy dostępne

| Komponent | URL | Opis |
|-----------|-----|------|
| **WebSocket UI** | `file://...websocket_client.html` | Główny interfejs użytkownika |
| **Broker API** | `http://localhost:8126/api/status` | Status API brokera |
| **LiteLLM** | `http://localhost:4000` | Proxy dla modeli AI |

## 📁 Struktura plików

```
gpt-pilot/
├── run.sh              # 🚀 Główny launcher
├── monitor.sh          # 🔍 Monitor systemu
├── websocket_client.html # 🌐 Interfejs webowy
├── logs/               # 📋 Logi systemowe
│   ├── broker.log      # WebSocket UI + IPC Broker
│   └── litellm.log     # LiteLLM proxy
└── core/ui/
    ├── websocket_ui.py     # WebSocket UI implementation
    ├── ipc_web_broker.py   # IPC Broker
    └── run_broker.py       # Launcher dla UI+Broker
```

## 🐛 Rozwiązywanie problemów

### Port zajęty
```bash
# Sprawdź co używa portu
sudo lsof -i :PORT_NUMBER

# Zabij proces
sudo kill -9 PID
```

### WebSocket nie łączy się
1. Sprawdź czy broker działa: `curl localhost:8126/api/status`
2. Sprawdź logi: `tail -f logs/broker.log`
3. Odśwież stronę w przeglądarce

### LiteLLM błędy
1. Sprawdź konfigurację w `litellm_config.yaml`
2. Sprawdź logi: `tail -f logs/litellm.log`
3. Sprawdź API klucze

### GPT-Pilot błędy
1. Sprawdź czy venv jest aktywowany
2. Sprawdź połączenie IPC: `telnet localhost 8125`
3. Sprawdź logi brokera

## 🎉 Gotowe!

Po uruchomieniu `./run.sh` możesz korzystać z GPT-Pilot przez elegancki interfejs webowy z:
- 💬 Interaktywnymi pytaniami i buttonami
- 📊 Statusem projektu w czasie rzeczywistym  
- 📈 Statystykami konwersacji
- 🎨 Nowoczesnym, responsywnym designem

Miłego kodowania z GPT-Pilot! 🤖✨ 