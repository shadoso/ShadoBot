from sqlalchemy import Column, Enum, String, ARRAY, Numeric, DateTime, Integer
from app.data.data_types import Gender, Country, Verification
from app.data.schemas.game.coordinates_schemas import Biomes, Sector
from app.data.session import Base, engine


class Names(Base):
    __tablename__ = 'names'

    name = Column(String, nullable=False, primary_key=True)
    gender = Column(Enum(Gender), nullable=False, primary_key=True)
    country = Column(Enum(Country), nullable=False, primary_key=True)
    verification = Column(Enum(Verification), nullable=False)


class Surnames(Base):
    __tablename__ = 'surnames'

    surname = Column(String, nullable=False, primary_key=True)
    verification = Column(Enum(Verification), nullable=False)
    country = Column(Enum(Country), nullable=False, primary_key=True)


class Universe(Base):
    __tablename__ = 'universe'

    sector = Column(Enum(Sector), nullable=False, primary_key=True)
    x = Column(Integer, nullable=False, primary_key=True)
    y = Column(Integer, nullable=False, primary_key=True)
    biome = Column(ARRAY(item_type=Biomes, as_tuple=True), nullable=False, primary_key=True)
    name = Column(String, nullable=False, primary_key=True)


class Community(Base):
    __tablename__ = 'community'

    id = Column(String, nullable=False, primary_key=True)
    description = Column(String(256), nullable=False)
    # coordinates = Column(JSON, nullable=False)
    # inventory = Column(JSON, nullable=True)
    # buffs = Column(JSON, nullable=False)
    coins = Column(Numeric(precision=9, scale=2), nullable=False)
    daily = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    # collectables = Column(JSON, nullable=False)


Base.metadata.create_all(bind=engine)
