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


class FakeAuthReq(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class FakeAuthResp(BaseModel):
    staff_id: int
    first_name: str
    last_name: str
    email: str
    store_id: int


class RentReq(BaseModel):
    inventory_id: int
    customer_id: int
    return_duration: int
    staff_id: int

    class Config:
        orm_mode = True


class RentResp(BaseModel):
    rental_id: int

    class Config:
        orm_mode = True


class PaymentReq(BaseModel):
    customer_id: int
    staff_id: int
    rental_id: int
    amount: float

    class Config:
        orm_mode = True
