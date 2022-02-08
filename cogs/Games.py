import discord
from secrets import randbelow
from discord.ext import commands
from features.database import Manager

DICE_DESCRIPTION = "**Não foi dessa vez... me passa o :credit_card: hehehe**"
WIN_DESCRIPTION = "**Não pode ser... o coração dos dados!!!**"
BACK_DECRIPTION = "**Puts... olha pra você não falar que eu nunca te ajudei toma o dinheiro de volta :credit_card:**"
LOSE = "https://cdn.discordapp.com/attachments/935364491804303392/940466618432094208/TK_Sticker.gif"
WIN = "https://cdn.discordapp.com/attachments/935364491804303392/940466807674925116/Poppy_Sticker.gif"
BACK = "https://cdn.discordapp.com/attachments/935364491804303392/940470569978167357/Sad_Poro_Sticker.gif"
MULTIPLIER = 25
INDEX = 0
SHADOCOIN = 11
DICE_SIZE = 120
ONE = 1


class Game(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def dados(self, ctx, msg=25.00):
        account = Manager(str(ctx.author.id), str(ctx.author.name))
        verify = account.verify_user()

        if verify is not None:
            dice = randbelow(DICE_SIZE) + ONE
            cash = float(verify[INDEX][SHADOCOIN])
            if cash >= msg:

                if DICE_SIZE == dice:
                    prize = msg * MULTIPLIER
                    dices = discord.Embed(title=f"**:game_die: {dice}**", description=WIN_DESCRIPTION, color=0xffc700)
                    dices.add_field(name="Prêmio", value=f"**:credit_card: {prize:.2f}**")
                    dices.set_thumbnail(url=WIN)
                    return await ctx.send(embed=dices)

                if ONE == dice:
                    dices = discord.Embed(title=f"**:game_die: {dice}**", description=BACK_DECRIPTION, color=0xffc700)
                    dices.set_thumbnail(url=BACK)
                    return await ctx.send(embed=dices)

                elif DICE_SIZE != dice:
                    dices = discord.Embed(title=f"**:game_die: {dice}**", description=DICE_DESCRIPTION, color=0xffc700)
                    dices.set_thumbnail(url=LOSE)
                    return await ctx.send(embed=dices)

            else:
                return await ctx.send("Essa aposta ta grande D+ pro seu bolso")
        else:
            return await ctx.send("Se cadastra primeiro :v")

    @commands.command()
    async def jack(self, ctx):
        pass

    @commands.command()
    async def dardos(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Game(bot))
