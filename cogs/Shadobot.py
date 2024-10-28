from absolute_path import cog_description
from cogs.base.command import BaseCommand
from languages.check_language import verify_language

from nextcord import Interaction, SlashOption
import nextcord

from commands.shadobot.embed import ai_embed
from commands.shadobot.functions.shadobot_AI import generate_text

SHADOBOT_SLASH = cog_description(file_path=__file__)

TEMP_ = {
    "pt_BR": "Temporary"
}

class Shadobot(BaseCommand):
    def __init__(self, client):
        super().__init__(client, delete_after=None)

    @nextcord.slash_command(**SHADOBOT_SLASH.bot)
    async def shadobot(self,):
        pass

    # @shadobot.subcommand()
    # async def task(self):
    #     pass

    @shadobot.subcommand()
    async def talk(self,
                   interaction: Interaction,
                   question: str = SlashOption(
                       **SHADOBOT_SLASH.question,
                       required=True
                   )
                   ):

        language = await verify_language(
            language=interaction.locale,
            language_keys=TEMP_
        )
        message = await generate_text(
            question=question,
            language=language
        )

        embed = await ai_embed(
            question=question,
            message=message["messages"][-1]["content"]
        )
        await self.send_response(interaction, embed=embed)

def setup(client):
    client.add_cog(Shadobot(client))