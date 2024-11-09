from pydantic import BaseModel
from absolute_path import cog_response
from nextcord import Embed
from languages.check_language import verify_language

SOCIAL = cog_response(__file__)


class Url(BaseModel):
    url: str


class Link(BaseModel):
    mediumgif: Url


class Formats(BaseModel):
    media_formats: Link


class Gif(BaseModel):
    results: list[Formats]

    async def social_embed(self, action: str, language: str, author: str, who: str = None):
        embeds = []
        language = await verify_language(
            language=language,
            language_keys=SOCIAL.credit
        )

        for gif in self.results:
            if who:
                embed = Embed(title=f"{author} {SOCIAL.response[action][language]} {who}")
                embed.add_field(
                    name="",
                    value=f"{SOCIAL.credit[language]}{SOCIAL.site}"
                )
                embed.set_image(url=gif.media_formats.mediumgif.url)

            else:
                embed = Embed().add_field(
                    name="",
                    value=f"{SOCIAL.credit[language]}{SOCIAL.site}"
                )
                embed.set_image(url=gif.media_formats.mediumgif.url)

            embeds.append(embed)

        return embeds
