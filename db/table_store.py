from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Store(Base):
    __tablename__ = "store"
    store_id = Column(Integer, primary_key=True)
    manager_staff_id = Column(Integer, ForeignKey("staff.staff_id"), primary_key=True)
    address_id = Column(Integer, ForeignKey("address.address_id"), primary_key=True)
    last_update = Column(TIMESTAMP)
    staff = relationship("Staff")
    address = relationship("Address")

