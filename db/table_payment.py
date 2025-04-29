from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.database import Base


class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), primary_key=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), primary_key=True)
    rental_id = Column(Integer, ForeignKey("rental.rental_id"), primary_key=True)
    amount = Column(Float)
    payment_date = Column(TIMESTAMP)
    rental = relationship("Rental")
    customer = relationship("Customer")
    staff = relationship("Staff")
