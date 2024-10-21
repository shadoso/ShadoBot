# Standard
from typing import List, Optional

# Third-party
from sqlalchemy import ARRAY, Boolean, String, NUMERIC

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Primes(Base):
    __tablename__ = "primes"

    prime: Mapped[int] = mapped_column(
        NUMERIC,
        primary_key=True,
    )
    happy: Mapped[bool] = mapped_column(Boolean)
    prime_index: Mapped[Optional[int]] = mapped_column(NUMERIC)
    hash_256: Mapped[str] = mapped_column(String(length=64))

class PrimeProducts(Base):
    __tablename__ = "prime_products"

    product: Mapped[int] = mapped_column(
        NUMERIC,
        primary_key=True,
    )
    primes: Mapped[List[int]] = mapped_column(ARRAY(NUMERIC))
    cspp: Mapped[bool] = mapped_column(Boolean) # chained super prime products
    happy: Mapped[bool] = mapped_column(Boolean)
    prime_index: Mapped[Optional[int]] = mapped_column(NUMERIC)
    hash_256: Mapped[str] = mapped_column(String(length=64))

class NoPrimeRelated(Base):
    __tablename__ = "no_prime_related"

    number: Mapped[int] = mapped_column(
        NUMERIC,
        primary_key=True,
    )
    happy: Mapped[bool] = mapped_column(Boolean)
    prime_index: Mapped[Optional[int]] = mapped_column(NUMERIC)
    hash_256: Mapped[str] = mapped_column(String(length=64))