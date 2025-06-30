#!/bin/bash

# GPT-Pilot Monitor Script
# Monitoruje logi i status wszystkich komponentów

# Kolory
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

log() {
    echo -e "${GREEN}[$(date '+%H:%M:%S')]${NC} $1"
}

# Banner
echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    🔍 GPT-PILOT MONITOR                      ║"
echo "║                  System Status & Log Viewer                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Sprawdź status portów
check_status() {
    local port=$1
    local name=$2
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "   ✅ ${GREEN}$name${NC} - Port $port: RUNNING"
    else
        echo -e "   ❌ ${RED}$name${NC} - Port $port: NOT RUNNING"
    fi
}

log "📊 System Status:"
check_status 4000 "LiteLLM Proxy   "
check_status 8125 "IPC Server      "
check_status 8126 "Broker API      "
check_status 8127 "WebSocket UI    "

echo ""
log "📁 Available Logs:"
if [ -d "logs" ]; then
    ls -la logs/ 2>/dev/null || echo "   No log files found"
else
    echo "   logs/ directory doesn't exist"
fi

echo ""
log "🔧 Available Commands:"
echo "   1. tail -f logs/broker.log    - Monitor broker logs"
echo "   2. tail -f logs/litellm.log   - Monitor LiteLLM logs"
echo "   3. curl localhost:8126/api/status - Check broker API status"
echo "   4. ps aux | grep python       - Show running Python processes"

echo ""
echo -e "${YELLOW}What would you like to monitor?${NC}"
echo "1) Broker logs (real-time)"
echo "2) LiteLLM logs (real-time)"
echo "3) All logs (combined)"
echo "4) System status (refresh)"
echo "5) Kill all GPT-Pilot processes"
echo "q) Quit"

read -p "Choice [1-5/q]: " choice

case $choice in
    1)
        log "📋 Showing broker logs (Ctrl+C to exit)..."
        sleep 1
        tail -f logs/broker.log 2>/dev/null || echo "Broker log file not found"
        ;;
    2)
        log "📋 Showing LiteLLM logs (Ctrl+C to exit)..."
        sleep 1
        tail -f logs/litellm.log 2>/dev/null || echo "LiteLLM log file not found"
        ;;
    3)
        log "📋 Showing all logs combined (Ctrl+C to exit)..."
        sleep 1
        tail -f logs/*.log 2>/dev/null || echo "No log files found"
        ;;
    4)
        log "🔄 Refreshing status..."
        exec $0
        ;;
    5)
        log "🛑 Killing all GPT-Pilot processes..."
        pkill -f "litellm" 2>/dev/null || true
        pkill -f "run_broker.py" 2>/dev/null || true
        pkill -f "main.py.*ipc-port" 2>/dev/null || true
        log "✅ Processes killed"
        ;;
    q|Q)
        log "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac 