# Third-party
from sqlalchemy import Identity, INTEGER, String

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Names(Base):
    __tablename__ = "names"

    id: Mapped[int] = mapped_column(
        INTEGER,
        Identity(start=1),
        primary_key=True,
    )
    forename: Mapped[str] = mapped_column(
        String(length=20),
        unique=True
    )

# EDIT

# class Forenames(Base):
#     __tablename__ = "forenames"
#
#     id: Mapped[int] = mapped_column(
#         INTEGER,
#         Identity(start=1),
#         unique=True,
#     )
#     forename: Mapped[str] = mapped_column(
#         String(length=20),
#         primary_key=True
#     )
#
#     variations: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String(length=20)))
#     similarity: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
#
#     rate: Mapped[Optional[int]] = mapped_column(SMALLINT)
#     description: Mapped[Optional[str]] = mapped_column(String(length=64))
#
#     incidence: Mapped[Optional[int]] = mapped_column(BIGINT)
#     continents: Mapped[Optional[List[Continent]]] = mapped_column(ARRAY(Enum(Continent)))
#     partition: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
#
#     iso_list: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String(length=6)))
#     jurisdiction_list: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
#     sample_list: Mapped[Optional[List[int]]] = mapped_column(ARRAY(INTEGER))
#
#     gender_list: Mapped[Optional[List[Gender]]] = mapped_column(ARRAY(Enum(Gender)))
#     gender_odds: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
#
#     created: Mapped[date] = mapped_column(DATE)
#     last_updated: Mapped[date] = mapped_column(DATE)
#
#
# class Surnames(Base):
#     __tablename__ = "surnames"
#
#     id: Mapped[int] = mapped_column(
#         INTEGER,
#         Identity(start=1),
#         unique=True,
#     )
#     surname: Mapped[str] = mapped_column(
#         String(length=22),
#         primary_key=True
#     )
#
#     variations: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String(length=22)))
#     similarity: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
#
#     rate: Mapped[Optional[int]] = mapped_column(SMALLINT)
#     description: Mapped[Optional[str]] = mapped_column(String(length=64))
#
#     incidence: Mapped[Optional[int]] = mapped_column(BIGINT)
#     continents: Mapped[Optional[List[Continent]]] = mapped_column(ARRAY(Enum(Continent)))
#     partition: Mapped[Optional[List[float]]] = mapped_column(ARRAY(REAL))
#
#     iso_list: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String(length=6)))
#     jurisdiction_list: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))
#     sample_list: Mapped[Optional[List[int]]] = mapped_column(ARRAY(INTEGER))
#
#     created: Mapped[date] = mapped_column(DATE)
#     last_updated: Mapped[date] = mapped_column(DATE)
#
#
# class ForenamesDetails(Base):
#     __tablename__ = "forenames_details"
#
#     owner_id: Mapped[int] = mapped_column(ForeignKey("forenames.id"))
#     forename: Mapped[str] = mapped_column(
#         String(length=20),
#         primary_key=True
#     )
#
#     region_isos: Mapped[List[str]] = mapped_column(ARRAY(String(length=6)))
#     region_jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
#     region_samples: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))
#
#     gender_isos: Mapped[List[str]] = mapped_column(ARRAY(String(length=6)))
#     gender_jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
#     gender_list: Mapped[List[Gender]] = mapped_column(ARRAY(Enum(Gender)))
#     gender_odds: Mapped[List[float]] = mapped_column(ARRAY(REAL))
#     gender_samples: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))
#
#     created: Mapped[date] = mapped_column(DATE)
#     last_updated: Mapped[date] = mapped_column(DATE)
#
#
# class SurnamesDetails(Base):
#     __tablename__ = "surnames_details"
#
#     owner_id: Mapped[int] = mapped_column(ForeignKey("surnames.id"))
#     surname: Mapped[str] = mapped_column(
#         String(length=22),
#         primary_key=True
#     )
#
#     region_isos: Mapped[List[str]] = mapped_column(ARRAY(String(length=6)))
#     region_jurisdictions: Mapped[List[str]] = mapped_column(ARRAY(String))
#     region_samples: Mapped[List[int]] = mapped_column(ARRAY(INTEGER))
#
#     created: Mapped[date] = mapped_column(DATE)
#     last_updated: Mapped[date] = mapped_column(DATE)
