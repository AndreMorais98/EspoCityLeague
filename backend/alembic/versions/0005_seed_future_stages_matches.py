"""Seed future stages and matches data

Revision ID: 0005_seed_future_stages_matches
Revises: 0004_seed_stages_matches
Create Date: 2025-10-05 20:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '0005_seed_future_stages_matches'
down_revision: Union[str, None] = '0004_seed_stages_matches'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Seed future stages and matches tables with data."""
    
    # Create stages table reference
    stages_table = table(
        'stages',
        column('id', sa.Integer),
        column('name', sa.String),
        column('date', sa.DateTime),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )
    
    # Create matches table reference
    matches_table = table(
        'matches',
        column('id', sa.Integer),
        column('home_team_id', sa.Integer),
        column('away_team_id', sa.Integer),
        column('stage_id', sa.Integer),
        column('kickoff_at', sa.DateTime),
        column('place', sa.String),
        column('home_score', sa.Integer),
        column('away_score', sa.Integer),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )
    
    # Future stages data
    future_stages_data = [
        {
            "id": 3,
            "name": "Matchday 3",
            "date": datetime(2025, 10, 21, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 4,
            "name": "Matchday 4",
            "date": datetime(2025, 11, 4, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 5,
            "name": "Matchday 5",
            "date": datetime(2025, 11, 18, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 6,
            "name": "Matchday 6",
            "date": datetime(2025, 12, 2, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 7,
            "name": "Matchday 7",
            "date": datetime(2025, 12, 16, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 8,
            "name": "Matchday 8",
            "date": datetime(2025, 12, 30, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 9,
            "name": "Knockout Phase Play-offs First Leg",
            "date": datetime(2026, 1, 14, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 10,
            "name": "Knockout Phase Play-offs Second Leg",
            "date": datetime(2026, 1, 21, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 11,
            "name": "Round of 16 First Leg",
            "date": datetime(2026, 2, 18, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 12,
            "name": "Round of 16 Second Leg",
            "date": datetime(2026, 2, 25, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 13,
            "name": "Quarter-finals First Leg",
            "date": datetime(2026, 4, 7, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 14,
            "name": "Quarter-finals Second Leg",
            "date": datetime(2026, 4, 14, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 15,
            "name": "Semi-finals First Leg",
            "date": datetime(2026, 4, 28, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 16,
            "name": "Semi-finals Second Leg",
            "date": datetime(2026, 5, 5, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 17,
            "name": "Final",
            "date": datetime(2026, 5, 30, 0, 0),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    
    # Future matches data
    future_matches_data = [
        # Matchday 3 (2025-10-21)
        {"home_team_id": 18, "away_team_id": 35, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool vs Ajax
        {"home_team_id": 14, "away_team_id": 25, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge vs Bodo/Glimt
        {"home_team_id": 23, "away_team_id": 28, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta vs PSV
        {"home_team_id": 17, "away_team_id": 3, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona vs Real Madrid
        {"home_team_id": 7, "away_team_id": 11, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabag vs Atlético Madrid
        {"home_team_id": 22, "away_team_id": 1, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray vs Benfica
        {"home_team_id": 12, "away_team_id": 16, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle vs Frankfurt
        {"home_team_id": 10, "away_team_id": 33, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham vs Pafos
        {"home_team_id": 24, "away_team_id": 21, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus vs Royale Union SG
        {"home_team_id": 26, "away_team_id": 9, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Leverkusen vs Manchester City
        {"home_team_id": 20, "away_team_id": 4, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli vs Inter
        {"home_team_id": 8, "away_team_id": 32, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Dortmund vs Slavia Prague
        {"home_team_id": 15, "away_team_id": 29, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP vs FC Copenhagen
        {"home_team_id": 36, "away_team_id": 27, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty vs Villarreal
        {"home_team_id": 31, "away_team_id": 34, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco vs Ath Bilbao
        {"home_team_id": 30, "away_team_id": 5, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos vs PSG
        {"home_team_id": 19, "away_team_id": 6, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea vs Arsenal
        {"home_team_id": 2, "away_team_id": 13, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern Munich vs Marseille
        
        # Matchday 4 (2025-11-04)
        {"home_team_id": 6, "away_team_id": 7, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 4, "away_team_id": 29, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 24, "away_team_id": 10, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 18, "away_team_id": 3, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 21, "away_team_id": 35, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 25, "away_team_id": 19, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 33, "away_team_id": 16, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 8, "away_team_id": 13, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 26, "away_team_id": 31, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 20, "away_team_id": 36, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 34, "away_team_id": 27, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 32, "away_team_id": 1, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 14, "away_team_id": 5, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 2, "away_team_id": 11, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 30, "away_team_id": 15, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 17, "away_team_id": 22, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 23, "away_team_id": 9, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 12, "away_team_id": 28, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        
        # Matchday 5 (2025-11-18)
        {"home_team_id": 18, "away_team_id": 25, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 4, "away_team_id": 22, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 32, "away_team_id": 34, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 20, "away_team_id": 29, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 13, "away_team_id": 14, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 9, "away_team_id": 21, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 35, "away_team_id": 6, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 12, "away_team_id": 5, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 16, "away_team_id": 30, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 3, "away_team_id": 28, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 24, "away_team_id": 1, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 31, "away_team_id": 36, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 11, "away_team_id": 33, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 17, "away_team_id": 8, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 2, "away_team_id": 26, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 7, "away_team_id": 27, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 19, "away_team_id": 10, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 23, "away_team_id": 15, "stage_id": 5, "kickoff_at": datetime(2025, 11, 18, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        
        # Matchday 6 (2025-12-02)
        {"home_team_id": 15, "away_team_id": 18, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 31, "away_team_id": 10, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 7, "away_team_id": 24, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 2, "away_team_id": 29, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 35, "away_team_id": 9, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 4, "away_team_id": 5, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 34, "away_team_id": 19, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 16, "away_team_id": 25, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 23, "away_team_id": 1, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 30, "away_team_id": 11, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 8, "away_team_id": 6, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 33, "away_team_id": 27, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 36, "away_team_id": 13, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 20, "away_team_id": 12, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 14, "away_team_id": 26, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 22, "away_team_id": 28, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 3, "away_team_id": 32, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 21, "away_team_id": 17, "stage_id": 6, "kickoff_at": datetime(2025, 12, 2, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        
        # Matchday 7 (2025-12-16)
        {"home_team_id": 5, "away_team_id": 19, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 9, "away_team_id": 8, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 28, "away_team_id": 36, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 7, "away_team_id": 35, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 21, "away_team_id": 1, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 33, "away_team_id": 20, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 25, "away_team_id": 4, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 26, "away_team_id": 17, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 31, "away_team_id": 11, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 27, "away_team_id": 29, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 34, "away_team_id": 14, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 23, "away_team_id": 10, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 15, "away_team_id": 13, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 18, "away_team_id": 2, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 16, "away_team_id": 32, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 24, "away_team_id": 6, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 22, "away_team_id": 30, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 3, "away_team_id": 12, "stage_id": 7, "kickoff_at": datetime(2025, 12, 16, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        
        # Matchday 8 (2025-12-30)
        {"home_team_id": 1, "away_team_id": 33, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 30, "away_team_id": 36, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 26, "away_team_id": 3, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 19, "away_team_id": 20, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 29, "away_team_id": 11, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 32, "away_team_id": 6, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 4, "away_team_id": 7, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 22, "away_team_id": 8, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 2, "away_team_id": 23, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 35, "away_team_id": 28, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 16, "away_team_id": 10, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 5, "away_team_id": 18, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 12, "away_team_id": 25, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 31, "away_team_id": 17, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 34, "away_team_id": 13, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 15, "away_team_id": 14, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 27, "away_team_id": 21, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
        {"home_team_id": 24, "away_team_id": 9, "stage_id": 8, "kickoff_at": datetime(2025, 12, 30, 12, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},
    ]
 
    # Insert stages data
    op.bulk_insert(stages_table, future_stages_data)
    
    # Insert matches data
    op.bulk_insert(matches_table, future_matches_data)


def downgrade() -> None:
    """Remove seeded future stages and matches data."""
    op.execute("DELETE FROM matches WHERE stage_id BETWEEN 3 AND 17")
    op.execute("DELETE FROM stages WHERE id BETWEEN 3 AND 17")
