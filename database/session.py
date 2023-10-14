# Third-party
from sqlalchemy.exc import OperationalError

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

# Local
from database.models.names import Base

# Configuration
from config.config import settings as env

engine = create_async_engine(
    url=f"postgresql+asyncpg://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:"
        f"{env.DATABASE_PORT}/{env.DATABASE_NAME}"
)
session_maker = async_sessionmaker(
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
)


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def database():
    try:
        async with session_maker() as session:
            yield session.begin()

    except OperationalError as database_error:
        print(database_error)

    finally:
        await session.close()
