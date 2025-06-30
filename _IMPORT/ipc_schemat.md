Stworzymy centralny serwer-pośrednik (nazwijmy go ipc_web_broker.py), który będzie pełnił dwie role jednocześnie:


   1. Serwer TCP dla `gpt-pilot`: Będzie nasłuchiwał na połączenie od gpt-pilot (tak jak nasz poprzedni ipc_server.py), odbierał jego
      komunikaty i, co najważniejsze, wysyłał mu odpowiedzi.
   2. Serwer Web/WebSocket dla interfejsu: Będzie serwował prostą stronę HTML i utrzymywał połączenie WebSocket z przeglądarką, aby wysyłać
      jej aktualizacje statusu w czasie rzeczywistym.


  Oto jak wyglądałby przepływ danych:



    1 ┌──────────────────┐      TCP      ┌──────────────────────┐      HTTP/API      ┌──────────────────┐
    2 │                  │◄─────────────►│                      │◄───────────────────►│                  │
    3 │    gpt-pilot     │ (komunikaty) │  ipc_web_broker.py   │  (pytania/odpowiedzi) │   Agent (gemini-cli)     │
    4 │ (działa jako klient) │              │ (nasz nowy serwer)   │                    │                  │
    5 └──────────────────┘               └──────────┬───────────┘                    └──────────────────┘
    6                                               │
    7                                               │ WebSocket
    8                                               │ (status, logi)
    9                                               ▼
   10                                      ┌──────────────────┐
   11                                      │                  │
   12                                      │ Przeglądarka Web │
   13                                      │  (Interfejs UI)  │
   14                                      └──────────────────┘



  Jak to będzie działać w praktyce?

  Nasz ipc_web_broker.py będzie inteligentnym pośrednikiem:


   1. Gdy `gpt-pilot` wyśle komunikat o statusie (np. STREAM, PROGRESS, INFO):
       * Broker odbierze ten komunikat.
       * Prześle go natychmiast do wszystkich podłączonych klientów webowych przez WebSocket.
       * Klient webowy (przeglądarka) wyświetli ten status.


   2. Gdy `gpt-pilot` poprosi o dane wejściowe (komunikat USER_INPUT_REQUEST):
       * Broker odbierze pytanie.
       * Zamiast wysyłać je do przeglądarki, "zaparkuje" to pytanie, czekając na odpowiedź od agenta (czyli ode mnie).
       * Ja, jako agent, odpytam brokera (np. przez specjalny endpoint HTTP/API), aby pobrać oczekujące pytanie.
       * Po przetworzeniu pytania, wyślę odpowiedź z powrotem do brokera (przez inny endpoint HTTP/API).
       * Broker sformatuje moją odpowiedź w oczekiwany przez gpt-pilot format (RESPONSE) i odeśle ją przez połączenie TCP.
       * gpt-pilot otrzyma odpowiedź i będzie kontynuował pracę.

  Plan implementacji


  Aby to zrealizować, potrzebujemy:


   1. Wybrać technologię: Użyjemy FastAPI jako frameworka webowego, ponieważ doskonale integruje się z asyncio, co pozwoli nam łatwo zarządzać
      serwerem TCP i serwerem WebSocket w jednej aplikacji. Będziemy potrzebować uvicorn do jego uruchomienia.
   2. Stworzyć plik `ipc_web_broker.py`: Będzie zawierał logikę serwera TCP, endpointy WebSocket oraz endpointy HTTP/API dla mnie.
   3. Stworzyć prosty plik `index.html`: Będzie to nasz interfejs webowy, który połączy się z serwerem przez WebSocket i będzie wyświetlał
      otrzymywane dane.

