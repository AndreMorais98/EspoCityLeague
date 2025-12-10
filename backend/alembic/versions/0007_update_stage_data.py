"""Update stage dates and names

Revision ID: 0007_update_stage_data
Revises: 0006_add_tie_breaking_fields
Create Date: 2025-12-10 00:00:00.000000
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.sql import table, column
import os
import bcrypt


# revision identifiers, used by Alembic.
revision: str = "0007_update_stage_data"
down_revision: Union[str, None] = "0006_add_tie_breaking_fields"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()

    updates = [
        (5,  datetime(2025, 11, 25), "Matchday 5"),
        (6,  datetime(2025, 12, 9),  "Matchday 6"),
        (7,  datetime(2026, 1, 20),  "Matchday 7"),
        (8,  datetime(2026, 1, 28),  "Matchday 8"),
        (9,  datetime(2026, 2, 17),  "KO play-offs - 1st leg"),
        (10, datetime(2026, 2, 24),  "KO play-offs - 2nd leg"),
        (11, datetime(2026, 3, 10),  "Round of 16 - 1st leg"),
        (12, datetime(2026, 3, 17),  "Round of 16 - 2nd leg"),
        (13, datetime(2026, 4, 7),   "Quarter-finals - 1st leg"),
        (14, datetime(2026, 4, 14),  "Quarter-finals - 2nd leg"),
        (15, datetime(2026, 4, 28),  "Semi-finals - 1st leg"),
        (16, datetime(2026, 5, 5),   "Semi-finals - 2nd leg"),
        (17, datetime(2026, 5, 30),  "Finals"),
    ]

    for stage_id, new_date, new_name in updates:
        conn.execute(
            sa.text("""
                UPDATE stages
                SET date = :date,
                    name = :name,
                    updated_at = :updated_at
                WHERE id = :id
            """),
            {
                "id": stage_id,
                "date": new_date,
                "name": new_name,
                "updated_at": datetime.utcnow(),
            }
        )

    # --- ADD ADMIN USER "davide" ---

    username = "davide"
    phone = "+000000000"
    password = os.getenv("ADMIN_PASSWORD")
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    users = table(
        "users",
        column("username", sa.String),
        column("phone", sa.String),
        column("hashed_password", sa.String),
        column("is_active", sa.Boolean),
        column("is_superuser", sa.Boolean),
        column("score", sa.Integer),
        column("created_at", sa.DateTime),
        column("updated_at", sa.DateTime),
    )

    op.bulk_insert(
        users,
        [
            {
                "username": username,
                "phone": phone,
                "hashed_password": hashed,
                "is_active": True,
                "is_superuser": True,
                "score": 0,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            }
        ]
    )


def downgrade() -> None:
    # Write only if you need reversibility. Otherwise leave as pass.
    pass