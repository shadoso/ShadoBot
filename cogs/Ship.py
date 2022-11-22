from abs_pth import json_text, root_path
import requests
from PIL import Image
from nextcord import Interaction, SlashOption, Embed
from nextcord.ext import commands
import nextcord

where = ["app", "languages", "ship.json"]
command = ["ship", "crush", "who", "responses", "compatibility"]

slash = json_text(where=where, commands=command)
LEFT = root_path(where=["app", "sources", "LeftHeart.png"])
RIGHT = root_path(where=["app", "sources", "RightHeart.png"])


class Ship(commands.Cog):
    def __init__(self, client):
        self.__client = client

    @staticmethod
    async def get_ship(who: str, crush: str):
        default = "default"
        hash_int = 101
        hash_float = 100
        valid = {
            "0": "4", "1": "4", "2": "4", "3": "4",
            "5": "9", "6": "9", "7": "9", "8": "9",
        }
        jump = 2
        start_int = jump
        start_float = 4
        last_element = -1

        percentage = (int(who[start_int::jump]) + int(crush[start_int::jump])) % hash_int
        decimal = ((int(who[start_float::jump]) + int(crush[start_float::jump])) % hash_float) / hash_float
        key = str(percentage)

        # Only adds decimals if smaller than 100
        if percentage < hash_float:
            percentage += decimal

        # Check if is a valid number
        if key not in slash.responses[default].keys():
            key = key[:last_element] + valid[key[last_element]]

        return [f"{percentage:.2f}", key]

    @staticmethod
    async def couple(crush: str, who: str):
        img = Image.new("RGBA", (512, 512), 0)
        with Image.open(requests.get(url=crush, stream=True).raw) as crush_img:
            crush_img = crush_img.resize((512, 512))
            with Image.open(LEFT).convert("RGBA") as l_mask:
                img.paste(crush_img, (0, 0), l_mask)

        with Image.open(requests.get(url=who, stream=True).raw) as who_img:
            who_img = who_img.resize((512, 512))
            with Image.open(RIGHT).convert("RGBA") as r_mask:
                img.paste(who_img, (0, 0), r_mask)

        file = root_path(where=["app", "sources", "Edited.png"])
        img.convert("RGBA")
        img.save(file)

        return file

    @nextcord.slash_command(**slash.ship)
    async def ship(self,
                   interaction: Interaction,
                   crush: nextcord.Member = SlashOption(
                       **slash.crush,
                       required=True),
                   who: nextcord.Member = SlashOption(
                       **slash.who,
                       required=False)
                   ):

        default = "default"

        if who:
            percentage, key = await self.get_ship(
                who=str(who.id),
                crush=str(crush.id)
            )
        else:
            who = interaction.user
            percentage, key = await self.get_ship(
                who=str(who.id),
                crush=str(crush.id)
            )

        if interaction.locale in slash.responses.keys():
            middle_embed = Embed(
                title=f"{slash.compatibility[interaction.locale]}: {percentage}%\n{crush.name} + {who.name}",
                description=slash.responses[interaction.locale][key]
            )
            file = await self.couple(crush=crush.avatar.url, who=who.avatar.url)

            if file:
                file = nextcord.File(file, filename="image.png")
                middle_embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=middle_embed)

        else:
            middle_embed = Embed(
                title=f"{slash.compatibility[default]}: {percentage}%\n{crush.name} + {who.name}",
                description=slash.responses[default][key]
            )
            file = await self.couple(crush=crush.avatar.url, who=who.avatar.url)

            if file:
                file = nextcord.File(file, filename="image.png")
                middle_embed.set_image(url="attachment://image.png")
                await interaction.response.send_message(file=file, embed=middle_embed)


def setup(client):
    client.add_cog(Ship(client))
