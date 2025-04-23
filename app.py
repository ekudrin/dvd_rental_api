from typing import List

import uvicorn

from db.database import SessionLocal
from fastapi import FastAPI, Depends

from db.table_film import Film
from schema import FilmGet

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/film", response_model=List[FilmGet])
def get_all_films(limit: int = 10, db=Depends(get_db)):
    response = db.query(Film).limit(limit).all()
    return response


if __name__ == "__main__":
    uvicorn.run(app)
