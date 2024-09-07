from .database import SessionLocal


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
