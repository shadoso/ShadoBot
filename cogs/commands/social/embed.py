from pydantic import BaseModel
from nextcord import Embed
import asyncio
from cogs.commands.social.functions.tenor_gif import tenor
from abs_pth import json_text
from standardization.language import Languages, validating


class Action(BaseModel):
    angry: Languages
    bite: Languages
    bored: Languages
    cry: Languages
    cuddle: Languages
    glare: Languages
    happy: Languages
    hug: Languages
    kick: Languages
    kiss: Languages
    lick: Languages
    pat: Languages
    poke: Languages
    punch: Languages
    slap: Languages


class Url(BaseModel):
    url: str


class Link(BaseModel):
    mediumgif: Url


class Formats(BaseModel):
    media_formats: Link


class Gif(BaseModel):
    response: Action
    results: list[Formats]

    async def embeding(self, action: str, language: str, author: str, who: str = None):
        embeds = []
        language = validating(language=language)

        for gif in self.results:
            if who:
                title = author + " " + self.response.__getattribute__(action).__getattribute__(language) + " " + who
                embed = Embed(title=title).set_image(gif.media_formats.mediumgif.url)

            else:
                embed = Embed().set_image(gif.media_formats.mediumgif.url)

            embeds.append(embed)

        return embeds


if __name__ == "__main__":
    gif = asyncio.run(tenor("hug"))
    root_path = ["cogs", "commands", "social", "text", "response.json"]
    deck = ["response"]
    elements = json_text(where=root_path, commands=deck)
    embed = asyncio.run(Gif(**elements, **gif).embeding(
        action="hug",
        language="pt_BR",
        who="Shadoso",
        author="Will"
    ))
    print(embed)
