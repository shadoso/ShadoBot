from absolute_path import list_to_response
from languages.check_language import verify_language
from nextcord import Embed
import asyncio

ERROR_MESSAGE = list_to_response(file_path=["errors", "warning", "text", "response.json"])


async def error_embed(language: str):
    language = await verify_language(
        language=language,
        language_keys=ERROR_MESSAGE.credit
    )

    embed = Embed(title=ERROR_MESSAGE.title)
    for error_text in ERROR_MESSAGE.error[language]:
        embed.add_field(
            name="",
            value=f"**```{error_text}```**",
            inline=False
        )
    embed.add_field(
        name="",
        value=f"**{ERROR_MESSAGE.credit[language]}**" + ERROR_MESSAGE.artist,
        inline=False
    )
    embed.set_image(url=ERROR_MESSAGE.url)
    return embed


if __name__ == "__main__":
    testing = asyncio.run(error_embed("pt-BR"))
    print(testing.to_dict())
