from dataclasses import dataclass


@dataclass(slots=True)
class CreateCountry:
    id: int
    entity: str
    continent: str
    alpha_2_code: str
    alpha_3_code: str
    country_code: int