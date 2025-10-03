# EspoCityLeague Backend

FastAPI + SQLModel backend for a football betting webapp. Provides endpoints to manage teams, matches, and bets. Uses Postgres and Alembic migrations.

## Tech
- Python 3.12, FastAPI, SQLModel, SQLAlchemy
- Postgres 17 (Docker)
- Alembic (migrations)
- Uvicorn (dev server)

## Quick Start
```bash
# From repo root or here
cd backend
# Build and start services (API, DB, pgAdmin)
docker compose up --build
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- pgAdmin: http://localhost:8080

## Environment
Create `.env` in `backend/`:
```
DB_HOST=db
DB_PORT=5432
DB_NAME=espocity
DB_USER=postgres
DB_PASSWORD=postgres

# Admin seed for initial migration
ADMIN_USERNAME=admin
ADMIN_PHONE=0000000000
ADMIN_PASSWORD=admin
```
If the Postgres volume already exists and `DB_NAME` is missing, create it:
```bash
docker compose exec -T db psql -U "$DB_USER" -d postgres -c "CREATE DATABASE \"$DB_NAME\";"
```

## Migrations
- Create (autogenerate):
```bash
docker compose run --rm backend bash -lc "alembic revision -m 'message' --autogenerate"
```
- Apply:
```bash
docker compose run --rm backend alembic upgrade head
```
- Downgrade one step:
```bash
docker compose run --rm backend alembic downgrade -1
```

## API Overview
- Teams
  - POST `/teams` – create team
  - GET `/teams/{id}` – get team by id
- Matches
  - POST `/matches` – create match
  - GET `/matches/{id}` – get match by id
  - GET `/matches?date=YYYY-MM-DD` – list matches for a day (UTC)
- Bets
  - POST `/bets` – create bet (one per user per match)
  - PATCH `/bets/{id}` – update bet predictions
  - GET `/bets/{id}` – get bet by id
  - GET `/bets/user/{user_id}` – list user's bet history

## Data Model (summary)
- User: username, phone, hashed_password, is_superuser, timestamps
- Team: name, logo_url, stadium_name, history (stringified JSON), timestamps
- Match: home_team_id, away_team_id, kickoff_at, place, scores, timestamps
- Bet: user_id, match_id, predicted_home, predicted_away, points_awarded (default 0), timestamps

## Dev Notes
- Dependencies managed by Poetry (installed in the image; `--no-root`).
- `backend/docker-compose.yml` loads env for both API and DB.
- Rebuild after dependency changes: `docker compose build backend`.
