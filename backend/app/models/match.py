from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Integer, ForeignKey
from datetime import datetime

if TYPE_CHECKING:
    from .stage import Stage
    from .team import Team
    from .bet import Bet


class MatchBase(SQLModel):
    kickoff_at: datetime = Field(index=True)
    place: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None


class Match(MatchBase, table=True):
    __tablename__ = "matches"

    id: int = Field(default=None, primary_key=True)
    home_team_id: int = Field(sa_column=Column(Integer, ForeignKey("teams.id", ondelete="RESTRICT"), nullable=False))
    away_team_id: int = Field(sa_column=Column(Integer, ForeignKey("teams.id", ondelete="RESTRICT"), nullable=False))
    stage_id: int = Field(sa_column=Column(Integer, ForeignKey("stages.id", ondelete="RESTRICT"), nullable=False))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    stage: "Stage" = Relationship(back_populates="matches")
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
    home_team_id: int
    away_team_id: int
    stage_id: int


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
    home_team_id: int
    away_team_id: int
    stage_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
