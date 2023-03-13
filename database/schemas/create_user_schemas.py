from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.data.schemas.game.pet_schemas import Pets
from enum import Enum


class Currency(BaseModel):
    dust: int
    scrap: int
    crystals: int
    tech: int
    core: int


class Collectables(BaseModel):
    cards: list[int]
    capsules: list[int]
    stamps: list[int]


class Inventory(BaseModel):
    currency: Currency
    collectables: Collectables
    pets: Optional[list[int]]
    items: Optional[list[int]]
    weapons: Optional[list[int]]


class Buffs(BaseModel):
    luck: float
    entropy: float
    knowledge: list[int]
    size: int


class CreateUser(BaseModel):
    id: str
    name: str
    description: str = ":D"
    inventory: Optional[Inventory]
    buffs: Buffs
    coins: float = 99.45
    daily: datetime = datetime.now()
    created: datetime = datetime.now()

    class Config:
        orm_mode = True
