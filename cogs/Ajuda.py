from discord.ext import commands

PING = 1000
HELP = {"comprar": """ Exemplos de compras
>>comprar cafe
>>comprar feito
""",
        "trocar": """ Exemplos de trocas
>>trocar tag {TAG DESEJADA}
>>trocar feito {Descrição do feito}
        """}


class Ajuda(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def ajuda(self, ctx, msg):
        try:
            return await ctx.send(HELP[msg])

        except Exception as CommandNotFound:
            print(CommandNotFound)
            return await ctx.send(f"Use apenas, comprar, trocar")


def setup(bot):
    bot.add_cog(Ajuda(bot))
