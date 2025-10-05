"""Seed stages and matches data

Revision ID: 0004_seed_stages_matches
Revises: 0003_seed_teams
Create Date: 2025-10-05 20:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '0004_seed_stages_matches'
down_revision: Union[str, None] = '0003_seed_teams'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Seed stages and matches tables with initial data."""
    
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
    
    # Stages data
    stages_data = [
        {
            "id": 1,
            "name": "Matchday 1",
            "date": datetime(2025, 9, 16),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "id": 2,
            "name": "Matchday 2", 
            "date": datetime(2025, 9, 30),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    
    # Matches data
    matches_data = [
        # Matchday 1
        {"home_team_id": 34, "away_team_id": 6, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 0, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ath Bilbao 0-2 Arsenal
        {"home_team_id": 28, "away_team_id": 21, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 1, "away_score": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSV 1-3 Royale Union SG
        {"home_team_id": 24, "away_team_id": 8, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 4, "away_score": 4, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus 4-4 Dortmund
        {"home_team_id": 3, "away_team_id": 13, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Real Madrid 2-1 Marseille
        {"home_team_id": 1, "away_team_id": 7, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 2, "away_score": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Benfica 2-3 Qarabag
        {"home_team_id": 10, "away_team_id": 27, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 12, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham 1-0 Villarreal
        
        {"home_team_id": 30, "away_team_id": 33, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 0, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos 0-0 Pafos
        {"home_team_id": 32, "away_team_id": 25, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Slavia Prague 2-2 Bodo/Glimt
        {"home_team_id": 35, "away_team_id": 4, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 0, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ajax 0-2 Inter
        {"home_team_id": 2, "away_team_id": 19, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 3, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern Munich 3-1 Chelsea
        {"home_team_id": 18, "away_team_id": 11, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 3, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool 3-2 Atlético Madrid
        {"home_team_id": 5, "away_team_id": 23, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 12, 0), "place": None, "home_score": 4, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSG 4-0 Atalanta
        
        {"home_team_id": 14, "away_team_id": 31, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge 4-1 Monaco
        {"home_team_id": 29, "away_team_id": 26, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # FC Copenhagen 2-2 Bayer Leverkusen
        {"home_team_id": 16, "away_team_id": 22, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 5, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Eintracht Frankfurt 5-1 Galatasaray
        {"home_team_id": 9, "away_team_id": 20, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Manchester City 2-0 Napoli
        {"home_team_id": 12, "away_team_id": 17, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 1, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle 1-2 Barcelona
        {"home_team_id": 15, "away_team_id": 36, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 12, 0), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP 4-1 Kairat Almaty
        
        # Matchday 2
        {"home_team_id": 23, "away_team_id": 14, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta 2-1 Club Brugge
        {"home_team_id": 36, "away_team_id": 3, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 0, "away_score": 5, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty 0-5 Real Madrid
        {"home_team_id": 11, "away_team_id": 16, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 5, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atlético Madrid 5-1 Eintracht Frankfurt
        {"home_team_id": 19, "away_team_id": 1, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea 1-0 Benfica
        {"home_team_id": 4, "away_team_id": 32, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 3, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Inter 3-0 Slavia Prague
        {"home_team_id": 25, "away_team_id": 10, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bodo/Glimt 2-2 Tottenham
        {"home_team_id": 22, "away_team_id": 18, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray 1-0 Liverpool
        {"home_team_id": 13, "away_team_id": 35, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 4, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Marseille 4-0 Ajax
        {"home_team_id": 33, "away_team_id": 2, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 12, 0), "place": None, "home_score": 1, "away_score": 5, "created_at": datetime.now(), "updated_at": datetime.now()},  # Pafos 1-5 Bayern Munich
        
        {"home_team_id": 7, "away_team_id": 29, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabag 2-0 FC Copenhagen
        {"home_team_id": 21, "away_team_id": 12, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 0, "away_score": 4, "created_at": datetime.now(), "updated_at": datetime.now()},  # Royale Union SG 0-4 Newcastle
        {"home_team_id": 6, "away_team_id": 30, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Arsenal 2-0 Olympiacos
        {"home_team_id": 31, "away_team_id": 9, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco 2-2 Manchester City
        {"home_team_id": 26, "away_team_id": 28, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 1, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayer Leverkusen 1-1 PSV
        {"home_team_id": 8, "away_team_id": 34, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Dortmund 4-1 Ath Bilbao
        {"home_team_id": 17, "away_team_id": 5, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 1, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona 1-2 PSG
        {"home_team_id": 20, "away_team_id": 15, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli 2-1 Sporting CP
        {"home_team_id": 27, "away_team_id": 24, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 12, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Villarreal 2-2 Juventus
    ]
    
    # Insert stages data
    op.bulk_insert(stages_table, stages_data)
    
    # Insert matches data
    op.bulk_insert(matches_table, matches_data)


def downgrade() -> None:
    """Remove seeded stages and matches data."""
    op.execute("DELETE FROM matches WHERE stage_id IN (1, 2)")
    op.execute("DELETE FROM stages WHERE id IN (1, 2)")
