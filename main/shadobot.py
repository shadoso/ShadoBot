import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from absolute_path import cog_list
from config.config import settings
from error_warning.embed import error_embed
from error_warning.functions.warning import error_details, warning_trigger

client = commands.Bot(
    intents=nextcord.Intents.all()
)

client.load_extensions(names=cog_list())


@client.event
async def on_application_command_error(interaction: Interaction, exception):
    warning = await error_details(
        error=str(exception),
        command_name=interaction.application_command.name,
        command_type=interaction.application_command.type
    )
    await warning_trigger(*warning)
    embed = await error_embed(language=interaction.locale)
    await interaction.response.send_message(embed=embed)


@client.event
async def on_ready():
    print(f"{client.user} ta on")


client.run(settings.DISCORD_KEY)
