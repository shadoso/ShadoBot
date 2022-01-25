from discord.ext import commands

PING = 1000
CMD_TEXT = """Lista de comandos:
ping: Retorna o ping do bot
fps: Quantos fps são necessários para rodar liso
epic: Mostra os jogos grais da epic games
senha: Cria uma senha com a palavra digitada (Experimental ainda, use so uma palavra e tudo em minusculo)
criar: Cria seu perfil no Shadosoverso
perfil: Mostra seu perfil no Shadosoverso
        """
MSG_BOT_ERROR = "O bot ta pegando fogo bixo!"
MSG_FPS = "**11 FPS ta lizinho!!!**"


# Commands should use @commands.command and an event should use @commands.Cog.listener

class TextCommands(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def cmd(self, ctx):
        return await ctx.send(CMD_TEXT)

    @commands.command()
    async def fps(self, ctx):
        return await ctx.send(MSG_FPS)

    @commands.command()
    async def ping(self, ctx):
        return await ctx.send(f"**Pong**\n {(self.__bot.latency * PING):.2f} ms")


def setup(bot):
    bot.add_cog(TextCommands(bot))
