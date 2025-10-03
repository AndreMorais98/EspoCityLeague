from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Team(SQLModel, table=True):
    __tablename__ = "teams"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    logo_url: Optional[str] = None
    stadium_name: Optional[str] = None
    history: Optional[str] = Field(default=None, description="Arbitrary JSON record history")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
