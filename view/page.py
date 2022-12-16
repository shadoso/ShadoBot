import nextcord
from nextcord import Interaction, Button
from nextcord.ui import View

next_button = "~~(8:>️️ ~~(8:>️️"
previous_button = "<:8)~~ <:8)~~"
one = 1


class Page(View):
    def __init__(self, embed: list):
        super().__init__(timeout=90)
        self.__embed = embed
        self.__page = 0
        self.message = None

    async def on_timeout(self):
        await self.message.edit(view=None)

    @nextcord.ui.button(label=previous_button, style=nextcord.ButtonStyle.gray)
    async def backward(self, button: Button, interaction: Interaction):
        self.__page -= one
        click = self.__page % len(self.__embed)
        embed = self.__embed[click]

        self.message = await interaction.response.edit_message(embed=embed)

    @nextcord.ui.button(label=next_button, style=nextcord.ButtonStyle.gray)
    async def forward(self, button: Button, interaction: Interaction):
        self.__page += one
        click = self.__page % len(self.__embed)
        embed = self.__embed[click]

        self.message = await interaction.response.edit_message(embed=embed)
