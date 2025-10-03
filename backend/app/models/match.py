from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Match(SQLModel, table=True):
    __tablename__ = "matches"

    id: int = Field(default=None, primary_key=True)
    home_team_id: int = Field(foreign_key="teams.id")
    away_team_id: int = Field(foreign_key="teams.id")
    kickoff_at: datetime = Field(index=True)
    place: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
