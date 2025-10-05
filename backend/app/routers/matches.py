from datetime import datetime, date, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
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
