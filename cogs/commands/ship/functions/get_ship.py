import asyncio
from config.constants import LAST_ELEMENT_, PERCENTAGE_
from algorithms.formulas import x_range as get_key

INTEGER_PERCENTAGE = 101
FLOAT_PERCENTAGE = PERCENTAGE_
STEP = -2


async def compatibility(who: int, crush: int):
    together = who + crush
    affinity = together % INTEGER_PERCENTAGE

    if affinity % PERCENTAGE_ == 0:
        return affinity, str(affinity)

    else:
        affinity_float_part = affinity + (int(str(together)[LAST_ELEMENT_::STEP]) % FLOAT_PERCENTAGE) / PERCENTAGE_
        affinity_key = get_key(
            max_range=PERCENTAGE_,
            mod=5,
            variable=affinity
        )
        return affinity_float_part, str(affinity_key)


if __name__ == "__main__":
    generating = asyncio.run(compatibility(who=12345674596889, crush=3614978179655))
    print()
    print(generating)
