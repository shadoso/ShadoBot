from abs_pth import json_text
from pydantic import BaseModel
from nextcord import Embed
from standardization.language import Languages, validating
import asyncio


class Text(BaseModel):
    key: int
    text: Languages


class Response(BaseModel):
    title: Languages
    response: list[Text]

    async def embeding(self, percentage: str, key: int, language: str, who: str, crush: str):
        couple = f"{who} + {crush}"
        index = {
            0: 0, 4: 1, 9: 2, 14: 3, 19: 4,
            24: 5, 29: 6, 34: 7, 39: 8, 44: 9,
            49: 10, 54: 11, 59: 12, 64: 13, 69: 14,
            74: 15, 79: 16, 84: 17, 89: 18, 94: 19,
            99: 20, 100: 21
        }
        language = validating(language=language)

        embed = Embed(
            title=self.title.__getattribute__(language) + percentage + "%"
        )
        embed.add_field(name=couple, value=self.response[index[key]].text.__getattribute__(language))

        return embed


if __name__ == "__main__":
    where = ["cogs", "commands", "ship", "text", "response.json"]
    command = ["title", "response"]
    slash = json_text(where=where, commands=command)
    x = asyncio.run(Response(**slash).embeding(
        percentage="32.22", key=34, language="pt-BR", who="shads", crush="nads"
    ))
    print(x)
