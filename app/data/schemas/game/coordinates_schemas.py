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
    hotel = "Hotel"
    india = "India"
    juliet = "Juliet"
    kilo = "Kilo"
    lima = "Lima"
    mike = "Mike"
    november = "November"
    oscar = "Oscar"
    papa = "Papa"
    quebec = "Quebec"
    romeo = "Romeo"
    sierra = "Sierra"
    tango = "Tango"
    uniform = "Uniform"
    victor = "Victor"
    whiskey = "Whiskey"
    xray = "Xray"
    yankee = "Yankee"
    zulu = "Zulu"


class SystemNames(str, Enum):
    alpha = "Alpha"
    beta = "Beta"
    gamma = "Gamma"
    delta = "Delta"
    epsilon = "Epsilon"
    zeta = "Zeta"
    eta = "Eta"
    theta = "Theta"
    iota = "Iota"
    kappa = "Kappa"
    ligma = "Ligma"
    mu = "Mu"
    nu = "Nu"
    xi = "Xi"
    omicron = "Omicron"
    pi = "Pi"
    rho = "Rho"
    sigma = "Sigma"
    tau = "Tau"
    upsilon = "Upsilon"
    phi = "Phi"
    chi = "Chi"
    psi = "Psi"
    omega = "Omega"


class Coordinates(BaseModel):
    sector: Sector
    biome: int
    name: str
