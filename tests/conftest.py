import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import User
from auth.dependencies import get_current_user
import config

# Define the test database engine
SQLALCHEMY_TEST_DATABASE_URL = f'postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.TEST_DB_NAME}'

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create all tables in the test database
def create_test_db():
    Base.metadata.create_all(bind=engine)


def drop_test_db():
    Base.metadata.drop_all(bind=engine)


# Dependency override for test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


# Mock the get_current_user dependency to always return a test user
def override_get_current_user():
    return User(id=1, username="testuser", hashed_password="test123")


app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    # Setup: Clear the test database
    drop_test_db()
    create_test_db()
    yield
    # Teardown: Clear the test database after each test
    drop_test_db()
