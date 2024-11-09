from absolute_path import cog_response
from algorithms.formulas import equation_straight_line as category
from config.constants import NAME_, URL_, TEXT_, KEYWORDS_, DESCRIPTION_, TOKEN_
from embed_recovery.token_handling import create_tarot_token
from languages.check_language import verify_language
from nextcord import Embed
import asyncio

TAROT = cog_response(__file__)
TAROT_DEFAULT = cog_response(
    file_path=__file__,
    json_name="tarot.json"
)


async def tarot_embed_default(
        language: str,
        cards: list[int],
        flip_side: list[int],
        style: str
        ) -> [Embed]:

    embeds = []
    language = await verify_language(
        language=language,
        language_keys=TAROT_DEFAULT.text_field
    )

    for index, card_number in enumerate(cards):
        group = str(int(category(
            first_interval=[22, 1],
            second_interval=[36, 2],
            variable=card_number
        )))
        card_side = str(flip_side[index])
        position = str(index)
        card_number = str(card_number)

        embed = Embed(title=TAROT_DEFAULT.category[group][language])
        embed.set_image(TAROT_DEFAULT.url[group])
        embed.add_field(
            name=TAROT_DEFAULT.name[style][position][language],
            value=TAROT_DEFAULT.choice[style][position][language]
        )
        embeds.append(embed)
        embed = Embed(title=TAROT.cards[card_number][NAME_][language])
        embed.add_field(
            name=TAROT_DEFAULT.key_field[language],
            value=TAROT.cards[card_number][DESCRIPTION_][card_side][KEYWORDS_][language],
            inline=False
        )
        embed.add_field(
            name=TAROT_DEFAULT.text_field[language],
            value=TAROT.cards[card_number][DESCRIPTION_][card_side][TEXT_][language],
            inline=False
        )
        embed.set_image(TAROT.cards[card_number][URL_])

        embeds.append(embed)

    embed_token = await create_tarot_token(
        language=language,
        cards=cards,
        style=style,
        flip_side=flip_side
    )

    embed = Embed(title=TOKEN_, description=embed_token)
    embeds.append(embed)
    return embeds


async def tarot_embed_rpg(
        language: str,
        cards: list[int],
        flip_side: list[int],
        style: str
        ) -> [Embed]:

    embeds = []
    language = await verify_language(language=language)

    for index, card_number in enumerate(cards):
        group = str(int(category(
            first_interval=[22, 1],
            second_interval=[36, 2],
            variable=card_number
        )))
        card_side = str(flip_side[index])
        position = str(index)
        card_number = str(card_number)

        embed = Embed(title=TAROT_DEFAULT.category[group][language])
        embed.set_image(TAROT_DEFAULT.url[group])
        embed.add_field(
            name=TAROT_DEFAULT.name[style][position][language],
            value=TAROT_DEFAULT.choice[style][position][language]
        )
        embeds.append(embed)
        embed = Embed(title=TAROT.cards[card_number][NAME_][language])
        embed.add_field(
            name=TAROT_DEFAULT.key_field[language],
            value=TAROT.cards[card_number][DESCRIPTION_][card_side][KEYWORDS_][language],
            inline=False
        )
        embed.add_field(
            name=TAROT_DEFAULT.text_field[language],
            value=TAROT.cards[card_number][DESCRIPTION_][card_side][TEXT_][language],
            inline=False
        )
        embed.set_image(TAROT.cards[card_number][URL_])

        embeds.append(embed)

    embed_token = await create_tarot_token(
        language=language,
        cards=cards,
        style=style,
        flip_side=flip_side
    )

    embed = Embed(title=TOKEN_, description=embed_token)
    embeds.append(embed)
    return embeds


if __name__ == "__main__":
    emb = asyncio.run(tarot_embed_default(
        language="batatat",
        cards=[1, 15, 45],
        flip_side=[1, -1, 1],
        style="acceptance",
    ))
    print(emb[6].to_dict())
