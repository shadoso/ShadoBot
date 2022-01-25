import os
from discord.ext import commands
from key.tokens import password

COMMAND_LIST = []

bot = commands.Bot(command_prefix=">>")


@bot.event
async def on_ready():
    print(f"O pai ta on {bot.user}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        COMMAND_LIST.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for command in COMMAND_LIST:
        bot.load_extension(command)


bot.run(password())
