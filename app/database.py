from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config

# Define the PostgreSQL database URL
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://postgres:postgres@db:5432/cyberpunk_inventory'

# Create the SQLAlchemy engine, which connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session to FastAPI endpoints.

    This function is used to inject a database session into path operations.
    It creates a new database session, yields it, and ensures the session is
    closed after the request is complete.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
