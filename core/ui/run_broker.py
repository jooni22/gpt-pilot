#!/usr/bin/env python3
"""
Skrypt uruchamiający IPC Web Broker
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core.ui.ipc_web_broker import main as broker_main
from core.ui.websocket_ui import WebSocketUI, WebSocketUIConfig


async def main():
    """Uruchom oba serwery"""
    # Konfiguracja dla WebSocket UI
    ws_config = WebSocketUIConfig(port=8127, host="localhost")
    ws_ui = WebSocketUI(ws_config)

    # Uruchomienie serwera WebSocket
    ws_server_task = asyncio.create_task(ws_ui.start())

    # Uruchomienie brokera IPC
    broker_task = asyncio.create_task(broker_main())

    print("🚀 Starting IPC Web Broker and WebSocket UI...")
    print(f"🔌 GPT-Pilot TCP: localhost:8125")
    print(f"🤖 gemini-cli API: http://localhost:8126")
    print(f"🌐 WebSocket UI: ws://{ws_config.host}:{ws_config.port}")
    print("=" * 50)

    await asyncio.gather(ws_server_task, broker_task)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
