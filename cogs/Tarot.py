from absolute_path import cog_description
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from view.page import Page
import nextcord
from cogs.commands.tarot.functions.spread import card_spread
from cogs.commands.tarot.embed import tarot_embed_default
from config.constants import SHADOBOT_

TAROT_SLASH = cog_description(file_path=__file__)


class Tarot(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**TAROT_SLASH.tarot)
    async def tarot(self,
                    interaction: Interaction
                    ):
        pass

    @tarot.subcommand(**TAROT_SLASH.reading)
    async def reading(self,
                      interaction: Interaction,
                      style: str = SlashOption(
                          **TAROT_SLASH.style,
                          required=True,
                      ),
                      modifier: str = SlashOption(
                          **TAROT_SLASH.modifier,
                          required=False
                      ),
                      day: int = SlashOption(
                          **TAROT_SLASH.day,
                          required=False
                      ),
                      month: int = SlashOption(
                          **TAROT_SLASH.month,
                          required=False
                      ),
                      year: int = SlashOption(
                          **TAROT_SLASH.year,
                          required=False
                      )
                      ):
        if not modifier:
            modifier = SHADOBOT_

        cards, flip_side = await card_spread(
            user=str(interaction.user.id),
            length=TAROT_SLASH.length[style],
            style=style,
            seed=modifier,
            day=str(day),
            month=str(month),
            year=str(year),
        )
        embeds = await tarot_embed_default(
            language=interaction.locale,
            cards=cards,
            flip_side=flip_side,
            style=style,
        )
        view = Page(embed=embeds, allowed=[interaction.user.id])
        view.message = await interaction.response.send_message(embed=embeds[0], view=view)


def setup(client):
    client.add_cog(Tarot(client))
