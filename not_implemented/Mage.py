from absolute_path import cog_description
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord

MAGE_SLASH = cog_description(file_path=__file__)


class Mage(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command()
    async def mage(self):
        pass

    @mage.subcommand()
    async def ascension(self):
        pass

    @ascension.subcommand()
    async def sphere(self):
        pass


def setup(client):
    client.add_cog(Mage(client))
