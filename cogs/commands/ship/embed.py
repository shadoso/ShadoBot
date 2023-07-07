from nextcord import Embed
from absolute_path import cog_response
import asyncio

SHIP_ = cog_response(__file__)


async def ship_embed(percentage: str, key: int, language: str, who: str, crush: str):
    language = language.replace("-", "_")
    language = language if language in SHIP_.title.keys() else "default"

    embed = Embed(title=f"{SHIP_.title[language]}{percentage}%")
    embed.add_field(
        name=f"{who} + {crush}",
        value=SHIP_.text[key][language]
    )
    embed.add_field(
        name="",
        value=f"{SHIP_.credit[language]}{SHIP_.artist}",
        inline=False
    )
    embed.set_image(url=SHIP_.url[key])

    return embed


if __name__ == "__main__":
    testing = asyncio.run(ship_embed(percentage="44", key="44", language="pt-BR", who="Shadoso", crush="Bot"))
    print(testing.to_dict())