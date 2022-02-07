import datetime

import discord
from discord.ext import commands
from epic_games.free_game import FireFox

MSG_UPDATE = "Dia mudou, screenshot mudou, me da 5 segundos"
MSG_FREE = f"Esses são os jogos gratis dessa semana na **Epic Games**\n"
MSG_FREE_URL = "**Deseja pega-los ?**\nAcesse: https://www.epicgames.com/store/pt-BR/free-games"
PATH_FREE = "/home/bismutoso/PycharmProjects/ShadoBot/free_game.png"
PATH_WEEK = "/home/bismutoso/PycharmProjects/ShadoBot/DateOfWeek.txt"


class Web(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def epic(self, ctx):
        today = int(datetime.date.today().weekday())

        with open(PATH_WEEK, "r") as check_week:
            old = int(check_week.read())
            check_week.close()

            if today == 0 and old == 6 or today > old:
                with open(PATH_WEEK, "w") as replace_week:
                    replace_week.write(str(today))
                    replace_week.close()

                await ctx.send(MSG_UPDATE)
                web = FireFox("https://www.epicgames.com/store/pt-BR/free-games")
                web.open()
                web.screenshot()
                web.close()

        await ctx.send(MSG_FREE, file=discord.File(PATH_FREE))
        return await ctx.send(MSG_FREE_URL)


def setup(bot):
    bot.add_cog(Web(bot))
