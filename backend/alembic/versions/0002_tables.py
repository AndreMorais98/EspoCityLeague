"""Add teams, matches, bets, and stages tables

Revision ID: 0002_tables
Revises: 0001_init
Create Date: 2025-10-05 19:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0002_tables'
down_revision: Union[str, None] = '0001_init'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create teams, stages, matches, and bets tables."""
    
    # Create teams table
    op.create_table('teams',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('logo_url', sa.String(), nullable=True),
        sa.Column('stadium_name', sa.String(), nullable=True),
        sa.Column('history', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_teams_name'), 'teams', ['name'], unique=False)
    
    # Create stages table
    op.create_table('stages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('date', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create matches table
    op.create_table('matches',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('home_team_id', sa.Integer(), nullable=False),
        sa.Column('away_team_id', sa.Integer(), nullable=False),
        sa.Column('stage_id', sa.Integer(), nullable=False),
        sa.Column('kickoff_at', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('place', sa.String(), nullable=True),
        sa.Column('home_score', sa.Integer(), nullable=True),
        sa.Column('away_score', sa.Integer(), nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['away_team_id'], ['teams.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['home_team_id'], ['teams.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(['stage_id'], ['stages.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_matches_kickoff_at'), 'matches', ['kickoff_at'], unique=False)
    op.create_index(op.f('ix_matches_stage_id'), 'matches', ['stage_id'], unique=False)
    
    # Create bets table
    op.create_table('bets',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('match_id', sa.Integer(), nullable=False),
        sa.Column('home_score_prediction', sa.Integer(), nullable=False),
        sa.Column('away_score_prediction', sa.Integer(), nullable=False),
        sa.Column('points_awarded', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['match_id'], ['matches.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'match_id')
    )
    op.create_index(op.f('ix_bets_user_id_match_id'), 'bets', ['user_id', 'match_id'], unique=True)


def downgrade() -> None:
    """Drop teams, matches, bets, and stages tables."""
    op.drop_index(op.f('ix_bets_user_id_match_id'), table_name='bets')
    op.drop_table('bets')
    op.drop_index(op.f('ix_matches_stage_id'), table_name='matches')
    op.drop_index(op.f('ix_matches_kickoff_at'), table_name='matches')
    op.drop_table('matches')
    op.drop_table('stages')
    op.drop_index(op.f('ix_teams_name'), table_name='teams')
    op.drop_table('teams')
