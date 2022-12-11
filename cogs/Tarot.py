from abs_pth import json_text
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from cogs.commands.tarot.embed import Deck
from cogs.commands.tarot.functions.spread import get_spread
from view.page import Page
import nextcord

where = ["cogs", "commands", "tarot", "text", "description.json"]
command = [
    "tarot", "card", "number",
    "spread", "style", "question",
    "day", "month", "year"
]
slash = json_text(where=where, commands=command)


class Tarot(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command()
    async def tarot(self):
        pass

    # @tarot.subcommand(**slash.card)
    # async def card(self,
    #                interaction: Interaction,
    #                number: int = SlashOption(
    #                    **slash.number,
    #                    required=True,
    #                    min_value=0,
    #                    max_value=78
    #                )
    #                ):
    #     embed = Embed()
    #     embed.set_image(slash.deck[str(number)])
    #     await interaction.response.send_message(embed=embed)

    @tarot.subcommand(**slash.spread)
    async def spread(self,
                     interaction: Interaction,
                     style: int = SlashOption(
                         **slash.style,
                         required=True,
                     ),
                     question: str = SlashOption(
                         **slash.question,
                         required=True
                     ),
                     day: int = SlashOption(
                         **slash.day,
                         required=False
                     ),
                     month: int = SlashOption(
                         **slash.month,
                         required=False
                     ),
                     year: int = SlashOption(
                         **slash.year,
                         required=False
                     )
                     ):
        cards = await get_spread(
            user=str(interaction.user.id),
            style=style,
            question=question,
            day=str(day),
            month=str(month),
            year=str(year)
        )
        root_path = ["cogs", "commands" "tarot", "text", "response.json"]
        deck = ["response"]
        elements = json_text(where=root_path, commands=deck)
        embeds = await Deck(**elements.response).embeding(language=interaction.locale, cards=cards)
        view = Page(embed=embeds)
        view.message = await interaction.response.send_message(embed=embeds[0], view=view)


def setup(client):
    client.add_cog(Tarot(client))
