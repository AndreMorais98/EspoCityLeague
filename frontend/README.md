# EspoCityLeague Frontend

This directory is intended for the web frontend (e.g., Vite/React, Next.js, SvelteKit) that consumes the backend API.

## Prerequisites
- Node.js 18+ and npm/pnpm/yarn

## Setup (example with Vite + React)
```bash
cd frontend
npm create vite@latest . -- --template react-ts
npm install
```

## Environment
Create `.env` (or `.env.local`) pointing to the backend API:
```
VITE_API_BASE_URL=http://localhost:8000
```
For Next.js, use:
```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Dev
```bash
npm run dev
# visit http://localhost:5173 (Vite) or the port your framework uses
```

## API usage
- The backend runs at `http://localhost:8000` by default.
- Endpoints:
  - Teams: POST /teams, GET /teams/{id}
  - Matches: POST /matches, GET /matches/{id}, GET /matches?date=YYYY-MM-DD
  - Bets: POST /bets, PATCH /bets/{id}, GET /bets/{id}, GET /bets/user/{user_id}


## Build & Deploy
- Configure the API base URL for production via envs.
- Build: `npm run build` then host `dist/` (Vite) or use your framework's deploy process.
