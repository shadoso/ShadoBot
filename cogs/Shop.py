import discord
from discord.ext import commands

DESCRIPTION = "Fiquei sabendo que você tem alguns Shadocoins :credit_card:"
VENDEDOR = "https://cdn.discordapp.com/attachments/935364491804303392/935382629782523944" \
           "/primary3APictures2FBell20Desenhos2FOliver20Icon20Bell_eightbit2.png "
COMPRAR = "> >>comprar tag `Otaku`\n> >>comprar feito `Hackeou a NASA com um Commodore 64`"
TAG = f"> Muda a TAG do perfil\n> Use **>>tags** para ver suas tags"
DEEDS = f"> Muda o grande feito do perfil\n> Use **>>feitos** para ver todos os seus feitos"
QUEIJO = "> Compra um Pão de queijo\n> Use **>>queijo** para ver quantos Pães de queijo você tem"


class Shop(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def loja(self, ctx):
        lojinha = discord.Embed(title="Oliver Thierry", description=DESCRIPTION, color=0xffc700)
        lojinha.set_thumbnail(url=VENDEDOR)
        lojinha.add_field(name="Exemplos de compras", value=COMPRAR, inline=False)
        lojinha.add_field(name="Tag :coin: 4,95", value=TAG, inline=False)
        lojinha.add_field(name="Grande feito :coin: 9,45", value=DEEDS, inline=False)
        lojinha.add_field(name="Pão de queijo :coin: 1", value=QUEIJO)
        return await ctx.send(embed=lojinha)


def setup(bot):
    bot.add_cog(Shop(bot))
