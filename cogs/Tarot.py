from abs_pth import json_text
from nextcord import Interaction, SlashOption, Embed
from nextcord.ext import commands
import nextcord
from cogs_methods.spread import generate_spread
from embed_buttons.page_number import Page

where = ["app", "languages", "tarot.json"]
command = ["tarot", "card", "number", "spread", "style", "question", "day", "month", "year", "response"]
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
                         min_length=15,
                         max_length=35,
                         required=True
                     ),
                     day: int = SlashOption(
                         **slash.day,
                         min_value=1,
                         max_value=31,
                         required=False
                     ),
                     month: int = SlashOption(
                         **slash.month,
                         min_value=1,
                         max_value=12,
                         required=False
                     ),
                     year: int = SlashOption(
                         **slash.year,
                         min_value=1912,
                         max_value=7648,
                         required=False
                     )
                     ):
        cards = await generate_spread(
            user=str(interaction.user.id),
            style=style,
            question=question,
            day=str(day),
            month=str(month),
            year=str(year)
        )
        embeds = []

        for index, card in enumerate(cards[:]):

            if index == 0:
                card_back = "78"
                url = slash.response[card_back]["url"]
                embeds.append(Embed(title=question).set_image(url=url))
            else:
                c = slash.response[str(card)]
                url = c["url"]
                name = c["name"]["default"]
                plus_key = c["keyword"]["up"]["default"]
                less_key = c["keyword"]["down"]["default"]
                plus_text = c["text"]["up"]["default"]
                less_text = c["text"]["down"]["default"]
                emb = Embed(title=name).set_image(url)
                emb.add_field(name="Keywords Up", value=plus_key, inline=False)
                emb.add_field(name="Card Up", value=plus_text, inline=False)
                emb.add_field(name="Keywords Down", value=less_key, inline=False)
                emb.add_field(name="Card Down", value=less_text, inline=False)
                embeds.append(emb)

        view = Page(embed=embeds)
        view.message = await interaction.response.send_message(embed=embeds[0], view=view)


def setup(client):
    client.add_cog(Tarot(client))
