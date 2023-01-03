from essentials_schemas import Status
from pydantic import BaseModel
from enum import Enum


class PetAge(str, Enum):
    young = "Young"
    adult = "Adult"
    teenager = "Teenager"
    elder = "Elder"


class PetRarity(str, Enum):
    common = "Common"
    huge = "Huge"


class PetSpecie(str, Enum):
    common = "Common"
    huge = "Huge"


class Pets(BaseModel):
    name: str
    specie: PetSpecie
    status: Status
    age: PetAge
    rarity: PetRarity
    price: float
