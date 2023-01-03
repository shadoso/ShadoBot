from enum import Enum


class Country(str, Enum):
    brazil = "Brazil"
    france = "France"
    japan = "Japan"
    philippines = "Philippines"
    russia = "Russia"
    spain = "Spain"
    usa = "USA"


class Gender(str, Enum):
    female = "Female"
    male = "Male"


class Verification(str, Enum):
    valid = "Valid"
    unknown = "Unknown"
