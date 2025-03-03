from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = sa.create_engine("postgresql://username:password@localhost/dbname")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Recipe(Base):
    __tablename__ = 'recipes_recipe'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    steps = sa.Column(sa.Text)
    preparation_time = sa.Column(sa.Integer)
    image = sa.Column(sa.String)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('auth_user.id'))
    category_id = sa.Column(sa.Integer, sa.ForeignKey('recipes_category.id'))

class Ingredient(Base):
    __tablename__ = 'recipes_ingredient'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)

class RecipeSchema(BaseModel):
    title: str
    description: Optional[str] = None
    steps: Optional[str] = None
    preparation_time: int
    image: Optional[str] = None
    author_id: int
    category_id: int

app = FastAPI()

@app.get("/recipes/")
async def get_recipes(db: SessionLocal = Depends(get_db)):
    db_recipes = db.query(Recipe).all()
    return db_recipes

@app.post("/recipes/", response_model=RecipeSchema)
async def create_recipe(recipe: RecipeSchema, db: SessionLocal = Depends(get_db)):
    new_recipe = Recipe(
        title=recipe.title,
        description=recipe.description,
        steps=recipe.steps,
        preparation_time=recipe.preparation_time,
        image=recipe.image,
        author_id=recipe.author_id,
        category_id=recipe.category_id
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@app.put("/recipes/{recipe_id}")
async def update_recipe(recipe_id: int, recipe: RecipeSchema, db: SessionLocal = Depends(get_db)):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db_recipe.title = recipe.title
    db_recipe.description = recipe.description
    db_recipe.steps = recipe.steps
    db_recipe.preparation_time = recipe.preparation_time
    db_recipe.image = recipe.image
    db_recipe.author_id = recipe.author_id
    db_recipe.category_id = recipe.category_id
    db.commit()
    return {"message": f"Updated recipe with ID {recipe_id}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)