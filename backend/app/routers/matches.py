from datetime import datetime, date, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from app.db import get_session
from app.models.match import Match, MatchCreate, MatchUpdate, MatchResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/matches", tags=["matches"])


@router.post("/", response_model=MatchResponse)
def create_match(
    match_data: MatchCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> MatchResponse:
    """Create a new match"""
    match = Match(**match_data.dict())
    session.add(match)
    session.commit()
    session.refresh(match)
    return match


@router.get("/{match_id}", response_model=MatchResponse)
def get_match(
    match_id: int, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> MatchResponse:
    """Get a specific match by ID"""
    match = session.get(Match, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match


@router.patch("/{match_id}/scores", response_model=MatchResponse)
def update_match_scores(
    match_id: int,
    scores: dict,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> MatchResponse:
    """Update match scores (admin only)"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only administrators can update match scores"
        )
    
    match = session.get(Match, match_id)
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found"
        )
    
    # Validate scores
    home_score = scores.get("home_score")
    away_score = scores.get("away_score")
    
    if home_score is None or away_score is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both home_score and away_score are required"
        )
    
    if not isinstance(home_score, int) or not isinstance(away_score, int):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scores must be integers"
        )
    
    if home_score < 0 or away_score < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scores must be non-negative"
        )
    
    # Update scores
    match.home_score = home_score
    match.away_score = away_score
    match.updated_at = datetime.now()
    
    session.add(match)
    session.commit()
    session.refresh(match)
    
    return match


@router.put("/{match_id}", response_model=MatchResponse)
def update_match(
    match_id: int,
    match_data: MatchUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> MatchResponse:
    """Update a match"""
    match = session.get(Match, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    match_dict = match_data.dict(exclude_unset=True)
    for key, value in match_dict.items():
        setattr(match, key, value)
    
    match.updated_at = match.updated_at  # This will be updated by the database trigger or manually
    session.add(match)
    session.commit()
    session.refresh(match)
    return match


@router.get("/", response_model=List[MatchResponse])
def list_matches_by_day(
    date_str: str = Query(None, alias="date", description="YYYY-MM-DD"),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
) -> List[MatchResponse]:
    """Get matches, optionally filtered by date"""
    if not date_str:
        return session.exec(select(Match)).all()
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    start = datetime.combine(d, datetime.min.time())
    end = start + timedelta(days=1)
    stmt = select(Match).where(Match.kickoff_at >= start, Match.kickoff_at < end)
    return session.exec(stmt).all()
