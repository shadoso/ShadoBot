from discord.ext import commands
from web_epic.selenium_epic import ShadoDriver
import discord

bot = commands.Bot(command_prefix=">")


@bot.command()
async def ping(ctx):
    await ctx.send(f"**Pong**\n {(bot.latency * 1000):.2f} ms")


@bot.command()
async def fps(ctx):
    await ctx.send(f"**11 FPS ta lizinho!!!**")


@bot.command()
async def up(ctx):
    url = "https://www.epicgames.com/store/pt-BR/free-games"

    img = ShadoDriver(url)
    img.open()
    img.scree_it()
    img.close_it()

    await ctx.send(file=discord.File("/home/bismutto/PycharmProjects/ShadoBot/web_epic/free_game.png"))


@bot.command()
async def free(ctx):
    await ctx.send(f"Esses são os jogos gratis dessa semana na **Epic Games**\n",
                   file=discord.File('/home/bismutto/PycharmProjects/ShadoBot/web_epic/free_game.png'))
    await ctx.send("**Deseja pega-los ?**\nAcesse: https://www.epicgames.com/store/pt-BR/free-games")


bot.run("ODg2NjA0OTY4MDgwMDY4Njc5.YT4BOA.lBiIim5IXFkyP5KlvvjgXw19lMs")
