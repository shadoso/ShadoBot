# Standard
from datetime import date
import this

# Local
from database.session import database_session
from database.models.users import Users, Actions, Backpack, Collectables, Display, Rank
from database.operations.users.verify import verify

COLLECTABLE_SIZE = 512
DEFAULT_COINS = 9945
EMPTY = 0
LIMITER_SIZE = 32
TAG_SIZE = 6
ZEN_END = 242
ZEN_START = 34

actions = {
    "commands": dict(),
    "limiter": list(EMPTY for _ in range(LIMITER_SIZE)),
    "luck": EMPTY,
    "tier": EMPTY,
    "daily": date.today(),
    "timer": date.today(),
}

backpack = {
    "dusts": EMPTY,
    "shards": EMPTY,
    "souls": EMPTY,
    "techs": EMPTY,
    "cores": EMPTY,
    "inventory": dict()
}

collectables = {
    "cards": list(False for _ in range(COLLECTABLE_SIZE)),
    "banners": list(False for _ in range(COLLECTABLE_SIZE)),
    "buddies": list(False for _ in range(COLLECTABLE_SIZE)),
    "tags": list(False for _ in range(COLLECTABLE_SIZE)),
}

display = {
    "card": EMPTY,
    "banner": EMPTY,
    "buddy": EMPTY,
    "tags": list(False for _ in range(TAG_SIZE)),
    "description": "".join(
        list(this.d[letter] if letter in this.d.keys() else letter for letter in this.s[ZEN_START:ZEN_END:])
    )
}

rank = {
    "ascension": EMPTY,
    "level": EMPTY,
    "exp": EMPTY,
}


async def create_user(discord_id: int, interaction):
    session = await database_session()

    exists = await verify(
        discord_id=discord_id,
        session=session
    )

    if not exists:
        user = Users(
            discord_id=discord_id,
            coins=DEFAULT_COINS,
            created=date.today()
        )
        user.actions = Actions(**actions)
        user.backpack = Backpack(**backpack)
        user.collectables = Collectables(**collectables)
        user.display = Display(**display)
        user.rank = Rank(**rank)

        session.add(user)
        await session.flush()
        await session.commit()
        await session.close()

        await interaction.response.send_message(":thumbsup:", delete_after=35)

    else:
        await session.close()
        await interaction.response.send_message(":clown:", delete_after=35)
