#!/bin/bash

# GPT-Pilot Complete Launcher
# Uruchamia wszystkie komponenty systemu GPT-Pilot

set -e  # Zatrzymaj skrypt przy błędzie

# Kolory dla logów
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Funkcja do logowania
log() {
    echo -e "${GREEN}[$(date '+%H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Funkcja do czyszczenia procesów przy wyjściu
cleanup() {
    log "🧹 Cleaning up processes..."
    
    # Zabij wszystkie procesy potomne
    jobs -p | xargs -r kill 2>/dev/null || true
    
    # Poczekaj chwilę na zakończenie procesów
    sleep 2
    
    # Wymuś zabicie jeśli nadal działają
    jobs -p | xargs -r kill -9 2>/dev/null || true
    
    log "✅ Cleanup completed"
    exit 0
}

# Ustaw trap na sygnały wyjścia
trap cleanup SIGINT SIGTERM EXIT

# Sprawdź czy porty są wolne
check_port() {
    local port=$1
    local name=$2
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        error "Port $port jest już zajęty! ($name)"
        error "Uruchom: sudo lsof -i :$port aby zobaczyć co używa tego portu"
        exit 1
    fi
}

# Banner
echo -e "${PURPLE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                        🤖 GPT-PILOT                          ║"
echo "║                   Complete System Launcher                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Sprawdź wymagane porty
log "🔍 Checking required ports..."
check_port 8125 "GPT-Pilot IPC"
check_port 8126 "Broker API"
check_port 8127 "WebSocket UI"
check_port 4000 "LiteLLM"

# Sprawdź czy venv istnieje
if [ ! -d "venv" ]; then
    error "Virtual environment nie istnieje! Uruchom najpierw: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Sprawdź czy wymagane pliki istnieją
required_files=("litellm_config.yaml" "core/ui/run_broker.py" "main.py" "websocket_client.html")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        error "Required file missing: $file"
        exit 1
    fi
done

# Stwórz katalog na logi jeśli nie istnieje
mkdir -p logs

log "🚀 Starting GPT-Pilot components..."

# 1. Uruchom LiteLLM w tle
log "📡 Starting LiteLLM proxy server..."
litellm --config litellm_config.yaml --port 4000 > logs/litellm.log 2>&1 &
LITELLM_PID=$!
sleep 3

# Sprawdź czy LiteLLM się uruchomił
if ! kill -0 $LITELLM_PID 2>/dev/null; then
    error "LiteLLM failed to start. Check logs/litellm.log"
    exit 1
fi
log "✅ LiteLLM started (PID: $LITELLM_PID)"

# 2. Uruchom WebSocket UI & IPC Broker
log "🌐 Starting WebSocket UI & IPC Broker..."
python core/ui/run_broker.py > logs/broker.log 2>&1 &
BROKER_PID=$!
sleep 5

# Sprawdź czy broker się uruchomił
if ! kill -0 $BROKER_PID 2>/dev/null; then
    error "Broker failed to start. Check logs/broker.log"
    exit 1
fi
log "✅ WebSocket UI & IPC Broker started (PID: $BROKER_PID)"

# 3. Wyświetl informacje o dostępnych interfejsach
echo ""
echo -e "${CYAN}🎯 Interfaces Available:${NC}"
echo -e "   🌐 ${BLUE}WebSocket UI:${NC} file://$(pwd)/websocket_client.html"
echo -e "   📊 ${BLUE}Broker API:${NC}  http://localhost:8126/api/status"
echo -e "   🤖 ${BLUE}LiteLLM:${NC}     http://localhost:4000"
echo ""

# 4. Poczekaj na połączenie WebSocket klienta
log "⏳ Waiting for WebSocket client connection..."
echo -e "${YELLOW}Please open the WebSocket client in your browser:${NC}"
echo -e "${BLUE}file://$(pwd)/websocket_client.html${NC}"
echo ""
echo -e "${YELLOW}Press any key when the browser client is connected...${NC}"
read -n 1 -s
log "✅ Proceeding with GPT-Pilot startup"

# 5. Uruchom GPT-Pilot (główny proces - w foreground)
echo ""
log "🚀 Starting GPT-Pilot main process..."
echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}                     GPT-Pilot Interactive Mode                      ${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════════${NC}"
echo ""

# Uruchom GPT-Pilot w trybie interaktywnym
venv/bin/python3 main.py --local-ipc-port 8125

# Jeśli dojdziemy tutaj, GPT-Pilot się zakończył
log "GPT-Pilot main process finished"

