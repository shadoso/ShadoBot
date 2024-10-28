from config.config import settings
import aiohttp
import asyncio
from absolute_path import ai_json

async def generate_text(question: str, language: str):
    url = "https://" + settings.DOMAIN
    payload = {
        "secret": settings.SHADOBOT_AI,
        "action": "talk",
        "language": language,
        "role": "user",
        "message": question
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()

if __name__ == "__main__":
    test = asyncio.run(generate_text("Tock Tock"))
    hay = asyncio.run(ai_json(test))
    print(test["messages"][-1]["content"])
