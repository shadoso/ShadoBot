import nextcord
from nextcord import Interaction, Button
from absolute_path import cog_response
from nextcord.ui import View

DICE_GAME = cog_response(__file__)
DICE = [d for d in range(1, 7)]
RIVAL = 1
EMPTY = 0
test = "teste"


class Board(View):
    def __init__(self, allowed: dict):
        super().__init__(timeout=90)

        self.__same_locale = False
        self.__current = 0
        self.__player = {
            index: [[EMPTY] * 3 for _ in range(3)] for index in range(2)
        }
        self.message = None
        self.__allowed = allowed

    def custom_label(self):
        return str(self.__current)

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.green)
    async def confirm(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.danger)
    async def deny(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.green)
    async def left(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.danger)
    async def middle(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.danger)
    async def right(self, button: Button, interaction: Interaction):
        pass

    @nextcord.ui.button(label=custom_label(), style=nextcord.ButtonStyle.danger)
    async def surrender(self, button: Button, interaction: Interaction):
        pass

    @staticmethod
    async def roll():
        from numpy.random import choice
        return choice(DICE)

    async def available(self) -> list:
        return [index + 1 for index, grid in enumerate(self.__player[self.__current]) if EMPTY in grid]

    async def purge(self, dice_result: int, grid: int):
        self.__player[(self.__current + RIVAL) % 2][grid] = [
            EMPTY if dice_result == dice else dice for dice in self.__player[(self.__current + RIVAL) % 2][grid]
        ]

    async def result(self, rival: int = EMPTY) -> list:
        from numpy import unique, multiply

        grid_info = []

        for grid in self.__player[(self.__current + rival) % 2]:
            distinct, multiple = unique(grid, return_counts=True)
            grid_info.append(sum(multiply(distinct, multiple ** 2)))

        return grid_info

    async def callback(self):
        pass
