from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Store(Base):
    __tablename__ = "address"
    address_id = Column(Integer, primary_key=True)
    address = Column(String)
    address2 = Column(String)
    district = Column(String)
    city_id = Column(Integer, ForeignKey("city.city_id"), primary_key=True)
    postal_code = Column(String)
    phone = Column(String)
    last_update = Column(TIMESTAMP)
    city = relationship("City")
    customer = relationship("Customer")
