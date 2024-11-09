import numpy as np
import asyncio
from config.constants import ENCODED_UTF_8_, HEXADECIMAL_

AVAILABLE_VALUES = [-1, 1]
BOTH_CATEGORY = 0
DEFAULT_FORMAT = ([-1, 1], [1, 0])
EMPTY_ARRAY = BOTH_CATEGORY
HASH_SEED = 4294963094
LAST_CARD = 78
MAJOR_CARD_RANGE = 22
MAJOR_CATEGORY = 1
MINOR_CATEGORY = -1
RESERVED_INDEX = MAJOR_CATEGORY
SHAPES = BOTH_CATEGORY
STATIC_SHAPE = MAJOR_CATEGORY
TOP_DECK = MINOR_CATEGORY
VALUES = MAJOR_CATEGORY


async def randomizer(
        hexadecimal_string: str,
        length: int,
        rules: list
):
    """
    Generate random draw information based on provided rules.

    Parameters
    ----------
    hexadecimal_string : str
        Hexadecimal seed value used for random number generation.
    length : int
        Length of the draw information to generate.
    rules : list
        List of rules specifying shapes and values for the draw.

    Returns
    -------
    shapes : numpy.ndarray
        Array containing the generated shapes for the draw.
    values : numpy.ndarray
        Array containing the generated values for the draw.
    seeds : numpy.ndarray
        Array of random seeds used for generation.
    """

    np.random.seed(int(hexadecimal_string, HEXADECIMAL_) % HASH_SEED)

    array_unique_element = np.full(shape=length - RESERVED_INDEX, fill_value=MINOR_CATEGORY)

    cards_info = [
        np.full(shape=length, fill_value=value) if shape == STATIC_SHAPE else
        np.hstack((array_unique_element * value, value)) for shape, value in zip(rules[SHAPES], rules[VALUES])
    ]

    if not any(cards_info[VALUES]):
        cards_info[VALUES] = np.random.choice(AVAILABLE_VALUES, length)

    np.random.shuffle(cards_info[SHAPES])
    np.random.shuffle(cards_info[VALUES])

    seeds = np.random.randint(HASH_SEED, size=length)

    return cards_info[SHAPES], cards_info[VALUES], seeds


async def drawing_cards(
        card_category_list: list,
        seeds: list
):
    major = np.array(range(MAJOR_CARD_RANGE))
    minor = np.array(range(MAJOR_CARD_RANGE, LAST_CARD))
    selected_cards = np.empty(EMPTY_ARRAY)

    deck = {
        MINOR_CATEGORY: minor,
        BOTH_CATEGORY: np.hstack((major, minor)),
        MAJOR_CATEGORY: major
    }
    for selected_category, seed in zip(card_category_list, seeds):
        # Removing drawn cards from the deck using A - B operation.
        deck[selected_category] = np.setdiff1d(deck[selected_category], selected_cards)

        np.random.seed(seed)
        np.random.shuffle(deck[selected_category])

        # append no numpy é estranho, não está errado
        selected_cards = np.append(selected_cards, (deck[selected_category][TOP_DECK]))

    return selected_cards.astype(int)


async def hexadecimal(
        user: str,
        day: str,
        month: str,
        year: str,
        length: str,
        style: str,
        seed: str
):
    from datetime import datetime

    dates = [
        day,
        month,
        year
    ]
    today = [
        datetime.today().day,
        datetime.today().month,
        datetime.today().year
    ]

    string_to_digest = [seed, style, length, user] + [
        str(today_value) if not date else
        str(date) for today_value, date in zip(today, dates)
    ]

    return ("".join(string_to_digest)).encode(ENCODED_UTF_8_).hex()


async def card_spread(
        user: str,
        length: int,
        seed: str,
        style: str,
        day: str = None,
        month: str = None,
        year: str = None,
        rules: list = DEFAULT_FORMAT
):
    hexadecimal_string = await hexadecimal(
        user=user,
        day=day,
        month=month,
        year=year,
        length=str(length),
        style=style,
        seed=seed
    )

    card_category_list, flip_side, seeds = await randomizer(
        hexadecimal_string=hexadecimal_string,
        length=length,
        rules=rules
    )

    hand = await drawing_cards(
        card_category_list=card_category_list,
        seeds=seeds
    )

    return hand.tolist(), flip_side.tolist()


if __name__ == "__main__":
    lis = [[-1, -1, -1, -1], [-1, -1, -1, 1], [-1, -1, 1, -1], [-1, -1, 1, 0], [-1, -1, 1, 1], [-1, 1, -1, -1],
           [-1, 1, -1, 1], [-1, 1, 1, -1], [-1, 1, 1, 0], [-1, 1, 1, 1], [1, -1, -1, -1], [1, -1, -1, 1],
           [1, -1, 1, -1], [1, -1, 1, 0], [1, -1, 1, 1], [1, 0, -1, -1], [1, 0, -1, 1], [1, 0, 1, -1], [1, 0, 1, 0],
           [1, 0, 1, 1], [1, 1, -1, -1], [1, 1, -1, 1], [1, 1, 1, -1], [1, 1, 1, 0], [1, 1, 1, 1]]
    for num in range(len(lis)):
        # print(f"{lis[num][:2]}{'  ' * 5}{lis[num][2:]}")
        generating = asyncio.run(card_spread(
            user="1050127323795570750",
            length=5,
            seed="Esse comando vai gerar o que eu quero ?",
            day=str(num),
            month="4",
            year="1999",
            style="tarot",
        ))
        print(generating)
        print()
