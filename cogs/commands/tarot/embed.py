from nextcord import Embed
import asyncio
from absolute_path import cog_response

TAROT_ = cog_response(__file__)


async def tarot_embed(self, language: str, cards: list[int]):
    embeds = []
    language = language.replace("-", "_")
    language = language if language in TAROT_.credit.keys() else "default"

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


async def texts(self, language: str, cards: list[int]):
    embeds = []
    position = {
        0: "upright",
        1: "inverted"
    }
    language = validating(language=language)

    for card in cards:
        content = self.deck[card]
        description = content.card_description

        for index, subject in enumerate([description.upright, description.inverted]):
            print(subject.text.__getattribute__(language))

        print()

    return None


if __name__ == "__main__":
    where = ["cogs", "commands", "tarot", "text", "response.json"]
    command = ["response"]
    slash = json_text(where=where, commands=command)
    cardss = list(range(25, 32))
    x = asyncio.run(Deck(**slash.response).texts("deafult", cards=cardss))
    print(x)
