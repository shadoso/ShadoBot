from absolute_path import cog_description
from cogs.commands.social.embed import Gif
from cogs.commands.social.functions.tenor_gif import tenor
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from view.page import Page
import nextcord

SOCIAL_SLASH = cog_description(file_path=__file__)


class Social(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**SOCIAL_SLASH.social)
    async def social(self,
                     interaction: Interaction,
                     action: str = SlashOption(
                         **SOCIAL_SLASH.type,
                         required=True
                     ),
                     who: nextcord.Member = SlashOption(
                         **SOCIAL_SLASH.who,
                         required=False
                     )
                     ):
        allow_interaction = [interaction.user.id]

        if who:
            allow_interaction.append(who.id)
            who = who.name

        gif = await tenor(action=action)
        embed = await Gif(**gif).social_embed(
            action=action,
            language=interaction.locale,
            who=who,
            author=interaction.user.name
        )
        view = Page(
            embed=embed,
            allowed=allow_interaction
        )
        view.message = await interaction.response.send_message(embed=embed[0], view=view)


def setup(client):
    client.add_cog(Social(client))
