"""seed_bets

Revision ID: 0005_seed_bets
Revises: 0004_seed_stages_matches
Create Date: 2025-10-06 15:43:50.380594

Points system based on colors:
- GREEN = 3 points (exact score match)
- YELLOW = 1 point (correct result - win/draw/loss - but wrong score)
- RED = 0 points (wrong result)

Match IDs are mapped from 0004_seed_stages_matches.py in the order they appear in the list.
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '0005_seed_bets'
down_revision: Union[str, Sequence[str], None] = '0004_seed_stages_matches'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Seed bets table with data from all users including points."""
    
    # Create bets table reference
    bets_table = table(
        'bets',
        column('id', sa.Integer),
        column('user_id', sa.Integer),
        column('match_id', sa.Integer),
        column('home_score_prediction', sa.Integer),
        column('away_score_prediction', sa.Integer),
        column('points_awarded', sa.Integer),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )
    
    # User IDs: 1=morais, 2=celo, 3=nuno, 4=barbosa, 5=tiago
 
    
    bets_data = [
        # Match 1: Ath Bilbao VS Arsenal - Actual: 0-2
        {"id": 1, "user_id": 1, "match_id": 1, "home_score_prediction": 0, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 2, "user_id": 4, "match_id": 1, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa GREEN
        {"id": 3, "user_id": 2, "match_id": 1, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 4, "user_id": 3, "match_id": 1, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 5, "user_id": 5, "match_id": 1, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 2: PSV VS Royale Union - Actual: 1-3
        {"id": 6, "user_id": 1, "match_id": 2, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 7, "user_id": 4, "match_id": 2, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 8, "user_id": 2, "match_id": 2, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 9, "user_id": 3, "match_id": 2, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 10, "user_id": 5, "match_id": 2, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 3: Juventus VS Dortmund - Actual: 4-4
        {"id": 11, "user_id": 1, "match_id": 3, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 12, "user_id": 4, "match_id": 3, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 13, "user_id": 2, "match_id": 3, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 14, "user_id": 3, "match_id": 3, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 15, "user_id": 5, "match_id": 3, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 4: Real Madrid VS Marseille - Actual: 2-1
        {"id": 16, "user_id": 1, "match_id": 4, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 17, "user_id": 4, "match_id": 4, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 18, "user_id": 2, "match_id": 4, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo GREEN
        {"id": 19, "user_id": 3, "match_id": 4, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 20, "user_id": 5, "match_id": 4, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 5: Benfica VS Qarabag - Actual: 2-3
        {"id": 21, "user_id": 1, "match_id": 5, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 22, "user_id": 4, "match_id": 5, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 23, "user_id": 2, "match_id": 5, "home_score_prediction": 4, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 24, "user_id": 3, "match_id": 5, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 25, "user_id": 5, "match_id": 5, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 6: Tottenham VS Villarreal - Actual: 1-0
        {"id": 26, "user_id": 1, "match_id": 6, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 27, "user_id": 4, "match_id": 6, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 28, "user_id": 2, "match_id": 6, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo GREEN
        {"id": 29, "user_id": 3, "match_id": 6, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 30, "user_id": 5, "match_id": 6, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago GREEN

        # Match 7: Olympiacos VS Pafos - Actual: 0-0
        {"id": 31, "user_id": 1, "match_id": 7, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 32, "user_id": 4, "match_id": 7, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 33, "user_id": 2, "match_id": 7, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 34, "user_id": 3, "match_id": 7, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 35, "user_id": 5, "match_id": 7, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 8: Slavia Praha VS Bodo - Actual: 2-2
        {"id": 36, "user_id": 1, "match_id": 8, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 37, "user_id": 4, "match_id": 8, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 38, "user_id": 2, "match_id": 8, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 39, "user_id": 3, "match_id": 8, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 40, "user_id": 5, "match_id": 8, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 9: Ajax VS Inter - Actual: 0-2
        {"id": 41, "user_id": 1, "match_id": 9, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 42, "user_id": 4, "match_id": 9, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 43, "user_id": 2, "match_id": 9, "home_score_prediction": 0, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 44, "user_id": 3, "match_id": 9, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 45, "user_id": 5, "match_id": 9, "home_score_prediction": 0, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 10: Bayern VS Chelsea - Actual: 3-1
        {"id": 46, "user_id": 1, "match_id": 10, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais GREEN
        {"id": 47, "user_id": 4, "match_id": 10, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 48, "user_id": 2, "match_id": 10, "home_score_prediction": 3, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 49, "user_id": 3, "match_id": 10, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 50, "user_id": 5, "match_id": 10, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 11: Liverpool VS Atlético M - Actual: 3-2
        {"id": 51, "user_id": 1, "match_id": 11, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 52, "user_id": 4, "match_id": 11, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 53, "user_id": 2, "match_id": 11, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 54, "user_id": 3, "match_id": 11, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 55, "user_id": 5, "match_id": 11, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 12: PSG VS Atalanta - Actual: 4-0
        {"id": 56, "user_id": 1, "match_id": 12, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 57, "user_id": 4, "match_id": 12, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 58, "user_id": 2, "match_id": 12, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 59, "user_id": 3, "match_id": 12, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 60, "user_id": 5, "match_id": 12, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 13: Brugge VS Monaco - Actual: 4-1
        {"id": 61, "user_id": 1, "match_id": 13, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 62, "user_id": 4, "match_id": 13, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 63, "user_id": 2, "match_id": 13, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 64, "user_id": 3, "match_id": 13, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 65, "user_id": 5, "match_id": 13, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 14: Copenhagen VS Leverkusen - Actual: 2-2
        {"id": 66, "user_id": 1, "match_id": 14, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 67, "user_id": 4, "match_id": 14, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 68, "user_id": 2, "match_id": 14, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 69, "user_id": 3, "match_id": 14, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 70, "user_id": 5, "match_id": 14, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 15: Frankfurt VS Galatasaray - Actual: 5-1
        {"id": 71, "user_id": 1, "match_id": 15, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 72, "user_id": 4, "match_id": 15, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 73, "user_id": 2, "match_id": 15, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 74, "user_id": 3, "match_id": 15, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 75, "user_id": 5, "match_id": 15, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 16: Man City VS Napoli - Actual: 2-0
        {"id": 76, "user_id": 1, "match_id": 16, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 77, "user_id": 4, "match_id": 16, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 78, "user_id": 2, "match_id": 16, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 79, "user_id": 3, "match_id": 16, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 80, "user_id": 5, "match_id": 16, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 17: Newcastle VS Barcelona - Actual: 1-2
        {"id": 81, "user_id": 1, "match_id": 17, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais GREEN
        {"id": 82, "user_id": 4, "match_id": 17, "home_score_prediction": 2, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 83, "user_id": 2, "match_id": 17, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 84, "user_id": 3, "match_id": 17, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 85, "user_id": 5, "match_id": 17, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 18: Sporting VS Kairat - Actual: 4-1
        {"id": 86, "user_id": 1, "match_id": 18, "home_score_prediction": 4, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 87, "user_id": 4, "match_id": 18, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa GREEN
        {"id": 88, "user_id": 2, "match_id": 18, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 89, "user_id": 3, "match_id": 18, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 90, "user_id": 5, "match_id": 18, "home_score_prediction": 4, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # MATCHDAY 2 BETS (30-09-2025 and 01-10-2025)
        
        # Match 19: Atalanta VS Brugge - Actual: 2-1
        {"id": 91, "user_id": 1, "match_id": 19, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais GREEN
        {"id": 92, "user_id": 4, "match_id": 19, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 93, "user_id": 2, "match_id": 19, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 94, "user_id": 3, "match_id": 19, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 95, "user_id": 5, "match_id": 19, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 20: Kairat VS Real Madrid - Actual: 0-5
        {"id": 96, "user_id": 1, "match_id": 20, "home_score_prediction": 1, "away_score_prediction": 5, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 97, "user_id": 4, "match_id": 20, "home_score_prediction": 0, "away_score_prediction": 5, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa GREEN
        {"id": 98, "user_id": 2, "match_id": 20, "home_score_prediction": 1, "away_score_prediction": 5, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 99, "user_id": 3, "match_id": 20, "home_score_prediction": 0, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 100, "user_id": 5, "match_id": 20, "home_score_prediction": 0, "away_score_prediction": 5, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago GREEN

        # Match 21: Atlético M VS Frankfurt - Actual: 5-1
        {"id": 101, "user_id": 1, "match_id": 21, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 102, "user_id": 4, "match_id": 21, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 103, "user_id": 2, "match_id": 21, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 104, "user_id": 3, "match_id": 21, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 105, "user_id": 5, "match_id": 21, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 22: Bodo VS Tottenham - Actual: 2-2
        {"id": 106, "user_id": 1, "match_id": 22, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 107, "user_id": 4, "match_id": 22, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 108, "user_id": 2, "match_id": 22, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 109, "user_id": 3, "match_id": 22, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 110, "user_id": 5, "match_id": 22, "home_score_prediction": 0, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 23: Chelsea VS Benfica - Actual: 1-0
        {"id": 111, "user_id": 1, "match_id": 23, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 112, "user_id": 4, "match_id": 23, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 113, "user_id": 2, "match_id": 23, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 114, "user_id": 3, "match_id": 23, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 115, "user_id": 5, "match_id": 23, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 24: Galatasaray VS Liverpool - Actual: 1-0
        {"id": 116, "user_id": 1, "match_id": 24, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 117, "user_id": 4, "match_id": 24, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 118, "user_id": 2, "match_id": 24, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 119, "user_id": 3, "match_id": 24, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 120, "user_id": 5, "match_id": 24, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 25: Inter VS Slavia Praga - Actual: 3-0
        {"id": 121, "user_id": 1, "match_id": 25, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 122, "user_id": 4, "match_id": 25, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 123, "user_id": 2, "match_id": 25, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo GREEN
        {"id": 124, "user_id": 3, "match_id": 25, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 125, "user_id": 5, "match_id": 25, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 26: Marseilla VS Ajax - Actual: 4-0
        {"id": 126, "user_id": 1, "match_id": 26, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 127, "user_id": 4, "match_id": 26, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 128, "user_id": 2, "match_id": 26, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 129, "user_id": 3, "match_id": 26, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 130, "user_id": 5, "match_id": 26, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 27: Pafos VS Bayern - Actual: 1-5
        {"id": 131, "user_id": 1, "match_id": 27, "home_score_prediction": 0, "away_score_prediction": 5, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 132, "user_id": 4, "match_id": 27, "home_score_prediction": 0, "away_score_prediction": 7, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 133, "user_id": 2, "match_id": 27, "home_score_prediction": 0, "away_score_prediction": 6, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 134, "user_id": 3, "match_id": 27, "home_score_prediction": 0, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 135, "user_id": 5, "match_id": 27, "home_score_prediction": 0, "away_score_prediction": 5, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago GREEN

        # Match 28: Qarabag VS Copenhaga - Actual: 2-0
        {"id": 136, "user_id": 1, "match_id": 28, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 137, "user_id": 4, "match_id": 28, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 138, "user_id": 2, "match_id": 28, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 139, "user_id": 3, "match_id": 28, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 140, "user_id": 5, "match_id": 28, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 29: Royale Union VS Newcastle - Actual: 0-4
        {"id": 141, "user_id": 1, "match_id": 29, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 142, "user_id": 4, "match_id": 29, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 143, "user_id": 2, "match_id": 29, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 144, "user_id": 3, "match_id": 29, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 145, "user_id": 5, "match_id": 29, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 30: Arsenal VS Olympiacos - Actual: 2-0
        {"id": 146, "user_id": 1, "match_id": 30, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 147, "user_id": 4, "match_id": 30, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa GREEN
        {"id": 148, "user_id": 2, "match_id": 30, "home_score_prediction": 4, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 149, "user_id": 3, "match_id": 30, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 150, "user_id": 5, "match_id": 30, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 31: Barcelona VS PSG - Actual: 1-2
        {"id": 151, "user_id": 1, "match_id": 31, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 152, "user_id": 4, "match_id": 31, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 153, "user_id": 2, "match_id": 31, "home_score_prediction": 3, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 154, "user_id": 3, "match_id": 31, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 155, "user_id": 5, "match_id": 31, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 32: Leverkusen VS PSV - Actual: 1-1
        {"id": 156, "user_id": 1, "match_id": 32, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 157, "user_id": 4, "match_id": 32, "home_score_prediction": 3, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 158, "user_id": 2, "match_id": 32, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 159, "user_id": 3, "match_id": 32, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno GREEN
        {"id": 160, "user_id": 5, "match_id": 32, "home_score_prediction": 1, "away_score_prediction": 0, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 33: Dortmund VS Ath Bilbao - Actual: 4-1
        {"id": 161, "user_id": 1, "match_id": 33, "home_score_prediction": 3, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais YELLOW
        {"id": 162, "user_id": 4, "match_id": 33, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa YELLOW
        {"id": 163, "user_id": 2, "match_id": 33, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 164, "user_id": 3, "match_id": 33, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 165, "user_id": 5, "match_id": 33, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago YELLOW

        # Match 34: Monaco VS City - Actual: 2-2
        {"id": 166, "user_id": 1, "match_id": 34, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais RED
        {"id": 167, "user_id": 4, "match_id": 34, "home_score_prediction": 0, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 168, "user_id": 2, "match_id": 34, "home_score_prediction": 0, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 169, "user_id": 3, "match_id": 34, "home_score_prediction": 1, "away_score_prediction": 3, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno RED
        {"id": 170, "user_id": 5, "match_id": 34, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 35: Nápoles VS Sporting - Actual: 2-1
        {"id": 171, "user_id": 1, "match_id": 35, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais GREEN
        {"id": 172, "user_id": 4, "match_id": 35, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa GREEN
        {"id": 173, "user_id": 2, "match_id": 35, "home_score_prediction": 2, "away_score_prediction": 0, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo YELLOW
        {"id": 174, "user_id": 3, "match_id": 35, "home_score_prediction": 3, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 175, "user_id": 5, "match_id": 35, "home_score_prediction": 1, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED

        # Match 36: Villareal VS Juventus - Actual: 2-2
        {"id": 176, "user_id": 1, "match_id": 36, "home_score_prediction": 2, "away_score_prediction": 2, "points_awarded": 3, "created_at": datetime.now(), "updated_at": datetime.now()},  # Morais GREEN
        {"id": 177, "user_id": 4, "match_id": 36, "home_score_prediction": 0, "away_score_prediction": 2, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Barbosa RED
        {"id": 178, "user_id": 2, "match_id": 36, "home_score_prediction": 0, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Celo RED
        {"id": 179, "user_id": 3, "match_id": 36, "home_score_prediction": 1, "away_score_prediction": 1, "points_awarded": 1, "created_at": datetime.now(), "updated_at": datetime.now()},  # Nuno YELLOW
        {"id": 180, "user_id": 5, "match_id": 36, "home_score_prediction": 2, "away_score_prediction": 1, "points_awarded": 0, "created_at": datetime.now(), "updated_at": datetime.now()},  # Tiago RED
    ]
    
    # Insert all bets
    op.bulk_insert(bets_table, bets_data)


def downgrade() -> None:
    """Remove all seeded bets."""
    op.execute("DELETE FROM bets WHERE id BETWEEN 1 AND 180")
