from absolute_path import cog_description
from cogs.base.command import BaseCommand
from cogs.commands.ship.embed import ship_embed
from cogs.commands.ship.functions.get_ship import compatibility
from nextcord import Interaction, SlashOption
import nextcord

SHIP_SLASH = cog_description(file_path=__file__)


class Ship(BaseCommand):
    def __init__(self, client):
        super().__init__(client)

    @nextcord.slash_command(**SHIP_SLASH.ship)
    async def ship(self,
                   interaction: Interaction,
                   crush: nextcord.Member = SlashOption(
                       **SHIP_SLASH.crush,
                       required=True
                   ),
                   who: nextcord.Member = SlashOption(
                       **SHIP_SLASH.who,
                       required=False
                   )
                   ):
        if not who:
            who = interaction.user

        percentage, key = await compatibility(
            who=who.id,
            crush=crush.id
        )
        embed = await ship_embed(
            percentage=percentage,
            key=key,
            language=interaction.locale,
            who=who.name,
            crush=crush.name
        )
        await self.send_response(interaction, embed=embed)


def setup(client):
    client.add_cog(Ship(client))
