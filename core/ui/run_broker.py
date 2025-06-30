#!/usr/bin/env python3
"""
Skrypt uruchamiający IPC Web Broker
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core.ui.ipc_web_broker import main

if __name__ == '__main__':
    import asyncio
    print("🚀 Starting IPC Web Broker...")
    print("🔌 GPT-Pilot TCP: localhost:8125")
    print("🤖 gemini-cli API: http://localhost:8126")
    print("=" * 50)
    asyncio.run(main())