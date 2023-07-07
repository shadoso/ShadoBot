from absolute_path import list_to_response
from nextcord import Embed
import asyncio

ERROR_ = list_to_response(file_path=["error_warning", "text", "response.json"])


async def error_embed(language: str):
    language = language.replace("-", "_")
    language = language if language in ERROR_.credit.keys() else "default"

    embed = Embed(title=ERROR_.title)
    for error_text in ERROR_.error[language]:
        embed.add_field(
            name="",
            value=error_text,
            inline=False
        )
    embed.add_field(
        name="",
        value=ERROR_.credit[language] + ERROR_.artist,
        inline=False
    )
    embed.set_image(url=ERROR_.url)
    return embed


if __name__ == "__main__":
    testing = asyncio.run(error_embed("pt-BR"))
    print(testing.to_dict())