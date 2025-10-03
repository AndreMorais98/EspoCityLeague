from datetime import datetime, date, timedelta
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from app.db import get_session
from app.models.match import Match

router = APIRouter(prefix="/matches", tags=["matches"])


@router.post("/", response_model=Match)
def create_match(match: Match, session: Session = Depends(get_session)) -> Match:
    session.add(match)
    session.commit()
    session.refresh(match)
    return match


@router.get("/{match_id}", response_model=Match)
def get_match(match_id: int, session: Session = Depends(get_session)) -> Match:
    match = session.get(Match, match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match


@router.get("/", response_model=list[Match])
def list_matches_by_day(
    date_str: str = Query(None, alias="date", description="YYYY-MM-DD"),
    session: Session = Depends(get_session),
) -> list[Match]:
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
