

from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum

from db.database import Base
from enums import FilmCategoryEnum


class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    name = Column(Enum(FilmCategoryEnum))
    last_update = Column(TIMESTAMP)

