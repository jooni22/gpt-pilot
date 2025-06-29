# Często zadawane pytania (FAQ)

## 🤔 Ogólne pytania

### Czym jest GPT-Pilot?
GPT-Pilot to narzędzie do automatycznego generowania aplikacji przy użyciu sztucznej inteligencji. System wykorzystuje różne modele LLM do tworzenia kompletnych aplikacji na podstawie opisu w języku naturalnym.

### Jakie typy aplikacji można tworzyć?
- Aplikacje webowe (React, Vue, Angular)
- API i backendy (Node.js, Python, PHP)
- Aplikacje mobilne (React Native)
- Narzędzia CLI
- Mikrousługi

### Ile kosztuje używanie GPT-Pilot?
GPT-Pilot jest darmowy, ale musisz płacić za API modeli LLM:
- OpenAI GPT-4: ~$0.03-0.06 za 1000 tokenów
- Anthropic Claude: ~$0.015-0.075 za 1000 tokenów  
- Groq: Darmowy tier dostępny

## 🔧 Pytania techniczne

### Które modele LLM są najlepsze?
**Zalecane:**
1. **GPT-4** - Najlepsza jakość kodu, ale droższy
2. **Claude-3 Sonnet** - Dobra jakość, szybszy
3. **Llama 3.1 70B (Groq)** - Darmowy, dobra jakość

### Jak długo trwa generowanie aplikacji?
- Prosta aplikacja: 10-30 minut
- Średnia aplikacja: 30-90 minut
- Złożona aplikacja: 1-3 godziny

### Czy mogę używać własnego kodu?
Tak! GPT-Pilot może:
- Analizować istniejący kod
- Dodawać nowe funkcje
- Refaktoryzować kod
- Naprawiać błędy

### Jakie języki programowania są obsługiwane?
**Pełne wsparcie:**
- JavaScript/TypeScript
- Python
- Node.js

**Częściowe wsparcie:**
- PHP
- Java
- C#
- Go

## 🚀 Pytania o użytkowanie

### Jak napisać dobry opis aplikacji?
**Dobre praktyki:**
```
✅ Dobry opis:
"Aplikacja do zarządzania zadaniami z funkcjami:
- Dodawanie/edycja/usuwanie zadań
- Kategorie i tagi
- Terminy i przypomnienia
- Interfejs mobilny
- Synchronizacja w chmurze"

❌ Słaby opis:
"Zrób mi aplikację do zadań"
```

### Czy mogę zatrzymać i wznowić generowanie?
Tak! GPT-Pilot automatycznie zapisuje postęp. Możesz:
- Zatrzymać w dowolnym momencie (Ctrl+C)
- Wznowić później uruchamiając ponownie
- Przeglądać historię zmian

### Jak dodać nowe funkcje do istniejącej aplikacji?
```bash
# Uruchom GPT-Pilot w katalogu z aplikacją
cd my-existing-app
python /path/to/gpt-pilot/main.py

# Opisz nowe funkcje
"Dodaj system logowania użytkowników z rejestracją przez email"
```

## 🐛 Pytania o problemy

### Aplikacja nie działa po wygenerowaniu
**Sprawdź:**
1. Czy zainstalowano wszystkie zależności?
2. Czy porty nie są zajęte?
3. Czy baza danych jest skonfigurowana?
4. Czy zmienne środowiskowe są ustawione?

```bash
# Typowe kroki naprawcze
cd my-app
pnpm install
pnpm run dev
```

### Kod jest niskiej jakości
**Przyczyny i rozwiązania:**
- **Słaby opis** → Bądź bardziej szczegółowy
- **Słaby model** → Użyj GPT-4 zamiast GPT-3.5
- **Złożoność** → Podziel na mniejsze części

### GPT-Pilot "zawiesza się"
**Możliwe przyczyny:**
- Problemy z API (rate limiting)
- Zbyt długi prompt
- Problemy z siecią

**Rozwiązania:**
```bash
# Sprawdź logi
tail -f pythagora.log

# Restart z debugowaniem
python main.py --debug
```

## 💰 Pytania o koszty

### Ile będzie kosztować moja aplikacja?
**Szacunkowe koszty (GPT-4):**
- Prosta aplikacja: $5-15
- Średnia aplikacja: $15-50  
- Złożona aplikacja: $50-200

### Jak kontrolować koszty?
- Używaj GPT-3.5 do prostych zadań
- Sprawdzaj zużycie w dashboardzie OpenAI
- Ustaw limity wydatków
- Używaj Groq dla darmowych eksperymentów

## 🔒 Pytania o bezpieczeństwo

### Czy mój kod jest bezpieczny?
- Kod jest generowany lokalnie
- API wysyła tylko prompty, nie cały kod
- Możesz przejrzeć wszystkie żądania
- Nie przechowujemy Twojego kodu

### Czy mogę używać w projektach komercyjnych?
Tak! GPT-Pilot ma licencję MIT. Wygenerowany kod należy do Ciebie.

## 📈 Pytania o rozwój

### Jak mogę przyczynić się do projektu?
- Zgłaszaj błędy na GitHub
- Proponuj nowe funkcje
- Twórz pull requesty
- Dziel się przykładami

### Jakie są plany na przyszłość?
- Więcej szablonów projektów
- Wsparcie dla większej liczby języków
- Lepsze debugowanie
- Integracja z IDE
- Wsparcie dla aplikacji mobilnych

## 🎯 Najlepsze praktyki

### Jak uzyskać najlepsze rezultaty?
1. **Bądź konkretny** w opisie
2. **Używaj GPT-4** dla ważnych projektów
3. **Testuj często** podczas generowania
4. **Przeglądaj kod** przed użyciem w produkcji
5. **Dokumentuj zmiany** dla zespołu

### Kiedy NIE używać GPT-Pilot?
- Aplikacje wymagające wysokiego bezpieczeństwa
- Systemy czasu rzeczywistego
- Bardzo specjalistyczne domeny
- Gdy masz bardzo konkretne wymagania architektoniczne