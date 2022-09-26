from pydantic import BaseModel
from .models import DishType
from typing import Type


class DishBase(BaseModel):
    text: str


class RecipeBase(BaseModel):
    title: str
    dish_type: DishBase
    description: str
    photo_link: str


class RecipeCreate(RecipeBase):
    pass
