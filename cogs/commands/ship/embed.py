from nextcord import Embed
from absolute_path import cog_response
import asyncio
from languages.check_language import verify_language

SHIP = cog_response(__file__)


async def ship_embed(percentage: float, key: str, language: str, who: str, crush: str):
    language = await verify_language(
        language=language,
        language_keys=SHIP.title
    )

    embed = Embed(title=f"{SHIP.title[language]}{percentage}%")
    embed.add_field(
        name=f"{who} + {crush}",
        value=SHIP.text[key][language]
    )
    embed.add_field(
        name="",
        value=f"{SHIP.credit[language]}{SHIP.artist}",
        inline=False
    )
    embed.set_image(url=SHIP.url[key])

    return embed


if __name__ == "__main__":
    testing = asyncio.run(ship_embed(percentage=44, key="44", language="pt-BR", who="Shadoso", crush="Bot"))
    print(testing.to_dict())
