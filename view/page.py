import nextcord
from nextcord import Interaction, Button
from nextcord.ui import View

next_button = "~~(8:>️️ ~~(8:>️️"
previous_button = "<:8)~~ <:8)~~"


class Page(View):
    def __init__(self, embed: list, allowed: list):
        super().__init__(timeout=90)
        self.__embed = embed
        self.__page = 0
        self.message = None
        self.__allowed = allowed

    async def on_timeout(self):
        await self.message.edit(view=None)

    @nextcord.ui.button(label=previous_button, style=nextcord.ButtonStyle.gray)
    async def backward(self, button: Button, interaction: Interaction):
        if interaction.user.id in self.__allowed:
            self.__page = (self.__page - 1) % len(self.__embed)
            embed = self.__embed[self.__page]

            self.message = await interaction.response.edit_message(embed=embed)

    @nextcord.ui.button(label=next_button, style=nextcord.ButtonStyle.gray)
    async def forward(self, button: Button, interaction: Interaction):
        if interaction.user.id in self.__allowed:
            self.__page = (self.__page + 1) % len(self.__embed)
            embed = self.__embed[self.__page]

            self.message = await interaction.response.edit_message(embed=embed)
