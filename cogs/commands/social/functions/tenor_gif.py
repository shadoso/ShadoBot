from config.config import settings
import aiohttp
import asyncio

GIF_AMOUNT = 3
QUERY = "?"
STATUS_OK = 200


async def tenor(action: str):
    url = f"https://tenor.googleapis.com/v2/search?q=Anime {action}&key={settings.TENOR_API}&client_key={settings.CKEY}&limit={GIF_AMOUNT}&random=True"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

if __name__ == "__main__":
    test = asyncio.run(tenor("hug"))
    print(test)
