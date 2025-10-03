import os
from typing import Generator
from sqlmodel import create_engine, Session


def get_database_url() -> str:
    try:
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        return f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    except Exception as e:
        raise Exception(f"Error getting database: {e}")


engine = create_engine(get_database_url(), echo=False, pool_pre_ping=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
