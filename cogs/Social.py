from abs_pth import json_text
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from cogs.commands.social.functions.tenor_gif import tenor
from cogs.commands.social.embed import Gif
import nextcord
from view.page import Page

where = ["cogs", "commands", "social", "text", "description.json"]
command = ["social", "who", "type"]
slash = json_text(where=where, commands=command)


class Social(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**slash.social)
    async def social(self,
                     interaction: Interaction,
                     action: str = SlashOption(
                         **slash.type,
                         required=True
                     ),
                     who: nextcord.Member = SlashOption(
                         **slash.who,
                         required=False
                     )
                     ):
        if who:
            who = who.name

        gif = await tenor(action=action)

        root_path = ["cogs", "commands", "social", "text", "response.json"]
        deck = ["response"]
        elements = json_text(where=root_path, commands=deck)
        embed = await Gif(**elements, **gif).embeding(
            action=action,
            language=interaction.locale,
            who=who,
            author=interaction.user.name
        )

        view = Page(embed=embed)
        view.message = await interaction.response.send_message(embed=embed[0], view=view)


def setup(client):
    client.add_cog(Social(client))
