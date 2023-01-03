from pydantic import BaseModel


class Status(BaseModel):
    strength: float
    dexterity: float
    constitution: float
    intelligence: float
    wisdom: float
    charisma: float
