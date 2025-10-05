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
        (1, "Benfica", "https://example.com/logos/benfica.png", "Estádio da Luz", None),
        (2, "Bayern Munich", "https://example.com/logos/bayern.png", "Allianz Arena", None),
        (3, "Real Madrid", "https://example.com/logos/real_madrid.png", "Santiago Bernabéu", None),
        (4, "Inter", "https://example.com/logos/inter.png", "Giuseppe Meazza", None),
        (5, "PSG", "https://example.com/logos/psg.png", "Parc des Princes", None),
        (6, "Arsenal", "https://example.com/logos/arsenal.png", "Emirates Stadium", None),
        (7, "Qarabag", "https://example.com/logos/qarabag.png", "Azersun Arena", None),
        (8, "Dortmund", "https://example.com/logos/dortmund.png", "Signal Iduna Park", None),
        (9, "Manchester City", "https://example.com/logos/man_city.png", "Etihad Stadium", None),
        (10, "Tottenham", "https://example.com/logos/tottenham.png", "Tottenham Hotspur Stadium", None),
        (11, "Atlético Madrid", "https://example.com/logos/atletico.png", "Metropolitano Stadium", None),
        (12, "Newcastle", "https://example.com/logos/newcastle.png", "St. James Park", None),
        (13, "Marseille", "https://example.com/logos/marseille.png", "Stade Vélodrome", None),
        (14, "Club Brugge KV", "https://example.com/logos/brugge.png", "Jan Breydel Stadion", None),
        (15, "Sporting CP", "https://example.com/logos/sporting.png", "Estádio José Alvalade", None),
        (16, "Eintracht Frankfurt", "https://example.com/logos/frankfurt.png", "Deutsche Bank Park", None),
        (17, "Barcelona", "https://example.com/logos/barcelona.png", "Camp Nou", None),
        (18, "Liverpool", "https://example.com/logos/liverpool.png", "Anfield", None),
        (19, "Chelsea", "https://example.com/logos/chelsea.png", "Stamford Bridge", None),
        (20, "Napoli", "https://example.com/logos/napoli.png", "Stadio Diego Armando Maradona", None),
        (21, "Royale Union SG", "https://example.com/logos/union_sg.png", "Stade Joseph Marien", None),
        (22, "Galatasaray", "https://example.com/logos/galatasaray.png", "Rams Park", None),
        (23, "Atalanta", "https://example.com/logos/atalanta.png", "Gewiss Stadium", None),
        (24, "Juventus", "https://example.com/logos/juventus.png", "Allianz Stadium", None),
        (25, "Bodo/Glimt", "https://example.com/logos/bodo_glimt.png", "Aspmyra Stadion", None),
        (26, "Bayer Leverkusen", "https://example.com/logos/leverkusen.png", "BayArena", None),
        (27, "Villarreal", "https://example.com/logos/villarreal.png", "Estadio de la Ceramica", None),
        (28, "PSV", "https://example.com/logos/psv.png", "Philips Stadion", None),
        (29, "FC Copenhagen", "https://example.com/logos/copenhagen.png", "Parken Stadium", None),
        (30, "Olympiacos", "https://example.com/logos/olympiacos.png", "Georgios Karaiskakis Stadium", None),
        (31, "Monaco", "https://example.com/logos/monaco.png", "Stade Louis II", None),
        (32, "Slavia Prague", "https://example.com/logos/slavia_prague.png", "Fortuna Arena", None),
        (33, "Pafos", "https://example.com/logos/pafos.png", "Stelios Kyriakides Stadium", None),
        (34, "Ath Bilbao", "https://example.com/logos/athletic_bilbao.png", "Estadio San Mamés", None),
        (35, "Ajax", "https://example.com/logos/ajax.png", "Johan Cruijff Arena", None),
        (36, "Kairat Almaty", "https://example.com/logos/kairat.png", "Almaty Central Stadium", None)
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
