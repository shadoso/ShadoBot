import asyncio


async def compatibility(who: int, crush: int):
    first_key = 0
    half = 2
    float_part = 100
    percentage = 101
    last_key = float_part
    last_number = -1
    valid_numbers = ["4", "9"]
    valid_key = {
        "0": "4", "1": "4", "2": "4", "3": "4",
        "5": "9", "6": "9", "7": "9", "8": "9",
    }

    percentage = (who + crush) % percentage
    floating_point = ((who / half) + (crush / half)) % float_part / float_part
    key = percentage

    if percentage < float_part:
        percentage += floating_point

    if first_key < key < last_key and str(key)[last_number] not in valid_numbers:
        key = str(key)[:last_number] + valid_key[str(key)[last_number]]

    return [f"{percentage:.2f}", int(key)]


if __name__ == "__main__":
    generating = asyncio.run(compatibility(who=12345674596889, crush=3614978179655))
    print(generating)