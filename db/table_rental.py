from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA

from db.database import Base


class Rental(Base):
    __tablename__ = "rental"
    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    rental_date = Column(TIMESTAMP)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), primary_key=True)
    return_date = Column(TIMESTAMP)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), primary_key=True)
    last_update = Column(TIMESTAMP)
    inventory = relationship("Inventory")
    customer = relationship("Customer")
    staff = relationship("Staff")
