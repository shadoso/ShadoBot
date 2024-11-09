from absolute_path import list_to_response
from nextcord import Embed
import asyncio

ACCOUNT_NOT_FOUND = list_to_response(file_path=["errors", "account", "text", "response.json"])


async def account_embed(language: str):
    language = language.replace("-", "_")
    language = language if language in ACCOUNT_NOT_FOUND.credit.keys() else "default"

    embed = Embed(title=ACCOUNT_NOT_FOUND.title)
    embed.add_field(
            name="",
            value=ACCOUNT_NOT_FOUND.error[language],
            inline=False
        )
    embed.add_field(
        name="",
        value=ACCOUNT_NOT_FOUND.credit[language] + ACCOUNT_NOT_FOUND.artist,
        inline=False
    )
    embed.set_image(url=ACCOUNT_NOT_FOUND.url)
    return embed


if __name__ == "__main__":
    testing = asyncio.run(account_embed("pt-BR"))
    print(testing.to_dict())