from abs_pth import json_text
from app.data.schemas.apis.tenor_schema import Gif
from config.config import settings
from random import choice
from nextcord import Interaction, SlashOption, Embed
from nextcord.ext import commands
from urllib import parse, request
import json
import nextcord

where = ["app", "languages", "action.json"]
command = ["social", "who", "type", "not_found", "response"]
slash = json_text(where=where, commands=command)


class Action(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**slash.social)
    async def social(self,
                     interaction: Interaction,
                     action: str = SlashOption(
                         **slash.type,
                         required=True
                     ),
                     who: nextcord.Member = SlashOption(
                         **slash.who,
                         required=False
                     )
                     ):

        default = "default"
        max_amount = 3
        query = "?"
        random_gif = True
        status_ok = 200
        url = "https://tenor.googleapis.com/v2/search"
        body = {
            "q": f"Anime {action}",
            "key": settings.TENOR_API,
            "client_key": settings.CKEY,
            "limit": max_amount,
            "random": random_gif
        }
        params = parse.urlencode(body)

        with request.urlopen("".join((url, query, params))) as response:

            if response.status == status_ok:
                data = json.loads(response.read())

            else:

                if interaction.locale in slash.not_found.keys():
                    await interaction.response.send_message(slash.not_found[interaction.locale])

                else:
                    await interaction.response.send_message(slash.not_found[default])

        gif = Gif(**data).get_url()

        if who:

            if interaction.locale in slash.response[action].keys():
                embed = Embed(title=f"{interaction.user.name} {slash.response[action][interaction.locale]} {who.name}")
                embed.set_image(choice(gif))
                await interaction.response.send_message(embed=embed)

            else:
                embed = Embed(title=f"{interaction.user.name} {slash.response[action][default]} {who.name}")
                embed.set_image(choice(gif))
                await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message(choice(gif))


def setup(client):
    client.add_cog(Action(client))
