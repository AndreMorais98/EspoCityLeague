# EspoCityLeague

Web App for Football betting

## Tech Stack
- Python 3.12 (LTS), FastAPI, SQLModel, SQLAlchemy
- Postgres 17 (Docker), Alembic (migrations)
- Uvicorn (dev server)
- Docker Compose for local dev
- pgAdmin for DB admin

## Prerequisites
- Docker and Docker Compose
- Optional: Make sure the `backend/.env` file exists with DB settings

## Environment Variables
Create `backend/.env` with at least:
```
DB_HOST=DB_HOST
DB_PORT=DB_PORT
DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD

# Optional admin seed (used by initial migration)
ADMIN_USERNAME=ADMIN_USERNAME
ADMIN_PHONE=ADMIN_PHONE
ADMIN_PASSWORD=ADMIN_PASSWORD
```

If you add a frontend app, create `frontend/.env` with:
```

## pgAdmin
- Service runs at `http://localhost:8080`
- Compose can mount `backend/docker/server.json` for a preconfigured server
- Alternatively, add a server manually in pgAdmin using host `db`, port `5432`, and your DB credentials