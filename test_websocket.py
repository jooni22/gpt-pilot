#!/usr/bin/env python3
"""
Test WebSocket - Symuluje kliknięcie przycisku "node"
"""

import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8127"
    
    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Połączono z WebSocket")
            
            # Wyślij odpowiedź na pytanie
            response = {
                "type": "user_response", 
                "content": {
                    "button": "node"
                }
            }
            
            print(f"📤 Wysyłam odpowiedź: {response}")
            await websocket.send(json.dumps(response))
            print("✅ Odpowiedź wysłana!")
            
            # Czekaj na ewentualne kolejne pytania
            try:
                for i in range(10):
                    message = await asyncio.wait_for(websocket.recv(), timeout=2.0)
                    data = json.loads(message)
                    print(f"📨 Otrzymano: {data.get('type', 'unknown')} - {str(data.get('content', ''))[:100]}")
                    
                    if data.get('type') == 'question_request':
                        print("❓ Nowe pytanie otrzymane!")
                        break
                        
            except asyncio.TimeoutError:
                print("⏰ Timeout - brak kolejnych wiadomości")
                
    except Exception as e:
        print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())