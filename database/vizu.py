import csv
from pathlib import Path
from database.session import database_session, create_tables
from datetime import date, datetime
import asyncio
from sqlalchemy import select
from database.session import database_session

contain = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}


async def main():
    await create_tables()


async def verify(name):
    sub_set = set(name.lower())
    if len(sub_set) >= 2 and sub_set.issubset(contain):
        return name


if __name__ == "__main__":
    asyncio.run(create_tables())
