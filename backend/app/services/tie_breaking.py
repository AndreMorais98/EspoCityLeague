from sqlmodel import Session, select
from typing import Dict, List, Tuple
from app.models.user import User
from app.models.bet import Bet
from app.models.match import Match


def calculate_tie_breaking_stats(session: Session, user_id: int) -> Dict[str, int]:
    """
    Calculate tie-breaking statistics for a user:
    - correct_results: Number of exact score predictions
    - lone_wolf_victories: Number of unique correct predictions (only user got it right)
    - defeats: Number of incorrect predictions
    """
    
    # Get all bets for the user with match results
    bets_query = select(Bet).where(
        Bet.user_id == user_id,
        Bet.match.has(Match.home_score.isnot(None)),
        Bet.match.has(Match.away_score.isnot(None))
    )
    bets = session.exec(bets_query).all()
    
    correct_results = 0
    lone_wolf_victories = 0
    defeats = 0
    
    for bet in bets:
        match = bet.match
        
        # Check if prediction is correct (exact score)
        is_correct = (
            bet.home_score_prediction == match.home_score and
            bet.away_score_prediction == match.away_score
        )
        
        if is_correct:
            correct_results += 1
            
            # Check if this is a lone wolf victory (only this user got it right)
            all_bets_for_match = session.exec(
                select(Bet).where(
                    Bet.match_id == match.id,
                    Bet.home_score_prediction == match.home_score,
                    Bet.away_score_prediction == match.away_score
                )
            ).all()
            
            if len(all_bets_for_match) == 1:  # Only this user got it right
                lone_wolf_victories += 1
        
        # Count as defeat only if the user got 0 points (completely wrong result)
        if bet.points_awarded == 0:
            defeats += 1
    
    return {
        "correct_results": correct_results,
        "lone_wolf_victories": lone_wolf_victories,
        "defeats": defeats
    }


def update_user_tie_breaking_stats(session: Session, user_id: int) -> None:
    """Update tie-breaking statistics for a specific user"""
    stats = calculate_tie_breaking_stats(session, user_id)
    
    user = session.get(User, user_id)
    if user:
        user.correct_results = stats["correct_results"]
        user.lone_wolf_victories = stats["lone_wolf_victories"]
        user.defeats = stats["defeats"]
        session.add(user)
        session.commit()


def update_all_users_tie_breaking_stats(session: Session) -> None:
    """Update tie-breaking statistics for all users"""
    users = session.exec(select(User)).all()
    
    for user in users:
        stats = calculate_tie_breaking_stats(session, user.id)
        user.correct_results = stats["correct_results"]
        user.lone_wolf_victories = stats["lone_wolf_victories"]
        user.defeats = stats["defeats"]
        session.add(user)
    
    session.commit()
