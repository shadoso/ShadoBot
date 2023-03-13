from sqlalchemy import Column, ARRAY, SmallInteger, Integer, Boolean, String
from app.data.session import Base


class Planets(Base):
    __tablename__ = 'planets'

    planet_id = Column(String(length=16), nullable=False, primary_key=True)
    sector = Column(SmallInteger, nullable=False)
    name = Column(SmallInteger, nullable=False)
    surname = Column(SmallInteger, nullable=False)
    trait = Column(SmallInteger, nullable=False)
    hex_id = Column(Integer, nullable=False)
    roman = Column(SmallInteger, nullable=False)
    galaxy = Column(SmallInteger, nullable=False)
    biomes = Column(ARRAY(SmallInteger), nullable=False)
    official = Column(Boolean, nullable=False)
    available = Column(Boolean, nullable=False)
