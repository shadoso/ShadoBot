from sqlalchemy import select
from database.models.users import Users


async def verify(discord_id: int, session):
    query = select(Users).where(Users.discord_id == discord_id)
    query = await session.execute(statement=query)

    if query.scalar():
        await session.close()
        return True
