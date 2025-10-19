from datetime import datetime, date, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from app.db import get_session
from app.models.match import Match, MatchCreate, MatchUpdate, MatchResponse
from app.models.bet import Bet
from app.models.user import User
from app.dependencies import get_current_user

router = APIRouter(prefix="/matches", tags=["matches"])


def calculate_bet_points(home_prediction: int, away_prediction: int, home_actual: int, away_actual: int) -> int:
    """
    Calculate points awarded for a bet based on the prediction vs actual result.
    
    Scoring system:
    - Exact score match: 3 points
    - Correct result (win/draw/loss): 1 point
    - Wrong result: 0 points
    """
    # Exact score match
    if home_prediction == home_actual and away_prediction == away_actual:
        return 3
    
    # Determine predicted result
    if home_prediction > away_prediction:
        predicted_result = "home_win"
    elif home_prediction < away_prediction:
        predicted_result = "away_win"
    else:
        predicted_result = "draw"
    
    # Determine actual result
    if home_actual > away_actual:
        actual_result = "home_win"
    elif home_actual < away_actual:
        actual_result = "away_win"
    else:
        actual_result = "draw"
    
    # Correct result (but not exact score)
    if predicted_result == actual_result:
        return 1
    
    # Wrong result
    return 0


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
    """Update match scores and process bet calculations (admin only)"""
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
    
    # Check if this is the first time scores are being set
    is_first_time_scoring = match.home_score is None and match.away_score is None
    
    # Update match scores
    match.home_score = home_score
    match.away_score = away_score
    match.updated_at = datetime.now()
    
    # Process bets only if this is the first time scores are being set
    if is_first_time_scoring:
        # Get all bets for this match
        bets_stmt = select(Bet).where(Bet.match_id == match_id)
        bets = session.exec(bets_stmt).all()
        
        # Track user score updates
        user_score_updates = {}
        
        for bet in bets:
            # Calculate points for this bet
            points_awarded = calculate_bet_points(
                bet.home_score_prediction,
                bet.away_score_prediction,
                home_score,
                away_score
            )
            
            # Update bet points
            bet.points_awarded = points_awarded
            bet.updated_at = datetime.now()
            
            # Track user score update
            if bet.user_id not in user_score_updates:
                user_score_updates[bet.user_id] = 0
            user_score_updates[bet.user_id] += points_awarded
        
        # Update user scores
        for user_id, points_to_add in user_score_updates.items():
            user = session.get(User, user_id)
            if user:
                user.score += points_to_add
                user.updated_at = datetime.now()
    
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
