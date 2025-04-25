from typing import List

import uvicorn

from db.database import SessionLocal
from fastapi import FastAPI, Depends

from db.table_film import Film
from schema import FilmGet, FilmByCategoryGet
from table_category import Category
from table_film_category import FilmCategory

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/film", response_model=List[FilmGet])
def get_all_films(limit: int = 10, db=Depends(get_db)):
    response = db.query(Film).limit(limit).all()
    return response


@app.get("/film-by-category/{category}", response_model=List[FilmByCategoryGet])
def get_film_by_category(category: str, limit: int = 10, db=Depends(get_db)):
    response = db.query(Film).join(FilmCategory).join(Category).filter(
        Category.name == category).limit(limit).all()
    return response


if __name__ == "__main__":
    uvicorn.run(app)
