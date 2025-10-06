"""Seed teams data

Revision ID: 0003_seed_teams
Revises: 0002_tables
Create Date: 2025-10-05 20:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision: str = '0003_seed_teams'
down_revision: Union[str, None] = '0002_tables'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Seed teams table with initial data."""
    
    teams_table = table(
        'teams',
        column('id', sa.Integer),
        column('name', sa.String),
        column('logo_url', sa.String),
        column('stadium_name', sa.String),
        column('history', sa.JSON),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )
    
    teams_data = [
        (1, "Ajax", "https://static.flashscore.com/res/image/data/nHNpUPcM-bZZPiwAI.png", "Johan Cruijff Arena", None),
        (2, "Arsenal", "https://static.flashscore.com/res/image/data/pfchdCg5-vcNAdtF9.png", "Emirates Stadium", None),
        (3, "Ath Bilbao", "https://static.flashscore.com/res/image/data/Y7CgBGYg-vJb36ZBF.png", "Estadio San Mamés", None),
        (4, "Atalanta", "https://static.flashscore.com/res/image/data/xASUZ6il-rg6usZns.png", "Gewiss Stadium", None),
        (5, "Atlético Madrid", "https://static.flashscore.com/res/image/data/CjfjIsYg-nLBjwR1F.png", "Metropolitano Stadium", None),
        (6, "Barcelona", "https://static.flashscore.com/res/image/data/8dhw5vxS-fcDVLdrL.png", "Camp Nou", None),
        (7, "Bayer Leverkusen", "https://static.flashscore.com/res/image/data/OWpaDOYA-WrjrBuU2.png", "BayArena", None),
        (8, "Bayern Munich", "https://static.flashscore.com/res/image/data/tMir8iCr-SvLFaVNH.png", "Allianz Arena", None),
        (9, "Benfica", "https://static.flashscore.com/res/image/data/AZHdTBf5-GEKimEim.png", "Estádio da Luz", None),
        (10, "Bodo/Glimt", "https://static.flashscore.com/res/image/data/KKvh8Yjl-nJtu1LWt.png", "Aspmyra Stadion", None),
        (11, "Chelsea", "https://static.flashscore.com/res/image/data/GMmvDEdM-IROrZEJb.png", "Stamford Bridge", None),
        (12, "Club Brugge", "https://static.flashscore.com/res/image/data/0nirFFf5-44lq3LsP.png", "Jan Breydel Stadion", None),
        (13, "Dortmund", "https://static.flashscore.com/res/image/data/Yiq1eU9r-WrjrBuU2.png", "Signal Iduna Park", None),
        (14, "Copenhagen", "https://static.flashscore.com/res/image/data/dvE1YECa-xv6lkb7q.png", "Parken Stadium", None),
        (15, "Frankfurt", "https://static.flashscore.com/res/image/data/f9dVVYCa-86lnAaq9.png", "Deutsche Bank Park", None),
        (16, "Galatasaray", "https://static.flashscore.com/res/image/data/ziy5KsdM-dEXkR0Wq.png", "Rams Park", None),
        (17, "Inter", "https://static.flashscore.com/res/image/data/lxz64qDa-jDrBQiMS.png", "Giuseppe Meazza", None),
        (18, "Juventus", "https://static.flashscore.com/res/image/data/CbDOFGyS-EXzXDYgS.png", "Allianz Stadium", None),
        (19, "Kairat Almaty", "https://static.flashscore.com/res/image/data/6uyKz6FG-rwQpsSWo.png", "Almaty Central Stadium", None),
        (20, "Liverpool", "https://static.flashscore.com/res/image/data/Gr0cGteM-KCp4zq5F.png", "Anfield", None),
        (21, "Man. City", "https://static.flashscore.com/res/image/data/UXcqj7HG-lQuhqN8N.png", "Etihad Stadium", None),
        (22, "Marseille", "https://static.flashscore.com/res/image/data/AwlBhPfM-voNnDKJK.png", "Stade Vélodrome", None),
        (23, "Monaco", "https://static.flashscore.com/res/image/data/GzvUVteM-0SFGJsPk.png", "Stade Louis II", None),
        (24, "Napoli", "https://static.flashscore.com/res/image/data/lhPsgJWg-vTT58gae.png", "Stadio Diego Armando Maradona", None),
        (25, "Newcastle", "https://static.flashscore.com/res/image/data/fojwJwZA-ImMEe0UF.png", "St. James Park", None),
        (26, "Olympiacos", "https://static.flashscore.com/res/image/data/C6DyywyB-lzmp9FUJ.png", "Georgios Karaiskakis Stadium", None),
        (27, "Pafos", "https://static.flashscore.com/res/image/data/WnpK7zEa-dOOzPK2E.png", "Stelios Kyriakides Stadium", None),
        (28, "PSG", "https://static.flashscore.com/res/image/data/EskJufg5-A7UDDuOO.png", "Parc des Princes", None),
        (29, "PSV", "https://static.flashscore.com/res/image/data/OEStlXZA-j5zA1baQ.png", "Philips Stadion", None),
        (30, "Qarabag", "https://static.flashscore.com/res/image/data/Em3WdChl-W0XY6C3I.png", "Azersun Arena", None),
        (31, "Real Madrid", "https://static.flashscore.com/res/image/data/A7kHoxZA-fcDVLdrL.png", "Santiago Bernabéu", None),
        (32, "Royale Union SG", "https://static.flashscore.com/res/image/data/0UfH7zXg-KrZtIamS.png", "Stade Joseph Marien", None),
        (33, "Slavia Prague", "https://static.flashscore.com/res/image/data/vJ0yQjf5-8nl9JmVC.png", "Fortuna Arena", None),
        (34, "Sporting CP", "https://static.flashscore.com/res/image/data/OWbPc9il-Ys9o4HYr.png", "Estádio José Alvalade", None),
        (35, "Tottenham", "https://static.flashscore.com/res/image/data/ARC62UAr-Ig5FKJZ5.png", "Tottenham Hotspur Stadium", None),
        (36, "Villarreal", "https://static.flashscore.com/res/image/data/65Z85Uh5-GSuwY3p9.png", "Estadio de la Ceramica", None),
    ]
    
    # Convert to proper format for bulk_insert
    from datetime import datetime
    now = datetime.now()
    
    teams_insert_data = []
    for team_id, name, logo_url, stadium_name, history in teams_data:
        teams_insert_data.append({
            'id': team_id,
            'name': name,
            'logo_url': logo_url,
            'stadium_name': stadium_name,
            'history': history,
            'created_at': now,
            'updated_at': now
        })
    
    op.bulk_insert(teams_table, teams_insert_data)


def downgrade() -> None:
    """Remove seeded teams data."""
    op.execute("DELETE FROM teams WHERE id BETWEEN 1 AND 36")
