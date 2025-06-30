# 🤖 API dla gemini-cli

## Przegląd

Minimalny broker IPC dla komunikacji między GPT-Pilot a gemini-cli.

- **TCP Server** (port 8125) - dla GPT-Pilot
- **HTTP API** (port 8126) - dla gemini-cli

## Uruchomienie

```bash
# Zainstaluj zależności
pip install fastapi uvicorn

# Uruchom broker
python core/ui/run_broker.py
```

## API Endpointy

### 📊 Status brokera
```bash
GET /api/status
```

**Odpowiedź:**
```json
{
  "status": "running",
  "gpt_pilot_connected": true,
  "pending_questions": 2,
  "current_question": "abc123",
  "stats": {
    "messages_received": 45,
    "messages_sent": 23,
    "questions_processed": 15,
    "errors": 0,
    "uptime": 3600.5
  }
}
```

### ❓ Pobierz aktualne pytanie
```bash
GET /api/question
```

**Odpowiedź gdy jest pytanie (HTTP 200):**
```json
{
  "id": "abc123",
  "question": "What should be the project name?",
  "context": {
    "type": "user_input_request",
    "category": "agent:architect"
  },
  "timestamp": 1703123456.789,
  "age": 5.2
}
```

**Odpowiedź gdy brak pytań (HTTP 204):**
```
No Content
```

### ✅ Odpowiedz na pytanie
```bash
POST /api/answer
Content-Type: application/json

{
  "response": "MyAwesomeApp"
}
```

**Odpowiedź:**
```json
{
  "status": "answered",
  "response": "MyAwesomeApp", 
  "question_id": "abc123"
}
```

### 📋 Lista oczekujących pytań
```bash
GET /api/questions/pending
```

**Odpowiedź:**
```json
[
  {
    "id": "def456",
    "question": "What should this app do?",
    "timestamp": 1703123456.789,
    "age": 2.1
  }
]
```

## Workflow dla gemini-cli

### Polling loop
```bash
while true; do
  # Sprawdź czy jest pytanie
  question=$(curl -s http://localhost:8126/api/question)
  
  if [ $? -eq 0 ]; then
    # Przetwórz pytanie i wyślij odpowiedź
    answer="continue"  # Twoja logika AI
    curl -X POST http://localhost:8126/api/answer \
      -H "Content-Type: application/json" \
      -d "{\"response\": \"$answer\"}"
  fi
  
  sleep 1
done
```

### Event-driven approach
1. Monitoruj `/api/status` dla zmian w `current_question`
2. Gdy się zmieni, pobierz `/api/question`
3. Przetworz i wyślij `/api/answer`

## Kody błędów

- `200` - OK
- `204` - No Content (brak pytań)
- `404` - Not Found (brak aktualnego pytania dla /api/answer)
- `500` - Internal Server Error

## Przykłady curl

```bash
# Status
curl http://localhost:8126/api/status

# Pytanie
curl http://localhost:8126/api/question

# Odpowiedź
curl -X POST http://localhost:8126/api/answer \
  -H "Content-Type: application/json" \
  -d '{"response": "continue"}'

# Lista oczekujących
curl http://localhost:8126/api/questions/pending
```