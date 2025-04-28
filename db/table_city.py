from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Store(Base):
    __tablename__ = "city"
    city_id = Column(Integer, primary_key=True)
    city = Column(String)
    country_id = Column(Integer, ForeignKey("country.country_id"), primary_key=True)
    last_update = Column(TIMESTAMP)
    country = relationship("Country")
