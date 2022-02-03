import discord
from features.database import Manager
from discord.ext import commands

# Character phrase ---------------------------------------------------------------------
CASINO_DESCRIPTION = "Bem vindo ao meu Cassino Bell Hill, fiquei sabendo que você tem alguns Shadocoins :credit_card:"
WALLET_DESCRIPTION = "Você possui $hα "
BAKERY_DESCRIPTION = "Bem vindo, Padaria do Bismutto, vai um cafezinho meu consagrado? :coffee:"
GANG_DESCRIPTION = "Fiquei sabendo por ai que você quer algumas tattoos :pen_ballpoint: ou talvez informações?"
# URLs ---------------------------------------------------------------------------------
BOSS = "https://cdn.discordapp.com/attachments/935364491804303392/935584332947525642" \
       "/primary3APictures2FBell20Desenhos2FOliver20Icon20Bell_eightbit3.png "
BAKER = "https://cdn.discordapp.com/attachments/935364491804303392/935410370510737408/Bismuto_Rosto_eightbit.png"
GANG = "https://cdn.discordapp.com/attachments/935364491804303392/935572429449875546" \
       "/primary3APictures2FBell20Desenhos2FAbigail20Icon20Bell_eightbit.png "
# Examples -----------------------------------------------------------------------------
EXAMPLES = "> **>>comprar tag** `Otaku`\n> **>>comprar feito** `Hackeou a NASA com um Commodore 64`"
# Item description ---------------------------------------------------------------------
TAG = f"> Muda a TAG do perfil\n> Use **>>tags** para ver suas tags"
DEEDS = f"> Muda o grande feito do perfil\n> Use **>>feitos** para ver todos os seus feitos"
CHEESE = "> Compra um Pão de queijo\n> Use **>>comida** para ver quantos Pães de queijo você tem"
PIZZA = "> Compra um Pizza de calabresa\n> Use **>>comida** para ver quantas Pizzas você tem"
SHRIMP = "> Compra uma Porção de camarão frito\n> Use **>>comida** para ver quantas Porções de camarão frito você tem"
COFFEE = "> Compra um Cafezinho\n> Use **>>comida** para ver quantos cafezinhos você tem"
JACK = f"> :slot_machine:\n> Use **>>jack** para apostar"
DICE = f"> :game_die:\n> Use **>>dados** para apostar"
DART = f"> :dart:\n> Use **>>dardos** para jogar"
# Others -------------------------------------------------------------------------------
BELL_DESCRIPTION = "Link para contato https://www.instagram.com/poferim/"
YUKI_DESCRIPTION = "Link para contato https://www.instagram.com/yuki1012__/"
MSG_NO_USER = "Usuário não registrado"
SHADOCOIN = 12


class Shop(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def loja(self, ctx):
        dcd_user_id = str(ctx.author.id)
        dcd_user_name = str(ctx.author.name)
        account = Manager(dcd_user_id, dcd_user_name)
        verify = account.verify_user()

        if verify is not bool:
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
            # MODIFICAR MODIFICAR
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
            casino.add_field(name="A Bell fez esse icon", value=BELL_DESCRIPTION)
            await ctx.send(embed=casino)

            bakery = discord.Embed(title="Bismutto", description=BAKERY_DESCRIPTION, color=0x90c0cb)
            bakery.set_thumbnail(url=BAKER)
            bakery.add_field(name="Pão de queijo :dollar: 1", value=CHEESE, inline=False)
            bakery.add_field(name="Cafezinho :dollar: 1,50", value=COFFEE, inline=False)
            bakery.add_field(name="Pizza de calabresa :dollar: 15", value=PIZZA, inline=False)
            bakery.add_field(name="Porção de camarão frito :dollar: 25", value=SHRIMP, inline=False)
            bakery.add_field(name="O Yuki fez esse icon", value=YUKI_DESCRIPTION)
            await ctx.send(embed=bakery)

            graffiti = discord.Embed(title="Abigail String", description=GANG_DESCRIPTION, color=0xfff1e8)
            graffiti.set_thumbnail(url=GANG)
            graffiti.add_field(name="Tag", value=TAG, inline=False)
            graffiti.add_field(name="Grande feito", value=DEEDS, inline=False)
            graffiti.add_field(name="A Bell fez esse icon", value=BELL_DESCRIPTION)
            return await ctx.send(embed=graffiti)
        else:
            return await ctx.send(MSG_NO_USER)


def setup(bot):
    bot.add_cog(Shop(bot))
