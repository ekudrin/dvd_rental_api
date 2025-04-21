from sqlalchemy import Column, Integer, String, TIMESTAMP

from db.database import Base


class Film(Base):
    __tablename__ = "film"
    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    release_year = Column(Integer)
    language_id = Column(Integer)
    rental_duration = Column(Integer)
    rental_rate = Column(Integer)
    length = Column(Integer)
    replacement_cost = Column(Integer)
    rating = Column(String)
    last_update = Column(TIMESTAMP)
    special_features = Column(String)
    fulltext = Column(String)
