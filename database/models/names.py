# Standard
from datetime import date
from typing import List, Optional
import enum

# Third-party
from sqlalchemy import ARRAY, BIGINT, DATE, Enum, ForeignKey, INTEGER, REAL, SMALLINT, String

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Gender(enum.Enum):
    female = "Female"
    male = "Male"


class OwnerForenamesGender(Base):
    """
    Gender Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "gender" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    forename : str
        Primary Key and Foreign Key.
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
        When created.
    last_updated: DATE
        When updated.
    """
    __tablename__ = "owner_forenames_gender"

    owner_id: Mapped[int] = mapped_column(ForeignKey("forenames.id"))
    forename: Mapped[str] = mapped_column(primary_key=True)

    jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
    isos: Mapped[List[str]] = mapped_column(ARRAY(String))
    genders: Mapped[List[Gender]] = mapped_column(ARRAY(Enum(Gender)))
    percentages: Mapped[List[float]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class OwnerForenamesRegion(Base):
    """
    Region Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "percentages" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    forename : str
        Primary Key and Foreign Key.
    jurisdictions: List[str]
        List of countries fullname.
    isos: List[str]
        List of ISO 3166-2.
    percentages: List[float]
        List of percentages.
    incidences: List[int]
        List of incidences.
    created: DATE
        When created.
    last_updated: DATE
        When updated.
    """
    __tablename__ = "owner_forenames_region"

    owner_id: Mapped[int] = mapped_column(ForeignKey("forenames.id"))
    forename: Mapped[str] = mapped_column(primary_key=True)

    jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
    isos: Mapped[List[str]] = mapped_column(ARRAY(String))
    percentages: Mapped[List[float]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


class OwnerSurnamesRegion(Base):
    """
    Region Table

    Notes ----- All ARRAY-type elements are interconnected. For example, the first element in "jurisdiction" and
    "percentages" belongs to the same group, and this applies to other ARRAYS as well.

    Attributes
    ----------
    surname : str
        Primary Key and Foreign Key.
    jurisdictions: List[str]
        List of countries fullname.
    isos: List[str]
        List of ISO 3166-2.
    percentages: List[float]
        List of percentages.
    incidences: List[int]
        List of incidences.
    created: DATE
        When created.
    last_updated: DATE
        When updated.
    """
    __tablename__ = "owner_surnames_region"

    owner_id: Mapped[int] = mapped_column(ForeignKey("surnames.id"))
    surname: Mapped[str] = mapped_column(primary_key=True)

    jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
    isos: Mapped[List[str]] = mapped_column(ARRAY(String))
    percentages: Mapped[List[float]] = mapped_column(ARRAY(REAL))
    incidences: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))

    created: Mapped[date] = mapped_column(DATE)
    last_updated: Mapped[date] = mapped_column(DATE)


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
    last_updated: DATE
        When updated.
    """
    __tablename__ = "forenames_gender"

    forename: Mapped[str] = mapped_column(
        ForeignKey("forenames.forename"),
        primary_key=True
    )

    all_incidences: Mapped[int] = mapped_column(BIGINT)
    highest_odds: Mapped[Gender] = mapped_column(Enum(Gender))
    gender_percentage: Mapped[float] = mapped_column(REAL)

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
    last_updated: DATE
        When updated.

    """
    __tablename__ = "forenames_region"

    forename: Mapped[str] = mapped_column(
        ForeignKey("forenames.forename"),
        primary_key=True
    )

    all_incidences: Mapped[int] = mapped_column(BIGINT)
    variations: Mapped[List[str]] = mapped_column(ARRAY(String))
    similarity: Mapped[List[float]] = mapped_column(ARRAY(REAL))

    jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
    isos: Mapped[List[str]] = mapped_column(ARRAY(String))
    percentages: Mapped[List[float]] = mapped_column(ARRAY(REAL))

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
    last_updated: DATE
        When updated.

    """
    __tablename__ = "surnames_region"

    surname: Mapped[str] = mapped_column(
        ForeignKey("surnames.surname"),
        primary_key=True
    )

    all_incidences: Mapped[int] = mapped_column(BIGINT)
    variations: Mapped[List[str]] = mapped_column(ARRAY(String))
    similarity: Mapped[List[float]] = mapped_column(ARRAY(REAL))

    jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
    isos: Mapped[List[str]] = mapped_column(ARRAY(String))
    percentages: Mapped[List[float]] = mapped_column(ARRAY(REAL))

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
        Smallint value range 0 - 10.
    rate_description:
        Description of rate value may auto or manual.
    region: ForenamesRegion
        Relationship with table ForenamesRegion.
    gender: ForenamesGender
        Relationship with table ForenamesGender.
    last_updated: DATE
        When updated.

    """
    __tablename__ = "forenames"

    id: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        autoincrement=True,
        unique=True
    )
    forename: Mapped[str] = mapped_column(
        String(length=20),
        primary_key=True
    )
    rate: Mapped[Optional[int]] = mapped_column(SMALLINT)
    rate_description: Mapped[Optional[str]] = mapped_column(String(length=128))

    region: Mapped["ForenamesRegion"] = relationship(cascade="all, delete-orphan")

    gender: Mapped["ForenamesGender"] = relationship(cascade="all, delete-orphan")

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
        Smallint value range 0 - 10.
    rate_description:
        Description of rate value may auto or manual.
    region: SurnamesRegion
        Relationship with table SurnamesRegion.
    last_updated: DATE
        When updated.

    """
    __tablename__ = "surnames"

    id: Mapped[Optional[int]] = mapped_column(
        INTEGER,
        autoincrement=True,
        unique=True
    )
    surname: Mapped[str] = mapped_column(
        String(length=22),
        primary_key=True
    )
    rate: Mapped[Optional[int]] = mapped_column(SMALLINT)
    rate_description: Mapped[Optional[str]] = mapped_column(String(length=128))

    region: Mapped["SurnamesRegion"] = relationship(cascade="all, delete-orphan")

    last_updated: Mapped[date] = mapped_column(DATE)
