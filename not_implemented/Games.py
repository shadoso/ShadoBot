from absolute_path import cog_description
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import nextcord
from cogs.commands.games.dice_grid.super_embed import Board

GAME_SLASH = cog_description(file_path=__file__)


class Games(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command()
    async def games(self):
        pass

    @games.subcommand(**GAME_SLASH.dice)
    async def dice(self,
                   interaction: Interaction,
                   who: nextcord.Member = SlashOption(
                       **GAME_SLASH.who,
                       required=True
                   )
                   ):
        allowed = {
            interaction.user.id: interaction.locale,
            who.id: None
        }
        super_embed = Board(
            allowed=allowed
        )
        super_embed.message = await interaction.response.send_message()


def setup(client):
    client.add_cog(Games(client))
