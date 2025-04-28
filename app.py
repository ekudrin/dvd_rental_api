from typing import List

import uvicorn

from db.database import SessionLocal
from fastapi import FastAPI, Depends, Query
from typing import Annotated
from db.table_film import Film
from enums import FilmCategoryEnum
from schema import FilmGet
from table_category import Category
from table_film_category import FilmCategory
from table_inventory import Inventory

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/film/", response_model=List[FilmGet])
def get_all_films(limit: int = 10, db=Depends(get_db)):
    """
    Возвращает заданное параметром limit количество фильмов.

    :param limit: Количество строк, которые необходимо вернуть, по умолчанию 10
    :param db: Подключение к базе данных
    :return: Лист сущностей FIlmGet, в текущей реализации это все поля таблицы.
    """
    response = db.query(Film.film_id, Film.title,Film.release_year, Film.length, Film.rating, Film.description, Film.special_features,
                        Film.rental_rate, Film.rental_duration).limit(
        limit).all()
    return response


@app.get("/film/by-category", response_model=List[FilmGet])
def get_film_by_category(category: FilmCategoryEnum = Query(), limit: int = 10, db=Depends(get_db)):
    """
    Возвращает заданное параметром limit количество фильмов с указанной категорией.

    :param category: Категория фильмов,которые необходимо вернуть. enum-поле, описание возможных значений в схеме
    :param limit: Количество строк,которые необходимо вернуть, по умолчанию 10.
    :param db:  Подключение к базе данных
    :return: Лист сущностей FIlmGet, в текущей реализации это все поля таблицы.
    """
    response = db.query(Film.film_id, Film.title,Film.release_year, Film.length, Film.rating, Film.description, Film.special_features,
                        Film.rental_rate, Film.rental_duration).join(FilmCategory).join(Category).filter(
        Category.name == category.value).limit(limit).all()
    return response


@app.get("/film/by-title", response_model=List[FilmGet])
def get_film_by_name(title: Annotated[str, Query()], limit: int = 10, db=Depends(get_db)):
    """
    Вернет фильм с указанным в query названием

    :param title: Название фильма
    :param limit: Количество строк,которые необходимо вернуть, по умолчанию 10.
    :param db:  Подключение к базе данных
    :return: лист FIlmGet, в текущей реализации это все поля таблицы.
    """

    response = db.query(Film.film_id, Film.title,Film.release_year, Film.length, Film.rating, Film.description, Film.special_features,
                        Film.rental_rate, Film.rental_duration).filter(Film.title == title).limit(limit).all()
    return response


@app.get("/film/in-store",response_model=List[FilmGet])
def get_film_in_store(store_id: Annotated[int, Query()], limit: int = 10, db=Depends(get_db)):
    """
    Вернет все фильмы в наличии в магазине по айди магазина

    :param store_id: айди магазина
    :param limit: Количество строк,которые необходимо вернуть, по умолчанию 10.
    :param db:  Подключение к базе данных
    :return: лист FIlmGet, в текущей реализации это все поля таблицы.
    """

    response = db.query(Film.film_id, Film.title,Film.release_year, Film.length, Film.rating, Film.description, Film.special_features,
                        Film.rental_rate, Film.rental_duration).join(Inventory).filter(Inventory.store_id == store_id).limit(limit).all()
    return response


if __name__ == "__main__":
    uvicorn.run(app)
