from discord.ext import commands
from app.old_not_in_use.features.password import Generator

MSG_MISSING = "Ta faltando a palavra"


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def senha(self, ctx, msg=None):
        if msg is None:
            return await ctx.send(MSG_MISSING)

        else:
            gen = Generator(msg)
            return await ctx.send(gen.phrase())


def setup(bot):
    bot.add_cog(Entertainment(bot))
