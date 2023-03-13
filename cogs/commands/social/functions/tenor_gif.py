from config.config import settings
from urllib import parse, request
import json
import asyncio


async def tenor(action: str):
    gif_amount = 3
    query = "?"
    status_ok = 200
    url = "https://tenor.googleapis.com/v2/search"
    body = {
        "q": f"Anime {action}",
        "key": settings.TENOR_API,
        "client_key": settings.CKEY,
        "limit": gif_amount,
        "random": True
    }
    params = parse.urlencode(body)

    with request.urlopen("".join((url, query, params))) as response:
        if response.status == status_ok:
            return json.loads(response.read())

        else:
            return None


if __name__ == "__main__":
    test = asyncio.run(tenor("hug"))
    print(test)