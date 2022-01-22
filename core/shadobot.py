import discord
from key.tokens import password
from discord.ext import commands
from users.sheets import Manager
from diversos.Password import Generator
from epic_games.free_game import FireFox

# Update the image
# web = FireFox("https://www.epicgames.com/store/pt-BR/free-games")
# web.open()
# web.screenshot()
# web.close()
# ----------------

bot = commands.Bot(command_prefix=">>")


@bot.event
async def on_ready():
    print(f"O pai ta on {bot.user}")


@bot.command()
async def cmd(ctx):
    try:
        await ctx.send("""Lista de comandos:
ping: Retorna o ping do bot
fps: Quantos fps são necessários para rodar liso
free: Mostra os jogos grais da epic games
senha: Cria uma senha com a palavra digitada (Experimental ainda, use so uma palavra e tudo em minusculo)
        """)

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


@bot.command()
async def perfil(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.name
    user_avatar = ctx.author.avatar

    account = Manager(str(user_id), user_name)

    try:
        info = account.show_user()
        shadocoins = str(f"```yaml\n$hα {info[11]}```")
        result = discord.Embed(title="Descrição", description=info[2], color=0xa2ff00)
        result.set_author(name=user_name)
        result.set_thumbnail(url=user_avatar)
        result.add_field(name="Casa", value=info[3], inline=True)
        result.add_field(name="Tag", value=info[4], inline=True)
        result.add_field(name="Shadocoins", value=shadocoins, inline=True)
        result.add_field(name=f"O universo é pequeno demais para contemplar seu maior feito! ", value=info[5])

        return await ctx.send(embed=result)

    except Exception as UserNotFound:
        print(UserNotFound)
        return await ctx.send(f"Campo invalido ou usuário não registrado")


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
                       file=discord.File("/home/bismutoso/PycharmProjects/ShadoBot/free_game.png"))
        await ctx.send("**Deseja pega-los ?**\nAcesse: https://www.epicgames.com/store/pt-BR/free-games")

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


@bot.command()
async def senha(ctx, msg=None, debug="False"):
    try:
        if debug == "False":
            debug = False

        if debug == "True":
            debug = True

        if msg is None:
            return await ctx.send("Ta faltando a palavra")

        elif type(debug) is not bool:
            return await ctx.send(f"Depois da palavras coloque True ou deixe o campo vazio.")

        gen = Generator(msg, debug)
        await ctx.send(gen.phrase())

    except Exception as glitch:
        return await ctx.send(f"O bot ta pegando fogo bixo, {glitch}")


bot.run(password())
