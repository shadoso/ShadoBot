from abs_pth import json_text
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord

where = ["app", "languages", "rpg.json"]
command = ["characters", "country", "gender", "quantity"]
slash = json_text(where=where, commands=command)


class Rpg(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**slash.characters)
    async def character(self,
                        interaction: Interaction,
                        quantity: int = SlashOption(
                            **slash.quantity,
                            required=True,
                            min_value=1,
                            max_value=15,
                        ),
                        country: str = SlashOption(
                            **slash.country,
                            required=False
                        ),
                        gender: str = SlashOption(
                            **slash.gender,
                            required=False
                        )

                        ):
        await interaction.response.send_message(f"Em desenvolvimento aguarde")


def setup(client):
    client.add_cog(Rpg(client))
