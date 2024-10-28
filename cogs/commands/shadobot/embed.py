from nextcord import Embed



async def ai_embed(question: str, message: str):
        embed = Embed(title=f"{question}")
        embed.add_field(
            name="",
            value=message
        )

        return embed
