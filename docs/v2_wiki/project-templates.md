# System szablonów projektów

## 📋 Przegląd systemu szablonów

GPT-Pilot używa systemu szablonów do szybkiego generowania struktur projektów dla różnych technologii. Każdy szablon zawiera gotową strukturę plików, konfigurację i podstawową implementację.

## 🎯 Dostępne szablony

### 1. Vite + React + TypeScript (`vite_react.py`)
**Technologie:**
- Frontend: React 18 + TypeScript
- Build tool: Vite
- Styling: Tailwind CSS + shadcn/ui
- Backend: Node.js + Express
- Database: SQLite/MongoDB

**Struktura:**
```
project/
├── client/          # Frontend React
│   ├── src/
│   ├── public/
│   └── package.json
├── server/          # Backend Node.js
│   ├── routes/
│   ├── models/
│   └── package.json
└── package.json     # Root package.json
```

### 2. React + Express (`react_express.py`)
**Technologie:**
- Frontend: React + JavaScript
- Backend: Express.js
- Database: Prisma ORM
- Styling: Tailwind CSS
- Auth: JWT

**Struktura:**
```
project/
├── ui/              # Frontend React
├── api/             # Backend Express
├── prisma/          # Database schema
└── package.json
```

### 3. Node.js + Express + MongoDB (`node_express_mongoose.py`)
**Technologie:**
- Backend: Node.js + Express
- Database: MongoDB + Mongoose
- View Engine: EJS
- Authentication: Session-based

**Struktura:**
```
project/
├── models/          # Mongoose models
├── routes/          # Express routes
├── views/           # EJS templates
├── public/          # Static files
└── server.js
```### 4. JavaScript + React (`javascript_react.py`)
**Technologie:**
- Frontend: React + JavaScript (bez TypeScript)
- Build tool: Vite
- Styling: CSS Modules

**Struktura:**
```
project/
├── src/
│   ├── components/
│   ├── assets/
│   └── App.jsx
├── public/
└── package.json
```

## 🏗️ Architektura systemu szablonów

### Klasa bazowa (`base.py`)
Wszystkie szablony dziedziczą z `BaseTemplate`:

```python
class BaseTemplate:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.technologies = []
    
    def get_tree_structure(self):
        """Zwraca strukturę plików szablonu"""
        pass
    
    def get_summary(self):
        """Zwraca podsumowanie szablonu"""
        pass
```

### Rejestr szablonów (`registry.py`)
Centralny rejestr wszystkich dostępnych szablonów:

```python
TEMPLATES = {
    "vite_react": ViteReactTemplate,
    "react_express": ReactExpressTemplate,
    "node_express_mongoose": NodeExpressMongooseTemplate,
    "javascript_react": JavaScriptReactTemplate
}
```

### Renderowanie szablonów (`render.py`)
System renderowania szablonów z dynamicznymi danymi:
- Zastępowanie placeholderów
- Generowanie plików konfiguracyjnych
- Dostosowywanie do wymagań projektu

## 📁 Struktura szablonów

### Katalog `tree/`
Zawiera fizyczne pliki każdego szablonu:
```
core/templates/tree/
├── vite_react/
│   ├── client/
│   ├── server/
│   └── package.json
├── react_express/
├── node_express_mongoose/
└── javascript_react/
```

### Katalog `info/`
Zawiera pliki podsumowania dla każdego szablonu:
```
core/templates/info/
├── vite_react/
│   └── summary.tpl
├── react_express/
│   └── summary.tpl
└── ...
```

## 🎨 Komponenty UI

### shadcn/ui Components
Szablony React zawierają gotowe komponenty UI:
- **Formularze:** Input, Button, Label, Form
- **Nawigacja:** Navigation Menu, Breadcrumb
- **Feedback:** Alert, Toast, Dialog
- **Layout:** Card, Sheet, Separator
- **Data Display:** Table, Badge, Avatar

### Przykład komponentu:
```tsx
// components/ui/button.tsx
export const Button = ({ children, variant, ...props }) => {
  return (
    <button 
      className={cn(buttonVariants({ variant }))}
      {...props}
    >
      {children}
    </button>
  )
}
```

## ⚙️ Konfiguracja szablonów

### Package.json templates
Każdy szablon ma swój `package.json` z odpowiednimi zależnościami:

```json
{
  "name": "{{project_name}}",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

### Konfiguracja narzędzi
- **Vite:** `vite.config.js/ts`
- **TypeScript:** `tsconfig.json`
- **Tailwind:** `tailwind.config.js`
- **ESLint:** `eslint.config.js`

## 🚀 Proces generowania projektu

1. **Wybór szablonu** - Architect wybiera odpowiedni szablon
2. **Konfiguracja** - Dostosowanie szablonu do wymagań
3. **Kopiowanie plików** - Skopiowanie struktury z `tree/`
4. **Renderowanie** - Zastąpienie placeholderów
5. **Instalacja zależności** - `npm install` lub `pnpm install`
6. **Inicjalizacja** - Uruchomienie skryptów inicjalizacyjnych

## 🔧 Dostosowywanie szablonów

### Placeholders w plikach:
- `{{project_name}}` - Nazwa projektu
- `{{project_description}}` - Opis projektu
- `{{author_name}}` - Autor projektu
- `{{database_type}}` - Typ bazy danych

### Warunkowe renderowanie:
```javascript
// Jeśli wybrano MongoDB
{{#if_mongodb}}
const mongoose = require('mongoose');
{{/if_mongodb}}

// Jeśli wybrano PostgreSQL
{{#if_postgresql}}
const { Pool } = require('pg');
{{/if_postgresql}}
```

## 📊 Metryki szablonów

### Popularność szablonów:
- Vite + React + TypeScript - 45%
- React + Express - 30%
- Node.js + Express + MongoDB - 20%
- JavaScript + React - 5%

### Czas generowania:
- Małe projekty: 30-60 sekund
- Średnie projekty: 1-3 minuty
- Duże projekty: 3-10 minut