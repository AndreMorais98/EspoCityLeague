from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime
import os
import bcrypt

revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String, nullable=False, unique=True),
        sa.Column("phone", sa.String, nullable=False, unique=True),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.text("true")),
        sa.Column("is_superuser", sa.Boolean, nullable=False, server_default=sa.text("false")),
        sa.Column("score", sa.Integer, nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
    )

    admin_username = os.getenv("ADMIN_USERNAME")
    admin_phone = os.getenv("ADMIN_PHONE")
    admin_password = os.getenv("ADMIN_PASSWORD")
    hashed = bcrypt.hashpw(admin_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

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
                "username": admin_username,
                "phone": admin_phone,
                "hashed_password": hashed,
                "is_active": True,
                "is_superuser": True,
                "score": 0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
            {
                "username": "celo",
                "phone": "910000001",
                "hashed_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                "is_active": True,
                "is_superuser": False,
                "score": 0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
            {
                "username": "nuno",
                "phone": "910000002",
                "hashed_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                "is_active": True,
                "is_superuser": False,
                "score": 0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
            {
                "username": "barbosa",
                "phone": "910000003",
                "hashed_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                "is_active": True,
                "is_superuser": False,
                "score": 0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
            {
                "username": "tiagao",
                "phone": "910000004",
                "hashed_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
                "is_active": True,
                "is_superuser": False,
                "score": 0,
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("users")
    