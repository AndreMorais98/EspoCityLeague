from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models.user import User
from app.dependencies import get_current_user

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


@router.get("/", response_model=list[User])
def get_leaderboard(
    session: Session = Depends(get_session),
    current_user: str = Depends(get_current_user)
) -> list[User]:
    """Get all users ordered by score (highest first)"""
    users = session.exec(select(User).order_by(User.score.desc())).all()
    return users
