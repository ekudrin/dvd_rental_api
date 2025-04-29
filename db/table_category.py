

from sqlalchemy import Column, Integer, TIMESTAMP, String

from db.database import Base


class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    last_update = Column(TIMESTAMP)

