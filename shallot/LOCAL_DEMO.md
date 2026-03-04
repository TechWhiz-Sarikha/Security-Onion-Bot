# Shallot Local Demo (No Docker)

This guide runs Shallot directly on your machine for demos/presentations.

## 1) Folder structure

```text
shallot/
  backend/
    src/app/...               # FastAPI app
    requirements.txt          # pip install dependencies
    .env.example              # local environment template
    data/                     # local SQLite DB will be created here
  frontend/
    src/...                   # Vue + Vuetify app
    vite.config.ts            # proxies /api to localhost:8000
```

## 2) Backend setup

```powershell
cd shallot\backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
```

Notes:
- `DEMO_MODE=true` in `.env` enables mock Security Onion alerts.
- SQLite DB is local: `backend/data/app.db`.
- CORS allows `http://localhost:5173`.

## 3) Frontend setup

```powershell
cd shallot\frontend
npm install
```

## 4) Run commands

Backend:
```powershell
cd shallot\backend
.\.venv\Scripts\activate
uvicorn app.main:app --app-dir src --reload --port 8000
```

Frontend:
```powershell
cd shallot\frontend
npm run dev
```

## 5) First admin user (auth kept enabled)

Open `http://localhost:5173`.
If no users exist, Shallot redirects to `/setup` where you create the first admin user.

Alternative API method:
```powershell
curl -X POST http://localhost:8000/api/auth/first-user `
  -H "Content-Type: application/json" `
  -d "{\"username\":\"admin\",\"password\":\"password123\"}"
```

## 6) Example mock alert data

`!alerts` in the Commands page returns demo alerts like:

```text
[HIGH] - ET TROJAN Suspicious PowerShell Encoded Command
  ruleid: 2024211
  eventid: demo-evt-001
  source: 10.10.20.15:54218
  destination: 185.199.110.153:443
  observer.name: so-sensor-01
```

## 7) Demo flow in browser

1. Open `http://localhost:5173`
2. Create first admin (or login)
3. Dashboard page loads
4. Commands page (`/dashboard/api-test`) loads
5. Run `!alerts` to show Security Onion-style alert analysis from mock data
