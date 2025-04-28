import datetime
from typing import List
from pydantic import BaseModel


class FilmGet(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int
    language_id: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    rating: str
    last_update: datetime.datetime
    special_features: List
    fulltext: str

    class Config:
        orm_mode = True


# Одно и то же с FilmGet
# или убрать совсем или сделать разницу между ответами запросов(убрать добавить поля)
# Повторить для всех эндпоинтов получения фильма(ов)
class FilmByCategoryGet(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int
    language_id: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    rating: str
    last_update: datetime.datetime
    special_features: List
    fulltext: str

    class Config:
        orm_mode = True
