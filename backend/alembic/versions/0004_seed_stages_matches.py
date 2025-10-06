"""Seed future stages and matches data

Revision ID: 0004_seed_stages_matches
Revises: 0003_seed_teams
Create Date: 2025-10-05 20:30:00.000000

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
    # Matchday 1 (Sep 16–18, 2025)
        {"home_team_id": 3, "away_team_id": 2, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 17, 45), "place": None, "home_score": 0, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Athletic Club 0-2 Arsenal (17:45 CEST)
        {"home_team_id": 29, "away_team_id": 32, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 17, 45), "place": None, "home_score": 1, "away_score": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSV Eindhoven 1-3 Union Saint-Gilloise (17:45 CEST)
        {"home_team_id": 18, "away_team_id": 13, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 20, 0), "place": None, "home_score": 4, "away_score": 4, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus 4-4 Borussia Dortmund (20:00 CEST)
        {"home_team_id": 31, "away_team_id": 22, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 20, 0), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Real Madrid 2-1 Marseille (20:00 CEST)
        {"home_team_id": 9, "away_team_id": 30, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 17, 45), "place": None, "home_score": 2, "away_score": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Benfica 2-3 Qarabağ (17:45 CEST)
        {"home_team_id": 35, "away_team_id": 36, "stage_id": 1, "kickoff_at": datetime(2025, 9, 16, 20, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham 1-0 Villarreal (20:00 CEST)
        
        {"home_team_id": 26, "away_team_id": 27, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 17, 45), "place": None, "home_score": 0, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos 0-0 Pafos (17:45 CEST)
        {"home_team_id": 33, "away_team_id": 10, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 17, 45), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Slavia Praha 2-2 Bodø/Glimt (17:45 CEST)
        {"home_team_id": 1, "away_team_id": 17, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 20, 0), "place": None, "home_score": 0, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ajax 0-2 Inter (20:00 CEST)
        {"home_team_id": 8, "away_team_id": 11, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 20, 0), "place": None, "home_score": 3, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern München 3-1 Chelsea (20:00 CEST)
        {"home_team_id": 20, "away_team_id": 5, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 20, 0), "place": None, "home_score": 3, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool 3-2 Atlético de Madrid (20:00 CEST)
        {"home_team_id": 28, "away_team_id": 4, "stage_id": 1, "kickoff_at": datetime(2025, 9, 17, 20, 0), "place": None, "home_score": 4, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Paris Saint-Germain 4-0 Atalanta (20:00 CEST)
        
        {"home_team_id": 12, "away_team_id": 23, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 17, 45), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge 4-1 Monaco (17:45 CEST)
        {"home_team_id": 14, "away_team_id": 7, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 17, 45), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Copenhagen 2-2 Leverkusen (17:45 CEST)
        {"home_team_id": 15, "away_team_id": 16, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 20, 0), "place": None, "home_score": 5, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Frankfurt 5-1 Galatasaray (20:00 CEST)
        {"home_team_id": 21, "away_team_id": 24, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 20, 0), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Manchester City 2-0 Napoli (20:00 CEST)
        {"home_team_id": 25, "away_team_id": 6, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 20, 0), "place": None, "home_score": 1, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle United 1-2 Barcelona (20:00 CEST)
        {"home_team_id": 34, "away_team_id": 19, "stage_id": 1, "kickoff_at": datetime(2025, 9, 18, 20, 0), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP 4-1 Kairat Almaty (20:00 CEST)
        
        # Matchday 2 (Sep 30–Oct 1, 2025) 
        {"home_team_id": 4, "away_team_id": 12, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 17, 45), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta 2-1 Club Brugge (17:45 CEST)
        {"home_team_id": 19, "away_team_id": 31, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 17, 45), "place": None, "home_score": 0, "away_score": 5, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty 0-5 Real Madrid (17:45 CEST)
        {"home_team_id": 5, "away_team_id": 15, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 5, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atlético de Madrid 5-1 Frankfurt (20:00 CEST)
        {"home_team_id": 11, "away_team_id": 9, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea 1-0 Benfica (20:00 CEST)
        {"home_team_id": 17, "away_team_id": 33, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 3, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Inter 3-0 Slavia Praha (20:00 CEST)
        {"home_team_id": 10, "away_team_id": 35, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bodø/Glimt 2-2 Tottenham (20:00 CEST)
        {"home_team_id": 16, "away_team_id": 20, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 1, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray 1-0 Liverpool (20:00 CEST)
        {"home_team_id": 22, "away_team_id": 1, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 4, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Marseille 4-0 Ajax (20:00 CEST)
        {"home_team_id": 27, "away_team_id": 8, "stage_id": 2, "kickoff_at": datetime(2025, 9, 30, 20, 0), "place": None, "home_score": 1, "away_score": 5, "created_at": datetime.now(), "updated_at": datetime.now()},  # Pafos 1-5 Bayern München (20:00 CEST)
        
        {"home_team_id": 30, "away_team_id": 14, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 17, 45), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabağ 2-0 Copenhagen (17:45 CEST)
        {"home_team_id": 32, "away_team_id": 25, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 17, 45), "place": None, "home_score": 0, "away_score": 4, "created_at": datetime.now(), "updated_at": datetime.now()},  # Union Saint-Gilloise 0-4 Newcastle United (17:45 CEST)
        {"home_team_id": 2, "away_team_id": 26, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 2, "away_score": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Arsenal 2-0 Olympiacos (20:00 CEST)
        {"home_team_id": 23, "away_team_id": 21, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco 2-2 Manchester City (20:00 CEST)
        {"home_team_id": 7, "away_team_id": 29, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 1, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Leverkusen 1-1 PSV Eindhoven (20:00 CEST)
        {"home_team_id": 13, "away_team_id": 3, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 4, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Borussia Dortmund 4-1 Athletic Club (20:00 CEST)
        {"home_team_id": 6, "away_team_id": 28, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 1, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona 1-2 Paris Saint-Germain (20:00 CEST)
        {"home_team_id": 24, "away_team_id": 34, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 2, "away_score": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli 2-1 Sporting CP (20:00 CEST)
        {"home_team_id": 36, "away_team_id": 18, "stage_id": 2, "kickoff_at": datetime(2025, 10, 1, 20, 0), "place": None, "home_score": 2, "away_score": 2, "created_at": datetime.now(), "updated_at": datetime.now()},  # Villarreal 2-2 Juventus (20:00 CEST)
        
        # Round 3 (Stage 3)
        # October 21, 17:45 CEST
        {"home_team_id": 6, "away_team_id": 26, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona vs Olympiacos Piraeus
        {"home_team_id": 19, "away_team_id": 27, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty vs Pafos
        # October 21, 20:00 CEST
        {"home_team_id": 2, "away_team_id": 5, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Arsenal vs Atl. Madrid
        {"home_team_id": 7, "away_team_id": 28, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayer Leverkusen vs PSG
        {"home_team_id": 14, "away_team_id": 13, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # FC Copenhagen vs Dortmund
        {"home_team_id": 25, "away_team_id": 9, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle vs Benfica
        {"home_team_id": 29, "away_team_id": 24, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSV vs Napoli
        {"home_team_id": 32, "away_team_id": 17, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Royale Union SG vs Inter
        {"home_team_id": 36, "away_team_id": 21, "stage_id": 3, "kickoff_at": datetime(2025, 10, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Villarreal vs Manchester City
        # October 22, 17:45 CEST
        {"home_team_id": 3, "away_team_id": 30, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ath Bilbao vs Qarabag
        {"home_team_id": 16, "away_team_id": 10, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray vs Bodo/Glimt
        # October 22, 20:00 CEST
        {"home_team_id": 4, "away_team_id": 33, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta vs Slavia Prague
        {"home_team_id": 8, "away_team_id": 12, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern Munich vs Club Brugge KV
        {"home_team_id": 11, "away_team_id": 1, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea vs Ajax
        {"home_team_id": 15, "away_team_id": 20, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Eintracht Frankfurt vs Liverpool
        {"home_team_id": 23, "away_team_id": 35, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco vs Tottenham
        {"home_team_id": 31, "away_team_id": 18, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Real Madrid vs Juventus
        {"home_team_id": 34, "away_team_id": 22, "stage_id": 3, "kickoff_at": datetime(2025, 10, 22, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP vs Marseille

        # Round 4 (Stage 4)
        # November 4, 17:45 CET
        {"home_team_id": 24, "away_team_id": 15, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli vs Eintracht Frankfurt
        {"home_team_id": 33, "away_team_id": 2, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Slavia Prague vs Arsenal
        # November 4, 20:00 CET
        {"home_team_id": 5, "away_team_id": 32, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atl. Madrid vs Royale Union SG
        {"home_team_id": 10, "away_team_id": 23, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bodo/Glimt vs Monaco
        {"home_team_id": 18, "away_team_id": 34, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus vs Sporting CP
        {"home_team_id": 20, "away_team_id": 31, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool vs Real Madrid
        {"home_team_id": 26, "away_team_id": 29, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos Piraeus vs PSV
        {"home_team_id": 28, "away_team_id": 8, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSG vs Bayern Munich
        {"home_team_id": 35, "away_team_id": 14, "stage_id": 4, "kickoff_at": datetime(2025, 11, 4, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham vs FC Copenhagen
        # November 5, 17:45 CET
        {"home_team_id": 27, "away_team_id": 36, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Pafos vs Villarreal
        {"home_team_id": 30, "away_team_id": 11, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabag vs Chelsea
        # November 5, 20:00 CET
        {"home_team_id": 1, "away_team_id": 16, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ajax vs Galatasaray
        {"home_team_id": 9, "away_team_id": 7, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Benfica vs Bayer Leverkusen
        {"home_team_id": 12, "away_team_id": 6, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge KV vs Barcelona
        {"home_team_id": 17, "away_team_id": 19, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Inter vs Kairat Almaty
        {"home_team_id": 21, "away_team_id": 13, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Manchester City vs Dortmund
        {"home_team_id": 22, "away_team_id": 4, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Marseille vs Atalanta
        {"home_team_id": 25, "away_team_id": 3, "stage_id": 4, "kickoff_at": datetime(2025, 11, 5, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle vs Ath Bilbao

        # Round 5 (Stage 5)
        # November 25, 17:45 CET
        {"home_team_id": 1, "away_team_id": 9, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ajax vs Benfica
        {"home_team_id": 16, "away_team_id": 32, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray vs Royale Union SG
        # November 25, 20:00 CET
        {"home_team_id": 10, "away_team_id": 18, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bodo/Glimt vs Juventus
        {"home_team_id": 11, "away_team_id": 6, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea vs Barcelona
        {"home_team_id": 13, "away_team_id": 36, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Dortmund vs Villarreal
        {"home_team_id": 21, "away_team_id": 7, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Manchester City vs Bayer Leverkusen
        {"home_team_id": 22, "away_team_id": 25, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Marseille vs Newcastle
        {"home_team_id": 24, "away_team_id": 30, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli vs Qarabag
        {"home_team_id": 33, "away_team_id": 3, "stage_id": 5, "kickoff_at": datetime(2025, 11, 25, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Slavia Prague vs Ath Bilbao
        # November 26, 17:45 CET
        {"home_team_id": 14, "away_team_id": 19, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # FC Copenhagen vs Kairat Almaty
        {"home_team_id": 27, "away_team_id": 23, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Pafos vs Monaco
        # November 26, 20:00 CET
        {"home_team_id": 2, "away_team_id": 8, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Arsenal vs Bayern Munich
        {"home_team_id": 5, "away_team_id": 17, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atl. Madrid vs Inter
        {"home_team_id": 15, "away_team_id": 4, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Eintracht Frankfurt vs Atalanta
        {"home_team_id": 20, "away_team_id": 29, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool vs PSV
        {"home_team_id": 26, "away_team_id": 31, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos Piraeus vs Real Madrid
        {"home_team_id": 28, "away_team_id": 35, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSG vs Tottenham
        {"home_team_id": 34, "away_team_id": 12, "stage_id": 5, "kickoff_at": datetime(2025, 11, 26, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP vs Club Brugge KV

        # Round 6 (Stage 6)
        # December 9, 15:30 CET
        {"home_team_id": 19, "away_team_id": 26, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 15, 30), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty vs Olympiacos Piraeus
        # December 9, 17:45 CET
        {"home_team_id": 8, "away_team_id": 34, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern Munich vs Sporting CP
        # December 9, 20:00 CET
        {"home_team_id": 4, "away_team_id": 11, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta vs Chelsea
        {"home_team_id": 6, "away_team_id": 15, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona vs Eintracht Frankfurt
        {"home_team_id": 17, "away_team_id": 20, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Inter vs Liverpool
        {"home_team_id": 23, "away_team_id": 16, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco vs Galatasaray
        {"home_team_id": 29, "away_team_id": 5, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSV vs Atl. Madrid
        {"home_team_id": 32, "away_team_id": 22, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Royale Union SG vs Marseille
        {"home_team_id": 35, "away_team_id": 33, "stage_id": 6, "kickoff_at": datetime(2025, 12, 9, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham vs Slavia Prague
        # December 10, 17:45 CET
        {"home_team_id": 30, "away_team_id": 1, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabag vs Ajax
        {"home_team_id": 36, "away_team_id": 14, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Villarreal vs FC Copenhagen
        # December 10, 20:00 CET
        {"home_team_id": 3, "away_team_id": 28, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ath Bilbao vs PSG
        {"home_team_id": 7, "away_team_id": 25, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayer Leverkusen vs Newcastle
        {"home_team_id": 9, "away_team_id": 24, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Benfica vs Napoli
        {"home_team_id": 12, "away_team_id": 2, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge KV vs Arsenal
        {"home_team_id": 13, "away_team_id": 10, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Dortmund vs Bodo/Glimt
        {"home_team_id": 18, "away_team_id": 27, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus vs Pafos
        {"home_team_id": 31, "away_team_id": 21, "stage_id": 6, "kickoff_at": datetime(2025, 12, 10, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Real Madrid vs Manchester City

        # Round 7 (Stage 7)
        # January 20, 15:30 CET
        {"home_team_id": 19, "away_team_id": 12, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 15, 30), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Kairat Almaty vs Club Brugge KV
        # January 20, 17:45 CET
        {"home_team_id": 10, "away_team_id": 21, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bodo/Glimt vs Manchester City
        # January 20, 20:00 CET
        {"home_team_id": 14, "away_team_id": 24, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # FC Copenhagen vs Napoli
        {"home_team_id": 17, "away_team_id": 2, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Inter vs Arsenal
        {"home_team_id": 26, "away_team_id": 7, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Olympiacos Piraeus vs Bayer Leverkusen
        {"home_team_id": 31, "away_team_id": 23, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Real Madrid vs Monaco
        {"home_team_id": 34, "away_team_id": 28, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Sporting CP vs PSG
        {"home_team_id": 35, "away_team_id": 13, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tottenham vs Dortmund
        {"home_team_id": 36, "away_team_id": 1, "stage_id": 7, "kickoff_at": datetime(2026, 1, 20, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Villarreal vs Ajax
        # January 21, 17:45 CET
        {"home_team_id": 16, "away_team_id": 5, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Galatasaray vs Atl. Madrid
        {"home_team_id": 30, "away_team_id": 15, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 17, 45), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Qarabag vs Eintracht Frankfurt
        # January 21, 20:00 CET
        {"home_team_id": 4, "away_team_id": 3, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atalanta vs Ath Bilbao
        {"home_team_id": 8, "away_team_id": 32, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayern Munich vs Royale Union SG
        {"home_team_id": 11, "away_team_id": 27, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Chelsea vs Pafos
        {"home_team_id": 18, "away_team_id": 9, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Juventus vs Benfica
        {"home_team_id": 22, "away_team_id": 20, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Marseille vs Liverpool
        {"home_team_id": 25, "away_team_id": 29, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Newcastle vs PSV
        {"home_team_id": 33, "away_team_id": 6, "stage_id": 7, "kickoff_at": datetime(2026, 1, 21, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Slavia Prague vs Barcelona
        # Round 8 (Stage 8)
        # January 28, 20:00 CET
        {"home_team_id": 1, "away_team_id": 26, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ajax vs Olympiacos Piraeus
        {"home_team_id": 2, "away_team_id": 19, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Arsenal vs Kairat Almaty
        {"home_team_id": 3, "away_team_id": 34, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Ath Bilbao vs Sporting CP
        {"home_team_id": 5, "away_team_id": 10, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Atl. Madrid vs Bodo/Glimt
        {"home_team_id": 6, "away_team_id": 14, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barcelona vs FC Copenhagen
        {"home_team_id": 7, "away_team_id": 36, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Bayer Leverkusen vs Villarreal
        {"home_team_id": 9, "away_team_id": 31, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Benfica vs Real Madrid
        {"home_team_id": 12, "away_team_id": 22, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Club Brugge KV vs Marseille
        {"home_team_id": 13, "away_team_id": 17, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Dortmund vs Inter
        {"home_team_id": 15, "away_team_id": 35, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Eintracht Frankfurt vs Tottenham
        {"home_team_id": 20, "away_team_id": 30, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Liverpool vs Qarabag
        {"home_team_id": 21, "away_team_id": 16, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Manchester City vs Galatasaray
        {"home_team_id": 23, "away_team_id": 18, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Monaco vs Juventus
        {"home_team_id": 24, "away_team_id": 11, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Napoli vs Chelsea
        {"home_team_id": 27, "away_team_id": 33, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # Pafos vs Slavia Prague
        {"home_team_id": 28, "away_team_id": 25, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSG vs Newcastle
        {"home_team_id": 29, "away_team_id": 8, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()},  # PSV vs Bayern Munich
        {"home_team_id": 32, "away_team_id": 4, "stage_id": 8, "kickoff_at": datetime(2026, 1, 28, 20, 0), "place": None, "home_score": None, "away_score": None, "created_at": datetime.now(), "updated_at": datetime.now()}   # Royale Union SG vs Atalanta
    ]

    # Insert stages data
    op.bulk_insert(stages_table, future_stages_data)
    
    # Insert matches data
    op.bulk_insert(matches_table, future_matches_data)
    
    # Update the sequences to start from the next available IDs
    op.execute("SELECT setval('stages_id_seq', (SELECT MAX(id) FROM stages))")
    op.execute("SELECT setval('matches_id_seq', (SELECT MAX(id) FROM matches))")


def downgrade() -> None:
    """Remove seeded future stages and matches data."""
    op.execute("DELETE FROM matches WHERE stage_id BETWEEN 1 AND 17")
    op.execute("DELETE FROM stages WHERE id BETWEEN 1 AND 17")
