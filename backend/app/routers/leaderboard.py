from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models.user import User
from app.dependencies import get_current_user
from app.services.tie_breaking import update_all_users_tie_breaking_stats

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


@router.get("")
@router.get("/", response_model=list[User])
def get_leaderboard(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> list[User]:
    """Get all users ordered by score with tie-breaking rules:
    1. More correct results
    2. More lone wolf victories  
    3. Fewer defeats
    """
    users = session.exec(
        select(User).order_by(
            User.score.desc(),
            User.correct_results.desc(),
            User.lone_wolf_victories.desc(),
            User.defeats.asc()
        )
    ).all()
    return users


@router.post("/update-stats")
def update_tie_breaking_stats(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> dict:
    """Update tie-breaking statistics for all users (Admin only)"""
    # Check if user is admin
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Admin access required")
    
    update_all_users_tie_breaking_stats(session)
    return {"message": "Tie-breaking statistics updated successfully"}
