from abs_pth import json_text
from nextcord import Interaction
from nextcord.ext import commands
import nextcord

where = ["app", "languages", "info.json"]
command = ["language", "responses"]

slash = json_text(where=where, commands=command)


class Info(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(
        name="ping",
        description="Bot latency"
    )
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(f"Pong {interaction.client.latency * 1000:.2f}")

    @nextcord.slash_command(**slash.language)
    async def language(self, interaction: Interaction):
        default = "default"

        if interaction.locale in slash.responses.keys():
            await interaction.response.send_message(slash.responses[interaction.locale])

        else:
            await interaction.response.send_message(slash.responses[default])


def setup(client):
    client.add_cog(Info(client))
