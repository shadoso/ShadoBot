import discord
from discord.ext import commands
from app.old_not_in_use.features.database import Manager

# Text ----------------------------------------------------------------
MSG_UNIVERSE = "O universo é pequeno demais para contemplar seu maior feito!"
MSG_FOUND_USER = "Você já tem uma conta"
MSG_NEW_USER = "Conta criada no Shadosoverso"
MSG_NO_USER = "Campo invalido ou usuário não registrado"
# Index values --------------------------------------------------------
INDEX = 0
DEEDS1 = 6
DESCRIPTION = 2
ORG = 3
SHADOCOIN = 11
TAG = 5


class Profile(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def perfil(self, ctx):
        account = Manager(str(ctx.author.id), str(ctx.author.name))
        verify = account.verify_user()

        if verify is not None:
            color_shadocoin = str(f"```yaml\n$hα {verify[INDEX][SHADOCOIN]}```")
            banner = discord.Embed(title="Descrição", description=verify[INDEX][DESCRIPTION], color=0xa2ff00)
            banner.set_thumbnail(url=str(ctx.author.avatar))
            banner.set_author(name=ctx.author.name)
            banner.add_field(name="Organização", value=verify[INDEX][ORG], inline=True)
            banner.add_field(name="Tag", value=verify[INDEX][TAG], inline=True)
            banner.add_field(name="Shadocoins", value=color_shadocoin, inline=True)
            banner.add_field(name=MSG_UNIVERSE, value=verify[INDEX][DEEDS1])
            account.close_query()
            return await ctx.send(embed=banner)

        else:
            account.close_query()
            return await ctx.send(MSG_NO_USER)

    @commands.command()
    async def criar(self, ctx):
        account = Manager(str(ctx.author.id), str(ctx.author.name))
        verify = account.verify_user()

        if verify is not None:
            account.close_query()
            return await ctx.send(MSG_FOUND_USER)

        else:
            account.create_user()
            account.close_query()
            return await ctx.send(MSG_NEW_USER)


def setup(bot):
    bot.add_cog(Profile(bot))
