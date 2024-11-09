from sqlalchemy import Select
from database.models.users import Users, Display, Rank
from database.session import database_session
from algorithms.formulas import equation_straight_line as progress
from config.constants import EXP_, MONEY_SYMBOL_

import asyncio

UNNECESSARY = ["id", "card", "ascension"]
ENTITIES = [Users.coins] + [key for key in [*Display.__table__.c, *Rank.__table__.c] if key.name not in UNNECESSARY]
DOT = "."


async def details(discord_id: int):
    session = await database_session()

    query = Select(*ENTITIES).join(Users.display).join(Users.rank).where(Users.discord_id == discord_id).union()
    query = await session.execute(statement=query)
    await session.close()

    return dict(*query.mappings())


async def currency(coins: int):
    from math import log10

    units = int(log10(coins) + 1)
    mod = units % 3
    end = 4 - 0 ** mod

    money = f"{coins:,}"[:end:].replace(",", DOT) + " "
    money = money.replace(".0 ", "").strip()

    if DOT in money and money[-1] == "0":
        money = money.rstrip("0")

    return money + MONEY_SYMBOL_[units - mod - 3 * 0 ** mod]


async def experience(level: int, exp: int):
    minimum = [0, 314]
    maximum = [100, 0]
    percentage = float(f"{exp / EXP_[level] * 100:.2f}")
    bar = progress(first_interval=minimum, second_interval=maximum, variable=percentage)
    return f"{exp:,}/{EXP_[level]:,}".replace(",", DOT), f"{bar:.2f}"


async def nick(name: str):
    minimum = [32, 18]
    maximum = [20, 28]
    if len(name) <= 20:
        return 28

    else:
        font = progress(first_interval=minimum, second_interval=maximum, variable=len(name))
        return int(font)


async def tag():
    pass


async def main():
    pass
    # x = await details(discord_id=706647393478901864)
    # y = await details(discord_id=292139416275779584)


if __name__ == "__main__":
    x = asyncio.run(main())
