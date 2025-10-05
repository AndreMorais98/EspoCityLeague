from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..db import get_session
from ..models.stage import Stage, StageCreate, StageUpdate, StageResponse
from ..models.match import Match
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


@router.get("/{stage_id}/matches", response_model=List[Match])
def get_stage_matches(
    stage_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get all matches for a specific stage"""
    stage = session.get(Stage, stage_id)
    if not stage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stage not found"
        )
    
    statement = select(Match).where(Match.stage_id == stage_id).order_by(Match.kickoff_at)
    matches = session.exec(statement).all()
    return matches
