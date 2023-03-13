from abs_pth import json_text
from pydantic import BaseModel
from nextcord import Embed
from standardization.language import Languages, validating
import asyncio


class GlobalError(BaseModel):
    title: str
    text: Languages
    artist: str
    error: Languages
    url: str

    async def embeding(self, language: str):
        language = validating(language=language)
        description = self.error.__getattribute__(language)
        embed = Embed().add_field(name=self.title, value=description).set_image(self.url)
        return embed.add_field(name="", value=self.text.__getattribute__(language) + self.artist, inline=False)


if __name__ == "__main__":
    root_path = ["app", "main", "text", "response.json"]
    deck = ["response"]
    elements = json_text(where=root_path, commands=deck)
    embed = asyncio.run(GlobalError(**elements.response).embeding(language="pt-BR"))
    print(embed)
