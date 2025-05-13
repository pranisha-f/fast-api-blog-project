from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.configg import settings
from typing import Generator

engine = create_engine(settings.DATABASE_URL)
SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db()->Generator:
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()
