from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models.team import Team
from app.dependencies import get_current_user

router = APIRouter(prefix="/teams", tags=["teams"])

@router.get("", response_model=list[Team])
@router.get("/", response_model=list[Team])
def get_teams(
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
) -> list[Team]:
    """Get all teams"""
    teams = session.exec(select(Team)).all()
    return teams


@router.post("/", response_model=Team)
def create_team(team: Team, session: Session = Depends(get_session)) -> Team:
    existing = session.exec(select(Team).where(Team.name == team.name)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Team with this name already exists")
    session.add(team)
    session.commit()
    session.refresh(team)
    return team


@router.get("/{team_id}", response_model=Team)
def get_team(team_id: int, session: Session = Depends(get_session)) -> Team:
    team = session.get(Team, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
