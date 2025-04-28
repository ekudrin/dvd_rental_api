from sqlalchemy import Column, Integer, String, TIMESTAMP

from db.database import Base


class Store(Base):
    __tablename__ = "country"
    country_id = Column(Integer, primary_key=True)
    country = Column(String)
    last_update = Column(TIMESTAMP)
