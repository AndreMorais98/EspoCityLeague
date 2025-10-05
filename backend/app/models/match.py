from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class MatchBase(SQLModel):
    home_team_id: int = Field(foreign_key="teams.id")
    away_team_id: int = Field(foreign_key="teams.id")
    stage_id: int = Field(foreign_key="stages.id", description="Stage this match belongs to")
    kickoff_at: datetime = Field(index=True)
    place: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None


class Match(MatchBase, table=True):
    __tablename__ = "matches"

    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    stage: "Stage" = Relationship(
        back_populates="matches",
        sa_relationship_kwargs={"foreign_keys": "[Match.stage_id]"}  # Explicitly specify the foreign key
    )
    home_team: "Team" = Relationship(
        back_populates="home_matches",
        sa_relationship_kwargs={"foreign_keys": "[Match.home_team_id]"}
    )
    away_team: "Team" = Relationship(
        back_populates="away_matches",
        sa_relationship_kwargs={"foreign_keys": "[Match.away_team_id]"}
    )
    bets: List["Bet"] = Relationship(back_populates="match")


class MatchCreate(MatchBase):
    pass


class MatchUpdate(SQLModel):
    home_team_id: Optional[int] = None
    away_team_id: Optional[int] = None
    stage_id: Optional[int] = None
    kickoff_at: Optional[datetime] = None
    place: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None


class MatchResponse(MatchBase):
    id: int
    created_at: datetime
    updated_at: datetime
    stage: "StageResponse"
    home_team: "TeamResponse"
    away_team: "TeamResponse"
    bets: List["BetResponse"] = []