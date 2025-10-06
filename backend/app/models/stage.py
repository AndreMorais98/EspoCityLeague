from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .match import Match, MatchResponse


class StageBase(SQLModel):
    name: str = Field(max_length=100, description="Stage name (e.g., 'Group Stage', 'Round of 16', 'Quarter Finals')")
    date: datetime = Field(description="Stage date")


class Stage(StageBase, table=True):
    __tablename__ = "stages"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    matches: List["Match"] = Relationship(back_populates="stage")


class StageCreate(StageBase):
    pass


class StageUpdate(SQLModel):
    name: Optional[str] = Field(default=None, max_length=100)
    date: Optional[datetime] = Field(default=None)


class StageResponse(StageBase):
    id: int
    created_at: datetime
    updated_at: datetime
    matches: List["MatchResponse"] = []
