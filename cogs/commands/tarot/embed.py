from typing import Union
from abs_pth import json_text
from pydantic import BaseModel
from nextcord import Embed
import asyncio


class Languages(BaseModel):
    pt_BR: str = "pt_BR"
    default: str = "default"


class KeyText(BaseModel):
    keywords: Languages
    text: Languages


class CardDescription(BaseModel):
    upright: KeyText
    inverted: KeyText


class Fields(BaseModel):
    archetype: Languages
    upright: KeyText
    inverted: KeyText


class Card(BaseModel):
    url: str
    archetype: Union[str, None]
    name: Languages
    card_description: CardDescription


class Deck(BaseModel):
    fields: Fields
    deck: list[Card]

    async def embeding(self, language: str, cards: list[int]):
        embeds = []
        position = {
            0: "upright",
            1: "inverted"
        }
        language = language.replace("-", "_")

        if language not in dir(Languages()):
            language = Languages().default

        for card in cards:
            field = self.fields
            content = self.deck[card]
            description = content.card_description

            embed = Embed(title=content.name.__getattribute__(language)).set_image(content.url)
            embed.add_field(name=field.archetype.__getattribute__(language), value=content.archetype, inline=False)

            for index, subject in enumerate([description.upright, description.inverted]):
                embed.add_field(
                    name=field.__getattribute__(position[index]).keywords.__getattribute__(language),
                    value=subject.keywords.__getattribute__(language),
                    inline=False
                )
                embed.add_field(
                    name=field.__getattribute__(position[index]).text.__getattribute__(language),
                    value=subject.text.__getattribute__(language),
                    inline=False
                )

            embeds.append(embed)
        return embeds


if __name__ == "__main__":
    where = ["cogs", "commands", "tarot", "text", "response.json"]
    command = ["response"]
    slash = json_text(where=where, commands=command)
    cardss = [78, 0, 13, 48, 42]
    x = asyncio.run(Deck(**slash.response).embeding("pt_BR", cards=cardss))
    print(x)
