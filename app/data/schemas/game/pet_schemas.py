from pydantic import BaseModel
from enum import Enum


class PetType(str, Enum):
    ancient = "Ancient"
    anemo = "Anemo"
    aqua = "Aqua"
    bug = "Bug"
    cryo = "Cryo"
    dragon = "Dragon"
    electro = "Electro"
    fairy = "Fairy"
    machine = "Machine"
    common = "Common"
    phantom = "Phantom"
    plant = "Plant"
    plasma = "Plasma"
    pyro = "Pyro"
    quantum = "Quantum"
    virtual = "Virtual"
    void = "Void"
    kaiju = "Kaiju"


class Pets(BaseModel):
    name: str
    types: list[PetType]
    price: float
    pet_id: int
