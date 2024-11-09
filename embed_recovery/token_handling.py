from jose import jwt, JWTError
from config.config import settings
import asyncio

REMOVE_EXTRA1 = "**```"
REMOVE_EXTRA2 = "```**"


async def create_tarot_token(language, cards, style, flip_side):
    tarot = {
        "language": language,
        "cards": cards,
        "style": style,
        "flip_side": flip_side
    }
    message = f"**```{jwt.encode(claims=tarot.copy(), key=settings.SECRET_KEY, algorithm=settings.HASH_ALGORITHM)}```**"
    return message


async def verify_token(jwt_token):
    try:
        token = jwt_token.replace(REMOVE_EXTRA1, "")
        token = token.replace(REMOVE_EXTRA2, "")

        return jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=settings.HASH_ALGORITHM)

    except JWTError:
        return None


if __name__ == "__main__":
    testt = asyncio.run(create_tarot_token(
        language="br",
        cards=[15, 25, 45],
        style="lurk",
        flip_side=[-1, 1, -1]
    ))
    veri = asyncio.run(verify_token(jwt_token=testt))
    print(veri)
