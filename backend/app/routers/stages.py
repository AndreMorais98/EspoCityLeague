from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..db import get_session
from ..models.stage import Stage, StageCreate, StageUpdate, StageResponse
from ..models.match import Match
from ..models.bet import Bet
from ..dependencies import get_current_user
from ..models.user import User

router = APIRouter(prefix="/stages", tags=["stages"])


@router.post("/", response_model=StageResponse)
def create_stage(
    stage_data: StageCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Create a new stage"""
    stage = Stage(**stage_data.dict())
    session.add(stage)
    session.commit()
    session.refresh(stage)
    return stage


@router.get("", response_model=List[StageResponse])
@router.get("/", response_model=List[StageResponse])
def get_stages(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get all stages"""
    statement = select(Stage).order_by(Stage.date)
    stages = session.exec(statement).all()
    return stages


@router.get("/{stage_id}", response_model=StageResponse)
def get_stage(
    stage_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get a specific stage by ID"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    return stage


@router.put("/{stage_id}", response_model=StageResponse)
def update_stage(
    stage_id: int,
    stage_data: StageUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Update a stage"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    
    stage_dict = stage_data.dict(exclude_unset=True)
    for key, value in stage_dict.items():
        setattr(stage, key, value)
    
    stage.updated_at = stage.updated_at  # This will be updated by the database trigger or manually
    session.add(stage)
    session.commit()
    session.refresh(stage)
    return stage


@router.delete("/{stage_id}")
def delete_stage(
    stage_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Delete a stage (only if no matches are associated)"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    
    # Check if stage has any matches
    statement = select(Match).where(Match.stage_id == stage_id)
    matches = session.exec(statement).all()
    if matches:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete stage with associated matches"
        )
    
    session.delete(stage)
    session.commit()
    return {"message": "Stage deleted successfully"}


@router.get("/{stage_id}/matches")
@router.get("/{stage_id}/matches/")
def get_stage_matches(
    stage_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get all matches for a specific stage with user's bets"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    
    statement = select(Match).where(Match.stage_id == stage_id).order_by(Match.kickoff_at)
    matches = session.exec(statement).all()
    
    # Return matches with their related data and user's bet if exists
    result = []
    for match in matches:
        # Get user's bet for this match
        bet_statement = select(Bet).where(
            Bet.match_id == match.id,
            Bet.user_id == current_user.id
        )
        user_bet = session.exec(bet_statement).first()
        
        match_data = {
            "id": match.id,
            "home_team_id": match.home_team_id,
            "away_team_id": match.away_team_id,
            "stage_id": match.stage_id,
            "kickoff_at": match.kickoff_at,
            "place": match.place,
            "home_score": match.home_score,
            "away_score": match.away_score,
            "created_at": match.created_at,
            "updated_at": match.updated_at,
            "home_team": {
                "id": match.home_team.id,
                "name": match.home_team.name,
                "logo_url": match.home_team.logo_url,
            },
            "away_team": {
                "id": match.away_team.id,
                "name": match.away_team.name,
                "logo_url": match.away_team.logo_url,
            },
            "stage": {
                "id": match.stage.id,
                "name": match.stage.name,
            },
            "user_bet": {
                "id": user_bet.id,
                "home_score_prediction": user_bet.home_score_prediction,
                "away_score_prediction": user_bet.away_score_prediction,
                "points_awarded": user_bet.points_awarded,
            } if user_bet else None
        }
        result.append(match_data)
    
    return result


@router.get("/{stage_id}/bets")
@router.get("/{stage_id}/bets/")
def get_stage_bets(
    stage_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get all bets for matches in a specific stage"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    
    # Get all matches for this stage
    statement = select(Match).where(Match.stage_id == stage_id)
    matches = session.exec(statement).all()
    
    if not matches:
        return []
    
    # Get all bets for these matches
    match_ids = [match.id for match in matches]
    bet_statement = select(Bet).where(Bet.match_id.in_(match_ids)).order_by(Bet.match_id, Bet.user_id)
    bets = session.exec(bet_statement).all()
    
    # Build response with user and match details
    result = []
    for bet in bets:
        bet_data = {
            "id": bet.id,
            "user": {
                "id": bet.user.id,
                "username": bet.user.username,
            },
            "match": {
                "id": bet.match.id,
                "home_team": {
                    "id": bet.match.home_team.id,
                    "name": bet.match.home_team.name,
                    "logo_url": bet.match.home_team.logo_url,
                },
                "away_team": {
                    "id": bet.match.away_team.id,
                    "name": bet.match.away_team.name,
                    "logo_url": bet.match.away_team.logo_url,
                },
                "kickoff_at": bet.match.kickoff_at,
                "home_score": bet.match.home_score,
                "away_score": bet.match.away_score,
                "stage": {
                    "id": bet.match.stage.id,
                    "name": bet.match.stage.name,
                },
            },
            "home_score_prediction": bet.home_score_prediction,
            "away_score_prediction": bet.away_score_prediction,
            "points_awarded": bet.points_awarded,
        }
        result.append(bet_data)
    
    return result
