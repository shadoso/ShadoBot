import nextcord
from nextcord import Interaction, Button
from nextcord.ui import View

next_button = "➡️"
previous_button = "⬅️"
label = "1"


class Page(View):
    def __init__(self, embed: list, allowed: list):
        super().__init__(timeout=90)
        self.__embed = embed
        self.__page = 0
        self.message = None
        self.__allowed = allowed

    async def on_timeout(self):
        await self.message.edit(view=None)

    @nextcord.ui.button(emoji=previous_button, style=nextcord.ButtonStyle.blurple)
    async def backward(self, button: Button, interaction: Interaction):
        if interaction.user.id in self.__allowed:
            self.__page = (self.__page - 1) % len(self.__embed)
            embed = self.__embed[self.__page]
            self.children[1].label = str(self.__page + 1)
            self.message = await interaction.response.edit_message(embed=embed, view=self)

    @nextcord.ui.button(disabled=True, label=label, style=nextcord.ButtonStyle.blurple)
    async def middle(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(emoji=next_button, style=nextcord.ButtonStyle.blurple)
    async def forward(self, button: Button, interaction: Interaction):
        if interaction.user.id in self.__allowed:
            self.__page = (self.__page + 1) % len(self.__embed)
            embed = self.__embed[self.__page]
            self.children[1].label = str(self.__page + 1)
            self.message = await interaction.response.edit_message(embed=embed, view=self)
