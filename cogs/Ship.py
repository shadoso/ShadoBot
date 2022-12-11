from abs_pth import json_text
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord
from cogs.commands.ship.functions.get_ship import compatibility
from cogs.commands.ship.embed import Response

where = ["cogs", "commands", "ship", "text", "description.json"]
command = ["ship", "crush", "who"]

slash = json_text(where=where, commands=command)


class Ship(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**slash.ship)
    async def ship(self,
                   interaction: Interaction,
                   crush: nextcord.Member = SlashOption(
                       **slash.crush,
                       required=True),
                   who: nextcord.Member = SlashOption(
                       **slash.who,
                       required=False)
                   ):
        if not who:
            who = interaction.user

        percentage, key = await compatibility(who=who.id, crush=crush.id)
        di = ["cogs", "commands", "ship", "text", "response.json"]
        na = ["title", "response"]
        shi = json_text(where=di, commands=na)
        embed = await Response(**shi).embeding(
            percentage=percentage,
            key=key,
            language=interaction.locale,
            who=who.name,
            crush=crush.name
        )
        await interaction.response.send_message(embed=embed)


def setup(client):
    client.add_cog(Ship(client))
