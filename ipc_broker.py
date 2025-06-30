

import asyncio
import json
import logging
from asyncio import StreamReader, StreamWriter
from typing import Set

import websockets
from websockets.server import WebSocketServerProtocol

# --- Konfiguracja ---
LOG_FILE = "rozmowa.log"
GPT_PILOT_PORT = 8125
WEB_UI_PORT = 8765

# Komenda do uruchomienia Twojego agenta.
# Upewnij się, że jest poprawna i dostępna w Twoim środowisku.
# Możesz tu wstawić np. "gemini-cli --interactive" lub podobne.
AGENT_COMMAND = ["/usr/bin/python3", "-u", "-c", """
import sys
import time
print("Agent gemini-cli gotowy.", flush=True)
try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(f"Otrzymano: {line.strip()}", flush=True)
        time.sleep(2)
        print(f"Odpowiedź na '{line.strip()}'", flush=True)
except KeyboardInterrupt:
    pass
"""]


# --- Stan globalny serwera ---
web_clients: Set[WebSocketServerProtocol] = set()
conversation_history: list[str] = []
gpt_pilot_writer: StreamWriter | None = None
agent_process: asyncio.subprocess.Process | None = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def broadcast_to_web(message: str):
    """Wysyła wiadomość do wszystkich podłączonych klientów webowych."""
    if web_clients:
        # Kopiujemy zbiór, aby uniknąć problemów przy modyfikacji w trakcie iteracji
        await asyncio.gather(*[client.send(message) for client in list(web_clients)])

async def log_and_broadcast(source: str, content: str):
    """Zapisuje do pliku, dodaje do historii i rozgłasza wiadomość."""
    global conversation_history
    log_message = f"[{source}] {content}"
    logging.info(log_message)
    conversation_history.append(log_message)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_message + "\n")
    await broadcast_to_web(log_message)

async def handle_web_client(websocket: WebSocketServerProtocol, path: str):
    """Obsługuje połączenia od interfejsu webowego."""
    logging.info(f"Klient webowy dołączył: {websocket.remote_address}")
    web_clients.add(websocket)
    try:
        # Wyślij całą dotychczasową historię do nowego klienta
        if conversation_history:
            await websocket.send("\n".join(conversation_history))

        # Utrzymuj połączenie otwarte, aby nasłuchiwać na rozłączenie
        await websocket.wait_closed()
    finally:
        logging.info(f"Klient webowy rozłączył się: {websocket.remote_address}")
        web_clients.remove(websocket)

async def read_from_agent():
    """Czyta odpowiedzi od agenta (z jego stdout) i przekazuje dalej."""
    global gpt_pilot_writer
    while True:
        if agent_process and agent_process.stdout:
            try:
                response_bytes = await agent_process.stdout.readline()
                if not response_bytes:
                    await log_and_broadcast("BROKER", "Agent zakończył strumień stdout.")
                    break
                
                response = response_bytes.decode('utf-8').strip()
                await log_and_broadcast("AGENT", response)

                if gpt_pilot_writer:
                    # Przygotuj odpowiedź w formacie oczekiwanym przez IPCClientUI
                    response_payload = {
                        "type": "response",
                        "content": response
                    }
                    response_json = json.dumps(response_payload)
                    response_data = response_json.encode('utf-8')
                    
                    # Wyślij długość, a potem dane
                    gpt_pilot_writer.write(len(response_data).to_bytes(4, byteorder='big'))
                    gpt_pilot_writer.write(response_data)
                    await gpt_pilot_writer.drain()

            except Exception as e:
                await log_and_broadcast("BROKER_ERROR", f"Błąd przy czytaniu od agenta: {e}")
                break
        else:
            await asyncio.sleep(0.1)


async def handle_gpt_pilot(reader: StreamReader, writer: StreamWriter):
    """Obsługuje połączenie od aplikacji gpt-pilot."""
    global gpt_pilot_writer, agent_process
    gpt_pilot_writer = writer
    addr = writer.get_extra_info('peername')
    logging.info(f"Aplikacja gpt-pilot połączona z {addr}")

    try:
        while True:
            # IPCClientUI wysyła 4 bajty z długością wiadomości
            msg_length_bytes = await reader.readexactly(4)
            msg_length = int.from_bytes(msg_length_bytes, 'big')

            # Odczytaj właściwą wiadomość
            message_bytes = await reader.readexactly(msg_length)
            message_data = json.loads(message_bytes.decode('utf-8'))

            # Logujemy i rozgłaszamy KAŻDĄ wiadomość od aplikacji dla celów diagnostycznych
            msg_type = message_data.get('type')
            raw_content = message_data.get("content", "")
            # W wiadomościach typu 'buttons' treść jest połączona '/', zamieniamy na spacje dla czytelności
            display_content = raw_content.replace('/', ' / ') if isinstance(raw_content, str) else str(raw_content)
            await log_and_broadcast("APP", f"({msg_type}) {display_content}")

            # Do agenta wysyłamy TYLKO faktyczne prośby o input
            if msg_type == "user_input_request":
                question = message_data.get("content", "")
                if agent_process and agent_process.stdin:
                    agent_process.stdin.write(f"{question}\n".encode('utf-8'))
                    await agent_process.stdin.drain()
                else:
                    await log_and_broadcast("BROKER_ERROR", "Agent nie jest uruchomiony lub nie ma stdin.")

    except asyncio.IncompleteReadError:
        logging.info("Aplikacja gpt-pilot rozłączyła się.")
    except Exception as e:
        logging.error(f"Błąd w komunikacji z gpt-pilot: {e}")
    finally:
        gpt_pilot_writer = None


async def main():
    global agent_process
    
    # Wyczyść plik logu przy starcie
    with open(LOG_FILE, "w") as f:
        f.write("--- Sesja rozpoczęta ---\n")

    logging.info("Uruchamianie agenta jako podprocesu...")
    agent_process = await asyncio.create_subprocess_exec(
        *AGENT_COMMAND,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    logging.info(f"Agent uruchomiony z PID: {agent_process.pid}")

    # Uruchom zadanie w tle do czytania z agenta
    asyncio.create_task(read_from_agent())

    # Uruchom serwer TCP dla gpt-pilot
    gpt_pilot_server = await asyncio.start_server(
        handle_gpt_pilot, '127.0.0.1', GPT_PILOT_PORT)

    # Uruchom serwer WebSocket dla UI
    web_ui_server = await websockets.serve(handle_web_client, "127.0.0.1", WEB_UI_PORT)

    logging.info(f"Serwer dla gpt-pilot nasłuchuje na porcie {GPT_PILOT_PORT}")
    logging.info(f"Serwer dla Web UI nasłuchuje na porcie {WEB_UI_PORT}")
    logging.info("Broker jest gotowy. Czekam na połączenia...")

    await gpt_pilot_server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Zamykanie brokera...")

