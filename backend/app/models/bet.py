from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Bet(SQLModel, table=True):
    __tablename__ = "bets"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    match_id: int = Field(foreign_key="matches.id")
    predicted_home: int
    predicted_away: int
    points_awarded: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
