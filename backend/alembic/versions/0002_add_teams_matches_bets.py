from alembic import op
import sqlalchemy as sa

revision = "0002_add_teams_matches_bets"
down_revision = "0001_init"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "teams",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("logo_url", sa.String, nullable=True),
        sa.Column("stadium_name", sa.String, nullable=True),
        sa.Column("history", sa.JSON, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )

    op.create_table(
        "matches",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("home_team_id", sa.Integer, sa.ForeignKey("teams.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("away_team_id", sa.Integer, sa.ForeignKey("teams.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("kickoff_at", sa.DateTime, nullable=False),
        sa.Column("place", sa.String, nullable=True),
        sa.Column("home_score", sa.Integer, nullable=True),
        sa.Column("away_score", sa.Integer, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_matches_kickoff_at", "matches", ["kickoff_at"]) 

    op.create_table(
        "bets",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("match_id", sa.Integer, sa.ForeignKey("matches.id", ondelete="CASCADE"), nullable=False),
        sa.Column("predicted_home", sa.Integer, nullable=False),
        sa.Column("predicted_away", sa.Integer, nullable=False),
        sa.Column("points_awarded", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_bets_user_id_match_id", "bets", ["user_id", "match_id"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_bets_user_id_match_id", table_name="bets")
    op.drop_table("bets")
    op.drop_index("ix_matches_kickoff_at", table_name="matches")
    op.drop_table("matches")
    op.drop_table("teams")
