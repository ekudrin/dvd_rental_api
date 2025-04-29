from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA

from db.database import Base


class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address_id = Column(Integer, ForeignKey("address.address_id"), primary_key=True)
    email = Column(String)
    store_id = Column(Integer, ForeignKey("store.store_id"), primary_key=True)
    active = Column(Boolean)
    username = Column(String)
    password = Column(String)
    last_update = Column(TIMESTAMP)
    picture = Column(BYTEA)

