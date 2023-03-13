import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from abs_pth import filenames
from config.config import settings
from app.main.error_handling.embed import GlobalError
from abs_pth import json_text
from error_handling.functions.get_error import TelegramWarning

WHERE = ["cogs"]

client = commands.Bot(
    intents=nextcord.Intents.all()
)

for filename in filenames(where=WHERE):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_application_command_error(interaction: Interaction, exception):
    root_path = ["app", "main", "error_handling", "text", "response.json"]
    text = ["response"]
    elements = json_text(where=root_path, commands=text)
    embed = await GlobalError(**elements.response).embeding(language=interaction.locale)
    warning = TelegramWarning(
        error=exception,
        command_name=interaction.application_command.name,
        command_type=interaction.application_command.type
    )
    await warning.warning_trigger()
    await interaction.response.send_message(embed=embed)


@client.event
async def on_ready():
    print(f"{client.user} ta on")


client.run(settings.DISCORD_KEY)
