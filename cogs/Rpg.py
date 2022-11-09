from abs_pth import json_file
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord

CHA, COU, GEN, QUA = json_file(
    where=["app", "languages", "rpg.json"],
    commands=["character", "country", "gender", "quantity"])


class Rpg(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(
        name="character",
        name_localizations=CHA["names"],
        description="Creates random characters",
        description_localizations=CHA["descriptions"],
    )
    async def character(self,
                        interaction: Interaction,
                        quantity: int = SlashOption(
                            name="quantity",
                            name_localizations=QUA["names"],
                            description="Quantity of characters, 1 to 15",
                            description_localizations=QUA["descriptions"],
                            required=True,
                            min_value=1,
                            max_value=15,
                        ),
                        country: str = SlashOption(
                            name="country",
                            name_localizations=COU["names"],
                            description="Choose character nationality",
                            description_localizations=COU["descriptions"],
                            choices=COU["choices"],
                            required=False
                        ),
                        gender: str = SlashOption(
                            name="gender",
                            name_localizations=GEN["names"],
                            description="Choose character gender",
                            description_localizations=GEN["descriptions"],
                            choices=GEN["choices"],
                            required=False
                        )

                        ):
        await interaction.response.send_message(f"Em desenvolvimento aguarde")


def setup(client):
    client.add_cog(Rpg(client))
