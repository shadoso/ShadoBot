from datetime import datetime
import numpy as np
import asyncio

HASH_CARD = 78

FIRST_CARD = 0
HEXADECIMAL = 16
ENCODED = "utf-8"
HASH_SEED = 4294963094
testing = []


async def randomizer(hex_seed: str, length: int, rules: str = None):
    np.random.seed(int(hex_seed, HEXADECIMAL) % HASH_SEED)
    seeds = np.random.randint(HASH_SEED, size=length)
    if rules:
        pass
    else:
        position = []

    for seed in seeds:
        print(seed, seed % 78)

    np.random.seed(sum(seeds) % 256)
    li = np.random.choice([-1, 0, 1], size=length)
    print(li)

    # deck = {
    #     0: list(),
    #     1: list()
    # }
    # np.random.seed(int(hex_seed, HEXADECIMAL) % HASH_SEED)
    # seed_list = np.random.randint(HASH_SEED, size=length)
    # cards = []
    #
    # for index in range(length):
    #     np.random.seed(seed_list[index])
    #     np.random.shuffle(deck)
    #     cards.append(deck[FIRST_CARD])
    #     deck.pop(FIRST_CARD)
    # print(cards)

    return 0


async def card_shuffle():
    pass


async def card_spread(
        user: str, style: int, question: str,
        day: str = None, month: str = None, year: str = None
):
    dates = [day, month, year]
    today = {
        0: datetime.today().day,
        1: datetime.today().month,
        2: datetime.today().day
    }

    for index, date in enumerate(dates):
        if not date:
            dates[index] = str(today[index])

    cards = await randomizer(
        hex_seed=("".join(dates) + question + user + str(style)).encode(ENCODED).hex(),
        length=style
    )


if __name__ == "__main__":
    generating = asyncio.run(card_spread(
        user="1050127323795570750",
        style=5,
        question="Esse comando vai gerar o que eu quero ?",
        day="13",
        month="4",
        year="1999"
    ))
    generating1 = asyncio.run(card_spread(
        user="1050127323795570750",
        style=5,
        question="Esse comando vai gerar o que eu quero ?",
        day="4",
        month="8",
        year="1999"
    ))
    print(generating)
    print(generating1)
