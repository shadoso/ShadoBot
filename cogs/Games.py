from secrets import randbelow
from discord.ext import commands
from features.database import Manager

INDEX = 0
SHADOCOIN = 11
DICE_SIZE = 120
ONE = 1


class Game(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def dados(self, ctx, msg=25.00):
        discord_id = str(ctx.author.id)
        discord_name = str(ctx.author.name)
        account = Manager(discord_id, discord_name)
        verify = account.verify_user()

        if verify is not None:
            dice = randbelow(DICE_SIZE) + ONE
            cash = float(verify[INDEX][SHADOCOIN])
            if cash >= msg:
                if DICE_SIZE == dice:
                    return await ctx.send("Ganhou Caralhooooo")

                if DICE_SIZE != dice:
                    return await ctx.send(f"Não foi dessa vez... me passa o :credit_card: hehehe\n:game_die:{dice}")

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
