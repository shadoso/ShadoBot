from absolute_path import cog_description
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord

BOT_SLASH = cog_description(file_path=__file__)


class Bot(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command()
    async def bot(self):
        pass

    @bot.subcommand(**BOT_SLASH.details)
    async def details(self, interaction: Interaction):
        await interaction.response.send_message(content="test")

    @bot.subcommand(**BOT_SLASH.ping)
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(content="test")

    @bot.subcommand(**BOT_SLASH.development)
    async def development(self, interaction: Interaction):
        await interaction.response.send_message(content="test")

    @bot.subcommand(**BOT_SLASH.subtitles)
    async def subtitles(self, interaction: Interaction):
        await interaction.response.send_message(content="test")


def setup(client):
    client.add_cog(Bot(client))
