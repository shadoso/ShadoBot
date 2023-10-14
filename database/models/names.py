# Standard
from datetime import date
from typing import List, Optional
import enum

# Third-party
from sqlalchemy import ARRAY, BIGINT, DATE, Enum, ForeignKey, INTEGER, REAL, String

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Gender(enum.Enum):
    female = "Female"
    male = "Male"


class ForenamesGender(Base):
    """
    Gender Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "gender" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    forename : str
        Primary Key and Foreign Key.
    all_incidences: int
        Sum of all incidences.
    highest_odds: Enum
        Most probable gender.
    gender_percentage: float
        Most probable gender percentage.
    jurisdictions: List[str]
        List of countries fullname.
    isos: List[str]
        List of ISO 3166-2.
    genders: List[Enum]
        List of genders.
    percentages: List[float]
        List of percentages.
    incidences: List[int]
        List of incidences.
    created: DATE
        When created, DD/MM/YYYY format.
    last_updated: DATE
        When updated, DD/MM/YYYY format.

    """
    __tablename__ = "forenames_gender"

    forename: Mapped[str] = mapped_column(
        ForeignKey("forenames.forename"),
        primary_key=True,
    )
    all_incidences: Mapped[Optional[int]]
    highest_odds: Mapped[Optional[Gender]] = mapped_column(Enum(Gender))
    gender_percentage: Mapped[Optional[float]]

    jurisdictions: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    isos: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    genders: Mapped[Optional[List[Gender]]] = mapped_column(ARRAY(Enum(Gender)))
    percentages: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[Optional[List[int]]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class ForenamesRegion(Base):
    """
    Region Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "percentages" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    forename : str
        Primary Key and Foreign Key.
    all_incidences: int
        Sum of all incidences.
    jurisdictions: List[str]
        List of countries fullname.
    isos: List[str]
        List of ISO 3166-2.
    percentages: List[float]
        List of percentages.
    incidences: List[int]
        List of incidences.
    created: DATE
        When created, DD/MM/YYYY format.
    last_updated: DATE
        When updated, DD/MM/YYYY format.

    """
    __tablename__ = "forenames_region"

    forename: Mapped[str] = mapped_column(
        ForeignKey("forenames.forename"),
        primary_key=True,
    )
    all_incidences: Mapped[Optional[int]]

    jurisdictions: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    isos: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    percentages: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[Optional[List[int]]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class SurnamesRegion(Base):
    """
    Region Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "percentages" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    surname : str
        Primary Key and Foreign Key.
    all_incidences: int
        Sum of all incidences.
    jurisdictions: List[str]
        List of countries fullname.
    isos: List[str]
        List of ISO 3166-2.
    percentages: List[float]
        List of percentages.
    incidences: List[int]
        List of incidences.
    created: DATE
        When created, DD/MM/YYYY format.
    last_updated: DATE
        When updated, DD/MM/YYYY format.

    """
    __tablename__ = "surnames_region"

    surname: Mapped[str] = mapped_column(
        ForeignKey("surnames.surname"),
        primary_key=True,
    )
    all_incidences: Mapped[Optional[int]]

    jurisdictions: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    isos: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
    percentages: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[Optional[List[int]]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class Forenames(Base):
    """
    Forenames Table

    Notes ----- Rate serves two main purposes: it helps assess the accuracy of the data and measures the popularity
    of a name (how many people have this name). Higher values indicate better quality.

    Attributes
    ----------
    forename : str
        Primary Key.
    rate: int
        Sum of Region + Gender table.
    region: ForenamesRegion
        Relationship with table ForenamesRegion.
    gender: ForenamesGender
        Relationship with table ForenamesGender.
    created: DATE
        When created, DD/MM/YYYY format.
    last_updated: DATE
        When updated, DD/MM/YYYY format.

    """
    __tablename__ = "forenames"

    forename: Mapped[str] = mapped_column(
        String(length=16),
        primary_key=True
    )
    rate: Mapped[Optional[int]] = mapped_column(BIGINT)

    region: Mapped["ForenamesRegion"] = relationship(
        back_populates="forenames",
        cascade="all, delete-orphan"
    )

    gender: Mapped["ForenamesGender"] = relationship(
        back_populates="forenames",
        cascade="all, delete-orphan"
    )

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class Surnames(Base):
    """
    Surnames Table

    Notes ----- Rate serves two main purposes: it helps assess the accuracy of the data and measures the popularity
    of a surname (how many people have this surname). Higher values indicate better quality.

    Attributes
    ----------
    surname : str
        Primary Key.
    rate: int
        Sum of all incidences.
    region: SurnamesRegion
        Relationship with table SurnamesRegion.
    created: DATE
        When created, DD/MM/YYYY format.
    last_updated: DATE
        When updated, DD/MM/YYYY format.

    """
    __tablename__ = "surnames"

    surname: Mapped[str] = mapped_column(
        String(length=16),
        primary_key=True
    )
    rate: Mapped[Optional[int]] = mapped_column(BIGINT)

    region: Mapped["SurnamesRegion"] = relationship(
        back_populates="surnames",
        cascade="all, delete-orphan"
    )

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)
