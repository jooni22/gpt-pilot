#!/usr/bin/env python3
"""
Skrypt uruchamiający IPC Web Broker
"""

import sys
import os
import asyncio
import logging

# Dodaj główny katalog do ścieżki
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core.ui.ipc_web_broker import IPCWebBroker, BrokerConfig
from core.ui.websocket_ui import WebSocketUI, WebSocketUIConfig


async def main():
    """Uruchom oba serwery z lepszym logowaniem"""
    
    # Ustaw logowanie na INFO poziom
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("🚀 Starting GPT-Pilot WebSocket UI & IPC Broker...")
    print("=" * 60)
    
    # Konfiguracja dla WebSocket UI
    ws_config = WebSocketUIConfig(port=8127, host="localhost")
    ws_ui = WebSocketUI(ws_config)

    # Uruchomienie serwera WebSocket
    ws_started = await ws_ui.start()
    if not ws_started:
        print("❌ Failed to start WebSocket server!")
        return

    # Konfiguracja i uruchomienie brokera IPC z referencją do UI
    broker_config = BrokerConfig(log_level="INFO")
    broker = IPCWebBroker(config=broker_config, ui=ws_ui)

    print(f"🔌 GPT-Pilot TCP Server: localhost:8125")
    print(f"🤖 Gemini-CLI API: http://localhost:8126")
    print(f"🌐 WebSocket UI: ws://{ws_config.host}:{ws_config.port}")
    print("=" * 60)
    print("💡 Instructions:")
    print("   1. Open websocket_client.html in your browser")
    print("   2. Run: venv/bin/python3 main.py --local-ipc-port 8125")
    print("   3. Watch the logs below for detailed communication flow")
    print("=" * 60)

    try:
        # Uruchom broker w tle
        await broker.start()
    except KeyboardInterrupt:
        print("\n👋 Broker stopped by user")
        await ws_ui.stop()

if __name__ == '__main__':
    asyncio.run(main())
