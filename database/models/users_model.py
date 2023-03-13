from sqlalchemy import Column, ARRAY, SmallInteger, String, Numeric, DateTime, REAL
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.data.session import Base
from sqlalchemy.ext.mutable import MutableDict


class Collectables(Base):
    __tablename__ = 'collectables'

    user_id = Column(String, ForeignKey('profiles.user_id', ondelete="CASCADE"), primary_key=True)
    cards = Column(ARRAY(SmallInteger), nullable=True)
    capsules = Column(ARRAY(SmallInteger), nullable=True)
    stamps = Column(ARRAY(SmallInteger), nullable=True)
    codex = Column(ARRAY(SmallInteger), nullable=True)
    knowledge = Column(ARRAY(SmallInteger), nullable=True)


class Inventory(Base):
    __tablename__ = 'inventory'

    user_id = Column(String, ForeignKey('profiles.user_id', ondelete="CASCADE"), primary_key=True)
    loot = Column(MutableDict.as_mutable(JSONB), nullable=True)
    dust = Column(Numeric(precision=6, scale=2), nullable=True)
    crystals = Column(SmallInteger, nullable=True)
    scrap = Column(Numeric(precision=6, scale=2), nullable=True)
    tech = Column(SmallInteger, nullable=True)
    core = Column(SmallInteger, nullable=True)


class Timer(Base):
    __tablename__ = 'timer'

    user_id = Column(String, ForeignKey('profiles.user_id', ondelete="CASCADE"), primary_key=True)
    daily_timer = Column(DateTime, nullable=False)
    discovering_timer = Column(DateTime, nullable=False)
    looting_timer = Column(DateTime, nullable=False)


class StarShip(Base):
    __tablename__ = 'starship'

    user_id = Column(String, ForeignKey('profiles.user_id', ondelete="CASCADE"), primary_key=True)
    planet_id = Column(String(length=16), ForeignKey('planets.planet_id'), nullable=True)
    ship_type = Column(SmallInteger, nullable=True)
    ship_upgrades = Column(ARRAY(SmallInteger), nullable=True)
    gadgets = Column(ARRAY(SmallInteger), nullable=True)

    planet = relationship("Planets", backref="starships")


class Profiles(Base):
    __tablename__ = 'profiles'

    user_id = Column(String, nullable=False, primary_key=True)
    description = Column(String(156), nullable=False)
    coins = Column(Numeric(precision=11, scale=2), nullable=False)
    luck = Column(REAL, nullable=False)
    house = Column(SmallInteger, nullable=True)
    tags = Column(ARRAY(SmallInteger), nullable=True)
    created = Column(DateTime, nullable=False)

    timer = relationship("Timer", backref="profiles", uselist=False)
    inventory = relationship("Inventory", backref="profiles", uselist=False)
    starship = relationship("StarShip", backref="profiles", uselist=False)
    collectables = relationship("Collectables", backref="profiles", uselist=False)
