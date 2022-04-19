import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
host = os.getenv('DB_HOST')

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
