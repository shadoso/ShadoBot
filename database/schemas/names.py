from typing import Optional, List
from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True, slots=True)
class CreateBaseModel:
    created: Optional[date] = None
    last_updated: Optional[date] = None

    def __post_init__(self):
        self.created = date.today()
        self.last_updated = date.today()


@dataclass(kw_only=True, slots=True)
class CreateForename(CreateBaseModel):
    forename: str


@dataclass(kw_only=True, slots=True)
class CreateForenameGender(CreateForename):
    pass


@dataclass(kw_only=True, slots=True)
class CreateForenameRegion(CreateForename):
    pass


@dataclass(kw_only=True, slots=True)
class CreateSurname(CreateBaseModel):
    surname: str


@dataclass(kw_only=True, slots=True)
class CreateSurnameRegion(CreateSurname):
    pass


@dataclass(kw_only=True, slots=True)
class UpdateBaseModel:
    all_incidences: int

    jurisdictions: List[str]
    isos: List[str]
    percentages: List[float]
    incidences: List[int]

    created: date
    last_updated: Optional[date] = None

    def __post_init__(self):
        self.last_updated = date.today()


@dataclass(kw_only=True, slots=True)
class UpdateForenameGender:
    pass


@dataclass(kw_only=True, slots=True)
class UpdateForenameBaseModel(UpdateBaseModel):
    forename: str


@dataclass(kw_only=True, slots=True)
class UpdateSurnameBaseModel(UpdateBaseModel):
    surname: str
