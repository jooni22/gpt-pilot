#!/bin/bash

# Skrypt do debugowania GPT-Pilot z WebSocket UI

set -e

# Kolory do output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== GPT-Pilot WebSocket Debug Launcher ===${NC}"

# Sprawdź porty i zabij stare procesy
echo -e "${YELLOW}🧹 Czyszczenie starych procesów...${NC}"
pkill -f "litellm" 2>/dev/null || true
pkill -f "run_broker.py" 2>/dev/null || true  
pkill -f "websocket_ui.py" 2>/dev/null || true
pkill -f "main.py" 2>/dev/null || true
sleep 2

# Utwórz katalog logs
mkdir -p logs

# Funkcja do sprawdzania portów
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${RED}❌ Port $port jest zajęty${NC}"
        return 1
    else
        echo -e "${GREEN}✅ Port $port jest wolny${NC}"
        return 0
    fi
}

# Sprawdź wszystkie porty
echo -e "${YELLOW}🔍 Sprawdzanie portów...${NC}"
all_ports_free=true

for port in 8125 8126 8127 4000; do
    if ! check_port $port; then
        all_ports_free=false
    fi
done

if [ "$all_ports_free" = false ]; then
    echo -e "${RED}❌ Niektóre porty są zajęte. Zatrzymuję.${NC}"
    exit 1
fi

# Aktywuj venv jeśli istnieje
if [ -d "venv" ]; then
    echo -e "${YELLOW}🐍 Aktywuję virtualenv...${NC}"
    source venv/bin/activate
fi

# 1. Uruchom LiteLLM proxy
echo -e "${YELLOW}🚀 Uruchamiam LiteLLM proxy...${NC}"
litellm --config litellm_config.yaml > logs/litellm.log 2>&1 &
LITELLM_PID=$!
echo "LiteLLM PID: $LITELLM_PID"

# Czekaj aż LiteLLM się uruchomi
echo -e "${YELLOW}⏳ Czekam na LiteLLM (5s)...${NC}"
sleep 5

if ! check_port 4000; then
    echo -e "${RED}❌ LiteLLM nie uruchomił się na porcie 4000${NC}"
    kill $LITELLM_PID 2>/dev/null || true
    exit 1
fi
echo -e "${GREEN}✅ LiteLLM działa na porcie 4000${NC}"

# 2. Uruchom WebSocket UI i IPC Broker
echo -e "${YELLOW}🔗 Uruchamiam WebSocket UI i IPC Broker...${NC}"
python core/ui/run_broker.py > logs/broker.log 2>&1 &
BROKER_PID=$!
echo "Broker PID: $BROKER_PID"

# Czekaj na broker
echo -e "${YELLOW}⏳ Czekam na WebSocket UI i IPC Broker (5s)...${NC}"
sleep 5

# Sprawdź czy broker działa
broker_ok=true
for port in 8125 8126 8127; do
    if check_port $port; then
        echo -e "${RED}❌ Broker nie uruchomił się na porcie $port${NC}"
        broker_ok=false
    fi
done

if [ "$broker_ok" = false ]; then
    echo -e "${RED}❌ Broker nie uruchomił się poprawnie${NC}"
    kill $LITELLM_PID $BROKER_PID 2>/dev/null || true
    exit 1
fi

echo -e "${GREEN}✅ WebSocket UI działa na ws://localhost:8127${NC}"
echo -e "${GREEN}✅ IPC Broker działa na portach 8125, 8126${NC}"

# 3. Wyświetl logi brokera w czasie rzeczywistym
echo -e "${YELLOW}📋 Logi brokera (Ctrl+C aby przerwać):${NC}"
echo -e "${BLUE}===============================================${NC}"
tail -f logs/broker.log &
TAIL_PID=$!

# 4. Uruchom GPT-Pilot w osobnym terminalu
echo -e "${YELLOW}🎯 Teraz uruchom GPT-Pilot w drugim terminalu:${NC}"
echo -e "${GREEN}python main.py${NC}"
echo ""
echo -e "${YELLOW}🌐 Otwórz w przeglądarce:${NC}"
echo -e "${GREEN}file:///$(pwd)/websocket_client.html${NC}"
echo ""
echo -e "${YELLOW}📊 Status systemu:${NC}"
echo -e "${GREEN}• LiteLLM: http://localhost:4000${NC}"
echo -e "${GREEN}• WebSocket UI: ws://localhost:8127${NC}"  
echo -e "${GREEN}• IPC Broker API: http://localhost:8126/api/status${NC}"
echo ""
echo -e "${YELLOW}📝 Monitorowanie:${NC}"
echo -e "${GREEN}• Logi brokera: tail -f logs/broker.log${NC}"
echo -e "${GREEN}• Logi LiteLLM: tail -f logs/litellm.log${NC}"
echo ""
echo -e "${YELLOW}⏹️ Aby zatrzymać wszystko: Ctrl+C${NC}"

# Funkcja czyszczenia przy wyjściu
cleanup() {
    echo -e "\n${YELLOW}🧹 Zatrzymuję wszystkie procesy...${NC}"
    kill $TAIL_PID 2>/dev/null || true
    kill $BROKER_PID 2>/dev/null || true  
    kill $LITELLM_PID 2>/dev/null || true
    pkill -f "litellm" 2>/dev/null || true
    pkill -f "run_broker.py" 2>/dev/null || true
    echo -e "${GREEN}✅ Wszystko zatrzymane${NC}"
}

trap cleanup EXIT INT TERM

# Czekaj na zakończenie
wait $TAIL_PID