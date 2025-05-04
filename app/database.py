from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite DB URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./webhooks.db"
# Create DB engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for ORM models
Base = declarative_base()
