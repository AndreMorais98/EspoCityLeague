import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from .routers.teams import router as teams_router
from .routers.matches import router as matches_router
from .routers.bets import router as bets_router
from .routers.auth import router as auth_router
from .routers.leaderboard import router as leaderboard_router
from .routers.stages import router as stages_router
# Import models to ensure they're registered with SQLModel
from .models.user import User
from .models.team import Team
from .models.stage import Stage
from .models.match import Match
from .models.bet import Bet


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure DB connectivity
    with engine.connect() as _:
        pass
    yield
    # Shutdown: nothing yet

cors_origins = os.getenv("CORS_ORIGIN", "http://localhost:3000, http://localhost:5173")

app = FastAPI(title="EspoCityLeague API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(teams_router)
app.include_router(matches_router)
app.include_router(bets_router)
app.include_router(leaderboard_router)
app.include_router(stages_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
