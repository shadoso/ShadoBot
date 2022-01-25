import discord
from features.database import Manager
from discord.ext import commands

CASINO_DESCRIPTION = "Bem vindo ao meu Cassino Bell Hill, fiquei sabendo que você tem alguns Shadocoins :credit_card:"
WALLET_DESCRIPTION = "Você possui $hα "
BAKERY_DESCRIPTION = "Bem vindo a Padaria do Bismutto, vai um cafezinho meu consagrado ? :coffee:"
HACKER_DESCRIPTION = "ERROR_404_NOT_FOUND " * 9
BOSS = "https://cdn.discordapp.com/attachments/935364491804303392/935382629782523944" \
       "/primary3APictures2FBell20Desenhos2FOliver20Icon20Bell_eightbit2.png "
BAKER = "https://cdn.discordapp.com/attachments/935364491804303392/935410370510737408/Bismuto_Rosto_eightbit.png"
HACKER = "https://cdn.discordapp.com/attachments/935364491804303392/935422018311036958/image3A31064_eightbit.png"
EXAMPLES = "> **>>comprar tag** `Otaku`\n> **>>comprar feito** `Hackeou a NASA com um Commodore 64`"
TAG = f"> Muda a TAG do perfil\n> Use **>>tags** para ver suas tags"
DEEDS = f"> Muda o grande feito do perfil\n> Use **>>feitos** para ver todos os seus feitos"
CHEESE = "> Compra um Pão de queijo\n> Use **>>comida** para ver quantos Pães de queijo você tem"
PIZZA = "> Compra um Pizza de calabresa\n> Use **>>comida** para ver quantas Pizzas você tem"
SHRIMP = "> Compra uma Porção de camarão frito\n> Use **>>comida** para ver quantas Porções de camarão frito você tem"
COFFEE = "> Compra um Cafezinho\n> Use **>>comida** para ver quantos cafezinhos você tem"
JACK = f"> :slot_machine:\n> Use **>>jack** para apostar"
DICE = f"> :game_die:\n> Use **>>dados** para apostar"
DART = f"> :dart:\n> Use **>>dardos** para jogar"
ORG = f"> Hacks the server and decodes the security hash-256 key"
MSG_NO_USER = "Usuário não registrado"
SHADOCOIN = 11


class Shop(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def loja(self, ctx):
        dcd_user_id = str(ctx.author.id)
        dcd_user_name = str(ctx.author.name)
        account = Manager(dcd_user_id, dcd_user_name)
        verify = account.verify_user()

        if verify:
            wallet = account.show_info()
            cash = discord.Embed(title="Carteira", description=WALLET_DESCRIPTION + wallet[SHADOCOIN], color=0xa2ff00)
            cash.set_author(name=dcd_user_name)
            cash.add_field(name="Exemplos de compras", value=EXAMPLES, inline=False)
            await ctx.send(embed=cash)

            casino = discord.Embed(title="Oliver Thierry", description=CASINO_DESCRIPTION, color=0xffc700)
            casino.set_thumbnail(url=BOSS)
            casino.add_field(name="Caça-níqueis", value=JACK, inline=False)
            casino.add_field(name="D120", value=DICE, inline=False)
            casino.add_field(name="Dardos", value=DART, inline=False)
            await ctx.send(embed=casino)

            bakery = discord.Embed(title="Bismutto", description=BAKERY_DESCRIPTION, color=0x90c0cb)
            bakery.set_thumbnail(url=BAKER)
            bakery.add_field(name="Pão de queijo :dollar: 1", value=CHEESE, inline=False)
            bakery.add_field(name="Cafezinho :dollar: 1,50", value=COFFEE, inline=False)
            bakery.add_field(name="Pizza de calabresa :dollar: 15", value=PIZZA, inline=False)
            bakery.add_field(name="Porção de camarão frito :dollar: 25", value=SHRIMP, inline=False)
            await ctx.send(embed=bakery)

            web = discord.Embed(title="ERROR_404_NOT_FOUND", description=HACKER_DESCRIPTION, color=0x1d2b53)
            web.set_thumbnail(url=HACKER)
            web.add_field(name=":unlock: CHANGE_ORG_USER :coin: 99.945,99", value=ORG, inline=False)
            await ctx.send(embed=web)

        else:
            return await ctx.send(MSG_NO_USER)


def setup(bot):
    bot.add_cog(Shop(bot))
