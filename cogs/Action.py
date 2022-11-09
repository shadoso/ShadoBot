from abs_pth import json_file
from app.data.commands.schemas.apis.tenor_schema import Gif
from config.config import settings
from random import choice
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from urllib import parse, request
import json
import nextcord

SOCIAL, WHO, TYPE, NOT, RESPONSE = json_file(
    where=["app", "languages", "action.json"],
    commands=["social", "who", "type", "not_found", "response"])


class Action(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**SOCIAL)
    async def social(self,
                     interaction: Interaction,
                     action: str = SlashOption(
                         **TYPE,
                         required=True
                     ),
                     who: nextcord.Member = SlashOption(
                         **WHO,
                         required=False
                     )
                     ):
        body = {
            "q": f"Anime {action}",
            "key": settings.TENOR_API,
            "client_key": settings.CKEY,
            "limit": 3,
            "random": True
        }

        url = "https://tenor.googleapis.com/v2/search"
        params = parse.urlencode(body)

        with request.urlopen("".join((url, "?", params))) as response:
            if response.status == 200:
                data = json.loads(response.read())

            else:

                if interaction.locale in NOT.keys():
                    await interaction.response.send_message(NOT[interaction.locale])

                else:
                    await interaction.response.send_message(NOT["default"])

        gif = Gif(**data).get_url()

        if who:

            if interaction.locale in RESPONSE[action].keys():
                await interaction.response.send_message(
                    f"{interaction.user.mention} {RESPONSE[action][interaction.locale]} {who.mention}"
                )
                await interaction.channel.send(choice(gif))

            else:
                await interaction.response.send_message(
                    f"{interaction.user.mention} {RESPONSE[action]['default']} {who.mention}"
                )
                await interaction.channel.send(choice(gif))

        else:
            await interaction.response.send_message(choice(gif))


def setup(client):
    client.add_cog(Action(client))
