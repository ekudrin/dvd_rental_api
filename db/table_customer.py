from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship

from db.database import Base


class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("store.store_id"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address_id = Column(Integer, ForeignKey("address.address_id"), primary_key=True)
    activebool = Column(Boolean)
    create_date = Column(Date)
    last_update = Column(TIMESTAMP)
    active = Column(Integer)
