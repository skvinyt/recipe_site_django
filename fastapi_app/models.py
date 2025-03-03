from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

recipe_category = Table(
    'recipe_category', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('category.id'), primary_key=True)
)

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    steps = Column(String, index=True)
    preparation_time = Column(Integer, index=True)
    author_id = Column(Integer, index=True)

    categories = relationship("Category", secondary=recipe_category, back_populates="recipes")

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    recipes = relationship("Recipe", secondary=recipe_category, back_populates="categories")
