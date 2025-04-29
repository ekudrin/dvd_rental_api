from datetime import datetime, timedelta
from typing import Annotated
from typing import List

import uvicorn
from fastapi import FastAPI, Depends, Query, HTTPException

from db.database import SessionLocal
from db.table_film import Film
from enums import FilmCategoryEnum
from schema import FilmGet, FilmInStoreGet, CustomerGet, FakeAuthReq, FakeAuthResp, RentReq, RentResp, PaymentReq, \
    FilmCheckInStoreGet
from table_category import Category
from table_customer import Customer
from table_film_category import FilmCategory
from table_inventory import Inventory
from table_payment import Payment
from table_rental import Rental
from table_staff import Staff

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/film", response_model=List[FilmGet])
def get_all_films(title: str | None = None, category: FilmCategoryEnum | None = None, limit: int = 10,
                  db=Depends(get_db)):
    query = db.query(Film.film_id, Film.title, Category.name, Film.release_year, Film.length, Film.rating,
                     Film.description,
                     Film.special_features,
                     Film.rental_rate, Film.rental_duration).select_from(Film).join(FilmCategory).join(Category)
    if title is not None:
        query = query.filter(Film.title == title)
    if category is not None:
        query = query.filter(Category.name == category.value)

    response = query.limit(limit).all()

    return response


@app.get("/film/in-store", response_model=List[FilmInStoreGet])
def get_film_in_store(store_id: int, limit: int = 10, db=Depends(get_db)):
    """
    Вернет все фильмы в наличии в магазине по айди магазина
    формат ответа отличается от обычного формата фильмов,т.к. придется джойнить ещё  2 таблицы чтобы получить категорию,
    кажется что наличие фильма в магазине можно узнать и не уточняя категорию

    :param store_id: айди магазина
    :param limit: Количество строк,которые необходимо вернуть, по умолчанию 10.
    :param db:  Подключение к базе данных
    :return: Лист объектов с  айди фильма, названием фильма и ценой аренды
    """

    response = db.query(Film.film_id, Film.title, Film.length,
                        Film.rental_rate).join(Inventory).filter(
        Inventory.store_id == store_id).limit(limit).all()
    return response


@app.get("/film/check-in-store", response_model=List[FilmCheckInStoreGet])
def check_film_in_store(film_id: int, store_id: int, db=Depends(get_db)):
    """
    Возвращает айди товара(ов) на складе если они в наличии в магазине
    :param film_id: айди фильма
    :param store_id: айди магазина
    :param db: подключение к бд
    :return: список айди товаров если есть, текст ошибки если в магазине нет фильма в наличии
    """
    response = db.query(Inventory.inventory_id).filter(
        (Inventory.film_id == film_id) & (Inventory.store_id == store_id)).all()
    if len(response):
        return response
    else:
        raise HTTPException(status_code=404, detail="Film not found in store")


@app.get("/customer", response_model=CustomerGet)
def get_customer_id(first_name: Annotated[str, Query()], last_name: Annotated[str, Query()], db=Depends(get_db)):
    """
    Возвращает айди клиента по имени и фамилии
    :param first_name: Имя
    :param last_name: Фамилия
    :param db: подключение к бд
    :return: айди клиента
    """
    response = db.query(Customer).filter(
        (Customer.first_name == first_name) & (Customer.last_name == last_name)).first()
    if response is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return response


@app.post("/fake-auth/", response_model=FakeAuthResp)
def fake_auth(user: FakeAuthReq, db=Depends(get_db)):
    """
    временное( ;) ) решение по авторизации пользователя, для получения информации по айди магазина и айди сотрудника

    :param user: тело запроса, должно содержать поля username  и password
    :param db: подключение к бд
    :return: айди пользователя и айди магазина
    """
    response = db.query(Staff.staff_id, Staff.first_name, Staff.last_name, Staff.email, Staff.store_id).filter(
        (Staff.username == user.username) & (Staff.password == user.password)).first()
    if response is None:
        raise HTTPException(status_code=403, detail="Incorrect username or password")
    return response


@app.post("/rent", response_model=RentResp)
def post_rental(rent_info: RentReq, db=Depends(get_db)):
    """
    эндпоинт для аренды dvd,
     в запросе передается информация необходимая для аренды(клиент, что берет, кто проводит операцию),
      в ответе  айди аренды

    :param rent_info: класс с полями айди товара, айди клиента, время аренды, айди сотрудника
    :param db:подключение  к бд
    :return:  айди созданной аренды
    """
    rental_date = datetime.now()
    return_date = rental_date + timedelta(days=rent_info.return_duration)
    new_rent = Rental(rental_date=rental_date, inventory_id=rent_info.inventory_id, customer_id=rent_info.customer_id,
                      return_date=return_date, staff_id=rent_info.staff_id, last_update=rental_date)
    db.add(new_rent)
    db.commit()
    db.refresh(new_rent)
    return {"rental_id": new_rent.rental_id}


@app.post("/payment")
def post_payment(payment_info: PaymentReq, db=Depends(get_db)):
    """
    создает запись о проведенной оплате,
    для упрощения процесса передается  сумма как факт оплаты,
     без расчета стоимости и учета  было ли этого достаточно
    :return:
    """
    payment_date = datetime.now()
    new_payment = Payment(customer_id=payment_info.customer_id, staff_id=payment_info.staff_id,
                          rental_id=payment_info.rental_id, amount=payment_info.amount, payment_date=payment_date)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return {"payment_id": new_payment.payment_id}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
