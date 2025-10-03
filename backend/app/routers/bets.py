from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models.bet import Bet

router = APIRouter(prefix="/bets", tags=["bets"])


@router.post("/", response_model=Bet)
def create_bet(bet: Bet, session: Session = Depends(get_session)) -> Bet:
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
    # Only allow updating predictions for now
    bet.predicted_home = bet_update.predicted_home
    bet.predicted_away = bet_update.predicted_away
    session.add(bet)
    session.commit()
    session.refresh(bet)
    return bet


@router.get("/user/{user_id}", response_model=list[Bet])
def list_user_bets(user_id: int, session: Session = Depends(get_session)) -> list[Bet]:
    bets = session.exec(select(Bet).where(Bet.user_id == user_id)).all()
    return bets
