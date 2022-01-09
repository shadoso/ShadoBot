import discord
from key import password
from discord.ext import commands

bot = commands.Bot(command_prefix=">>")


@bot.event
async def on_ready():
    print(f"O pai ta on {bot.user}")


@bot.command()
async def ping(ctx):
    try:
        await ctx.send(f"**Pong**\n {(bot.latency * 1000):.2f} ms")

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


@bot.command()
async def fps(ctx):
    try:
        await ctx.send(f"**11 FPS ta lizinho!!!**")

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


@bot.command()
async def free(ctx):
    try:
        await ctx.send(f"Esses são os jogos gratis dessa semana na **Epic Games**\n",
                       file=discord.File('/home/bismutto/PycharmProjects/ShadoBot/epic_games/free_game.png'))
        await ctx.send("**Deseja pega-los ?**\nAcesse: https://www.epicgames.com/store/pt-BR/free-games")

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


@bot.command()
async def commands(ctx):
    try:
        await ctx.send("""Lista de comandos:
ping, fps, free
        """)

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")

bot.run(password())
