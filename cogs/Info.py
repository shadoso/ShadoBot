from abs_pth import json_file
from nextcord import Interaction
from nextcord.ext import commands
import nextcord

LANGUAGE, RESPONSES = json_file(
    where=["app", "languages", "info.json"],
    commands=["language", "responses"]
)


class Info(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(
        name="ping",
        description="Bot latency"
    )
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(f"Pong {interaction.client.latency * 1000:.2f}")

    @nextcord.slash_command(**LANGUAGE)
    async def language(self, interaction: Interaction):

        if interaction.locale in RESPONSES.keys():
            await interaction.response.send_message(RESPONSES[interaction.locale])

        else:
            await interaction.response.send_message(RESPONSES["default"])


def setup(client):
    client.add_cog(Info(client))
