from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Inventory(Base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey("film.film_id"), primary_key=True)
    store_id = Column(Integer, ForeignKey("store.store_id"), primary_key=True)
    last_update = Column(TIMESTAMP)
    film = relationship("Film")
    store = relationship("Store")
