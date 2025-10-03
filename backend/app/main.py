from contextlib import asynccontextmanager
from fastapi import FastAPI
from .db import engine
from .routers.teams import router as teams_router
from .routers.matches import router as matches_router
from .routers.bets import router as bets_router
from .routers.auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure DB connectivity
    with engine.connect() as _:
        pass
    yield
    # Shutdown: nothing yet


app = FastAPI(title="EspoCityLeague API", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(teams_router)
app.include_router(matches_router)
app.include_router(bets_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
