from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class FilmCategory(Base):
    __tablename__ = "film_category"
    film_id = Column(Integer, ForeignKey("film.film_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("category.category_id"), primary_key=True)
    last_update = Column(TIMESTAMP)
    film = relationship("Film")
    category = relationship("Category")
