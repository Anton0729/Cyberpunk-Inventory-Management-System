from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the PostgreSQL database URL
# SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://postgres:postgres@db:5432/cyberpunk_inventory'
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres@localhost:5432/cyberpunk_inventory"
)

# Create the SQLAlchemy engine, which connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
