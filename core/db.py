from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from secrets import SQL_SERVER_PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{SQL_SERVER_PASSWORD}@localhost/RecipesFastAPI"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()