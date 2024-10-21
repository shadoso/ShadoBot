# Third-party
from sqlalchemy import Identity, String, SMALLINT

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Countries(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(
        SMALLINT,
        Identity(start=1),
        primary_key=True,
    )
    entity: Mapped[str] = mapped_column(
        String(length=64),
        unique=True
    )
    continent: Mapped[str] = mapped_column(String(length=13))
    alpha_2_code: Mapped[str] = mapped_column(
        String(length=2),
        unique=True
    )
    alpha_3_code: Mapped[str] = mapped_column(
        String(length=3),
        unique=True
    )
    country_code: Mapped[int] = mapped_column(
        SMALLINT,
        unique=True
    )
