from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from datetime import datetime
from app.db import get_session
from app.models.bet import Bet
from app.models.match import Match

router = APIRouter(prefix="/bets", tags=["bets"])


@router.post("/", response_model=Bet)
def create_bet(bet: Bet, session: Session = Depends(get_session)) -> Bet:
    # Validate prediction values
    if bet.home_score_prediction < 0 or bet.away_score_prediction < 0:
        raise HTTPException(status_code=400, detail="Predictions must be non-negative numbers")
    
    # Check if match exists and hasn't started
    match = session.get(Match, bet.match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    if datetime.now() >= match.kickoff_at:
        raise HTTPException(status_code=400, detail="Cannot place bet after match has started")
    
    # Enforce one bet per user per match
    existing = session.exec(
        select(Bet).where(Bet.user_id == bet.user_id, Bet.match_id == bet.match_id)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bet already exists for this user and match")
    
    session.add(bet)
    session.commit()
    session.refresh(bet)
    return bet


@router.get("/", response_model=list[Bet])
def list_bets(session: Session = Depends(get_session)) -> list[Bet]:
    return session.exec(select(Bet)).all()


@router.get("/{bet_id}", response_model=Bet)
def get_bet(bet_id: int, session: Session = Depends(get_session)) -> Bet:
    bet = session.get(Bet, bet_id)
    if not bet:
        raise HTTPException(status_code=404, detail="Bet not found")
    return bet


@router.patch("/{bet_id}", response_model=Bet)
def update_bet(bet_id: int, bet_update: Bet, session: Session = Depends(get_session)) -> Bet:
    bet = session.get(Bet, bet_id)
    if not bet:
        raise HTTPException(status_code=404, detail="Bet not found")
    
    # Validate prediction values
    if bet_update.home_score_prediction < 0 or bet_update.away_score_prediction < 0:
        raise HTTPException(status_code=400, detail="Predictions must be non-negative numbers")
    
    # Check if match exists and hasn't started
    match = session.get(Match, bet.match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    if datetime.now() >= match.kickoff_at:
        raise HTTPException(status_code=400, detail="Cannot update bet after match has started")
    
    # Only allow updating predictions for now
    bet.home_score_prediction = bet_update.home_score_prediction
    bet.away_score_prediction = bet_update.away_score_prediction
    bet.updated_at = datetime.now()
    session.add(bet)
    session.commit()
    session.refresh(bet)
    return bet


@router.get("/user/{user_id}", response_model=list[Bet])
def list_user_bets(user_id: int, session: Session = Depends(get_session)) -> list[Bet]:
    bets = session.exec(select(Bet).where(Bet.user_id == user_id)).all()
    return bets
