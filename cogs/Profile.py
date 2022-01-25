import gspread
import discord
from discord.ext import commands
from google.oauth2.service_account import Credentials

SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
PATH = "/home/bismutoso/PycharmProjects/ShadoBot/key/shadobot-key.json"
MSG_UNIVERSE = "O universo é pequeno demais para contemplar seu maior feito!"
MSG_FOUND_USER = "Você já tem uma conta"
MSG_NEW_USER = "Conta criada no Shadosoverso"
MSG_NO_USER = "Campo invalido ou usuário não registrado"

DEEDS1 = 5
DESCRIPTION = 2
HOUSE = 3
SHADOCOIN = 11
TAG = 4


class Manager:
    def __init__(self, discord_id, name):
        scopes = SCOPE
        credentials = Credentials.from_service_account_file(PATH, scopes=scopes)
        gc = gspread.authorize(credentials)

        self.__open = gc.open("Shadobot").sheet1
        self.__discord_id = discord_id
        self.__name = name

    def create_user(self):
        user = [
            self.__discord_id,
            self.__name,
            "Novo usuário",
            "None",
            "None",
            "Criou uma conta",
            "None",
            "None",
            "None",
            "None",
            "None",
            9.45,
        ]

        self.__open.insert_row(user, 2)
        return True

    def verify_user(self):
        local = self.__open.find(self.__discord_id)
        return True if local is not None else False

    def show_info(self):
        info = self.__open.find(self.__discord_id)
        return self.__open.row_values(info.row)


class Profile(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def perfil(self, ctx):
        dcd_user_id = str(ctx.author.id)
        dcd_user_name = str(ctx.author.name)
        dcd_user_avatar = str(ctx.author.avatar)
        account = Manager(dcd_user_id, dcd_user_name)
        verify = account.verify_user()

        if verify:
            info = account.show_info()
            color_shadocoin = str(f"```yaml\n$hα {info[SHADOCOIN]}```")
            banner = discord.Embed(title="Descrição", description=info[DESCRIPTION], color=0xa2ff00)
            banner.set_thumbnail(url=dcd_user_avatar)
            banner.set_author(name=dcd_user_name)
            banner.add_field(name="Casa", value=info[HOUSE], inline=True)
            banner.add_field(name="Tag", value=info[TAG], inline=True)
            banner.add_field(name="Shadocoins", value=color_shadocoin, inline=True)
            banner.add_field(name=MSG_UNIVERSE, value=info[DEEDS1])
            return await ctx.send(embed=banner)

        else:
            return await ctx.send(MSG_NO_USER)

    @commands.command()
    async def criar(self, ctx):
        dcd_user_id = str(ctx.author.id)
        dcd_user_name = str(ctx.author.name)
        account = Manager(dcd_user_id, dcd_user_name)
        verify = account.verify_user()

        if verify:
            return await ctx.send(MSG_FOUND_USER)

        else:
            account.create_user()
            return await ctx.send(MSG_NEW_USER)


def setup(bot):
    bot.add_cog(Profile(bot))
