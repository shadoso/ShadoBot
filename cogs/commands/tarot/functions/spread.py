from datetime import datetime
import numpy as np
import asyncio


async def get_spread(
        user: str, style: int, question: str,
        day: str = None, month: str = None, year: str = None
):
    available = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
        52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
        65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77
    ]
    hash_table = 78
    first_item = 0
    seeds = [1049, 9949, 1669, 2069, 5939]
    encoded = "utf-8"
    hexadecimal = 16
    cards = [78]
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
