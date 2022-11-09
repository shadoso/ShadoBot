import nextcord
from nextcord.ext import commands
from abs_pth import filenames
from config.config import settings

WHERE = ["cogs"]

client = commands.Bot(
    intents=nextcord.Intents.all()
)

for filename in filenames(where=WHERE):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    print(f"{client.user} ta on")


client.run(settings.DISCORD_KEY)
