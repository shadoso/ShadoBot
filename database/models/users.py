# Standard
from datetime import date
from typing import List

# Third-party
from sqlalchemy import ARRAY, BIGINT, Boolean, DATE, ForeignKey, INTEGER, JSON, REAL, SMALLINT, String, Identity, TEXT

from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Actions(Base):
    __tablename__ = "actions"

    id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.discord_id"),
        primary_key=True
    )

    commands: Mapped[dict] = mapped_column(JSON)
    limiter: Mapped[List[int]] = mapped_column(ARRAY(SMALLINT))
    luck: Mapped[float] = mapped_column(REAL)
    tier: Mapped[int] = mapped_column(SMALLINT)

    daily: Mapped[date] = mapped_column(DATE)
    timer: Mapped[date] = mapped_column(DATE)


class Backpack(Base):
    __tablename__ = "backpack"

    id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.discord_id"),
        primary_key=True
    )

    dusts: Mapped[int] = mapped_column(SMALLINT)
    shards: Mapped[int] = mapped_column(SMALLINT)
    souls: Mapped[int] = mapped_column(SMALLINT)
    techs: Mapped[int] = mapped_column(SMALLINT)
    cores: Mapped[int] = mapped_column(SMALLINT)

    inventory: Mapped[dict] = mapped_column(
        JSON
    )


class Buddies(Base):
    __tablename__ = "buddies"

    id: Mapped[int] = mapped_column(
        SMALLINT,
        Identity(start=1),
        unique=True,
    )
    width: Mapped[int] = mapped_column(SMALLINT)
    height: Mapped[int] = mapped_column(SMALLINT)
    url: Mapped[str] = mapped_column(TEXT)


class Collectables(Base):
    __tablename__ = "collectables"

    id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.discord_id"),
        primary_key=True
    )

    # Max index size 512
    cards: Mapped[List[bool]] = mapped_column(ARRAY(Boolean))
    banners: Mapped[List[bool]] = mapped_column(ARRAY(Boolean))
    buddies: Mapped[List[bool]] = mapped_column(ARRAY(Boolean))
    secrets: Mapped[List[bool]] = mapped_column(ARRAY(Boolean))
    tags: Mapped[List[bool]] = mapped_column(ARRAY(Boolean))


class Display(Base):
    __tablename__ = "display"

    id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.discord_id"),
        primary_key=True
    )

    card: Mapped[int] = mapped_column(SMALLINT)
    banner: Mapped[int] = mapped_column(SMALLINT)
    buddy: Mapped[int] = mapped_column(SMALLINT)
    tags: Mapped[List[int]] = mapped_column(ARRAY(SMALLINT))

    description: Mapped[str] = mapped_column(String(length=264))


class Rank(Base):
    __tablename__ = "rank"

    id: Mapped[int] = mapped_column(
        BIGINT,
        ForeignKey("users.discord_id"),
        primary_key=True
    )

    ascension: Mapped[int] = mapped_column(INTEGER)
    level: Mapped[int] = mapped_column(SMALLINT)
    exp: Mapped[int] = mapped_column(INTEGER)


class Users(Base):
    __tablename__ = "users"

    discord_id: Mapped[int] = mapped_column(
        BIGINT,
        primary_key=True
    )

    coins: Mapped[int] = mapped_column(BIGINT)

    actions: Mapped["Actions"] = relationship(
        Actions,
        cascade="all, delete-orphan"
    )
    backpack: Mapped["Backpack"] = relationship(
        Backpack,
        cascade="all, delete-orphan"
    )
    collectables: Mapped["Collectables"] = relationship(
        Collectables,
        cascade="all, delete-orphan"
    )
    display: Mapped["Display"] = relationship(
        Display,
        cascade="all, delete-orphan"
    )
    rank: Mapped["Rank"] = relationship(
        Rank,
        cascade="all, delete-orphan"
    )

    created: Mapped[date] = mapped_column(DATE)


class Tags(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(
        SMALLINT,
        Identity(start=1),
        unique=True,
    )

    text: Mapped[str] = mapped_column(String(length=11))
    color: Mapped[str] = mapped_column(String(length=7))
