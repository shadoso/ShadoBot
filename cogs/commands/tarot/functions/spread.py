from datetime import datetime
import numpy as np
import asyncio


async def get_spread(
        user: str, style: int, question: str,
        day: str = None, month: str = None, year: str = None
):
    hash_table = 78
    available = list(range(hash_table))
    first_item = 0
    seeds = [1049, 9949, 1669, 2069, 5939]
    encoded = "utf-8"
    hexadecimal = 16
    cards = [hash_table]
    dates = [day, month, year]
    today = {
        0: datetime.today().day,
        1: datetime.today().month,
        2: datetime.today().day
    }

    for index, item in enumerate(dates):
        if not item:
            dates[index] = str(today[index])

    answer = ("".join(dates) + user + question + str(style)).encode(encoded).hex()

    for card in range(style):
        mixer = []
        mixer.extend(answer)

        np.random.seed(seeds[card])
        np.random.shuffle(mixer)
        mixer = int("".join(mixer), hexadecimal) % hash_table

        if mixer not in cards:
            cards.append(mixer)
            available.remove(mixer)

        else:
            # Pick a number that have been not used
            np.random.seed(seeds[card])
            np.random.shuffle(available)
            cards.append(available[first_item])

            # Return available to it's initial state
            available.remove(available[first_item])
            available.sort()

    return cards


if __name__ == "__main__":
    generating = asyncio.run(get_spread(
        user="1050127323795570750",
        style=5,
        question="Esse comando vai gerar o que eu quero ?",
        day="11",
        month="6",
        year="1999"
    ))
    print(generating)
