from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Set
from app.data.schemas.game.pet_schemas import Pets
from enum import Enum


class Inventory(BaseModel):
    pets: Optional[List[Pets]]
    itens: str
    weapons: str


class Buffs(BaseModel):
    luck: float
    size: int


class Collectables(BaseModel):
    dust: int
    scrap: int
    crystals: int
    tech: int
    core: int


class CreateUser(BaseModel):
    id: str
    description: str = ":D"
    # coordinates: Coordinates
    # inventory: Optional[Inventory]
    # buffs: Buffs
    coins: float = 99.45
    daily: datetime = datetime.now()
    created: datetime = datetime.now()

    # collectables: Collectables

    class Config:
        orm_mode = True
