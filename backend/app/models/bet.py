from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Bet(SQLModel, table=True):
    __tablename__ = "bets"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    match_id: int = Field(foreign_key="matches.id")
    home_score_prediction: int
    away_score_prediction: int
    points_awarded: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    # Relationships
    match: "Match" = Relationship(back_populates="bets")
    user: "User" = Relationship(back_populates="bets")
