import datetime
from typing import List
from pydantic import BaseModel


class FilmGet(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int
    rental_duration: int
    rental_rate: float
    length: int
    rating: str
    special_features: List

    class Config:
        orm_mode = True


class FilmInStoreGet(BaseModel):
    inventory_id: int

    class Config:
        orm_mode = True


class CustomerGet(BaseModel):
    customer_id: int

    class Config:
        orm_mode = True
