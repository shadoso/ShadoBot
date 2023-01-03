from abs_pth import json_text
from pydantic import BaseModel
from nextcord import Embed
from standardization.language import Languages, validating, Attribute
from typing import Optional
import asyncio


class CommandBody(BaseModel):
    name: Languages
    valid: Optional[Languages]
    required: Languages
    examples: list[Languages]


class CogCommands(BaseModel):
    example: Languages
    valid: Languages
    required: Languages
    returns: Languages
    social: CommandBody
    ship: CommandBody

    async def embeding(self, command_name: str, language: str):
        lis = {
            0: self.example,
            1: self.returns
        }
        hash_table = 2
        command = self.__getattribute__(command_name)

        language = validating(language=language)

        embed = Embed(title=command.__getattribute__(Attribute.name).__getattribute__(language))
        embed.add_field(
            name=self.required.__getattribute__(language),
            value=command.__getattribute__(Attribute.required).__getattribute__(language),
            inline=False
        )
        if command.__getattribute__(Attribute.valid):
            embed.add_field(
                name=self.valid.__getattribute__(language),
                value=command.__getattribute__(Attribute.valid).__getattribute__(language),
                inline=False
            )
        for index, fields in enumerate(command.__getattribute__("examples")):
            embed.add_field(
                name=lis[index % hash_table].__getattribute__(language),
                value=fields.__getattribute__(language),
                inline=False
            )

        return embed


if __name__ == "__main__":
    where = ["cogs", "commands", "help", "text", "response.json"]
    commandss = ["response"]
    slash = json_text(where=where, commands=commandss)
    x = asyncio.run(CogCommands(**slash.response).embeding(command_name="ship", language="pt_BR"))
    print(x)
