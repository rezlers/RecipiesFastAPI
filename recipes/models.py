from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="recipes")
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    title = Column(String)
    dish_type = Column(Integer, ForeignKey("dishtypes.id"))
    description = Column(Text)
    photo_link = Column(String)
    is_active = Column(Boolean)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    nickname = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
    is_active = Column(Boolean)


class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    date = Column(DateTime)


class DishType(Base):
    __tablename__ = 'dishtypes'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(String)


class Step(Base):
    __tablename__ = 'steps'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", backref="steps")
    step = Column(Text)


class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)


class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    recipe = relationship("Recipe", backref="hashtags")



