from abs_pth import json_text
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord
from cogs.commands.help.embed import CogCommands

where = ["cogs", "commands", "help", "text", "description.json"]
command = ["help", "commandd"]
slash = json_text(where=where, commands=command)


class Help(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**slash.help)
    async def help(self,
                   interaction: Interaction,
                   commandd: str = SlashOption(
                       **slash.commandd,
                       required=True
                   )
                   ):
        whee = ["cogs", "commands", "help", "text", "response.json"]
        commandss = ["response"]
        isla = json_text(where=whee, commands=commandss)
        embed = await CogCommands(**isla.response).embeding(command_name=commandd, language=interaction.locale)

        await interaction.user.send(embed=embed)
        await interaction.response.send_message("test")


def setup(client):
    client.add_cog(Help(client))
