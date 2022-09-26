from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, ForeignKey
from core.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    nickname = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)


class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
