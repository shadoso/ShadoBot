import discord
from discord.ext import commands

MSG_FREE = f"Esses são os jogos gratis dessa semana na **Epic Games**\n"
MSG_FREE_URL = "**Deseja pega-los ?**\nAcesse: https://www.epicgames.com/store/pt-BR/free-games"
PATH_FREE = "/home/bismutoso/PycharmProjects/ShadoBot/free_game.png"


class WebSelenium(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def epic(self, ctx):
        await ctx.send("COMANDO EM MANUTENÇÃO   ")
        await ctx.send(MSG_FREE, file=discord.File(PATH_FREE))
        return await ctx.send(MSG_FREE_URL)


def setup(bot):
    bot.add_cog(WebSelenium(bot))
