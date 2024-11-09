from nextcord import Interaction
from nextcord.ext import commands

class BaseCommand(commands.Cog):
    def __init__(self, client, timeout=32, delete_after=64):
        self.client = client
        self.timeout = timeout
        self.delete_after = delete_after

    async def send_response(self, interaction: Interaction, embed=None, content=None):
        await interaction.response.send_message(
            content=content,
            embed=embed,
            delete_after=self.delete_after
        )
