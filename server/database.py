from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Loads the environment variables from .env
load_dotenv() 

# Creates a SQLAlchemy engine using the database URL from environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Defines a Base class for declarative models which will be used to create database tables
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()