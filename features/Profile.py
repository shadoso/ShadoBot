# Third-party
from nextcord import Interaction

from nextcord.ext import commands

import nextcord

# Local
from absolute_path import cog_description

from database.operations.users.create import create_user


PROFILE_SLASH = cog_description(file_path=__file__)


class Profile(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @nextcord.slash_command(**PROFILE_SLASH.create)
    async def create(self,
                     interaction: Interaction
                     ):
        await create_user(
            discord_id=interaction.user.id,
            interaction=interaction
        )


def setup(client):
    client.add_cog(Profile(client))
