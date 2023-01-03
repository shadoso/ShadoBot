from essentials_schemas import Status
from pydantic import BaseModel
from enum import Enum


class WeaponRarity(str, Enum):
    common = "Common"
    uncommon = "Uncommon"
    rare = "Rare"
    epic = "Epic"
    legendary = "Legendary"


class WeaponStyle(str, Enum):
    ranged = "Ranged"
    melee = "Melee"
    summoner = "Summoner"


class Pets(BaseModel):
    name: str
    status: Status
    style: WeaponStyle
    damage: float
    crit_rate: float
    rarity: WeaponRarity
    price: float
