from pydantic import BaseModel
from typing import Set
from enum import Enum


class Sector(str, Enum):
    alfa = "Alfa"
    bravo = "Bravo"
    charlie = "Charlie"
    delta = "Delta"
    echo = "Echo"
    foxtrot = "Foxtrot"
    golf = "Golf"


class Biomes(str, Enum):
    crimson = "Crimson"
    desert = "Desert"
    forest = "Forest"
    hallow = "Hallow"
    jungle = "Jungle"
    magma = "Magma"
    oasis = "Oasis"
    ocean = "Ocean"
    outpost = "Outpost"
    savannah = "Savannah"
    tundra = "Tundra"


class Coordinates(BaseModel):
    sector: Sector
    x: int
    y: int
    biome: Set[Biomes]
    name: str
