# Standard
from contextlib import asynccontextmanager

# Third-party
from sqlalchemy.exc import OperationalError

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

# Local
from database.models.countries import Base as Countries
from database.models.names import Base as Names
from database.models.numbers import Base as Numbers
# from database.models.users import Base as Users

# Configuration
from config.config import settings as env

TABLES = [Numbers, Countries, Names]

engine = create_async_engine(
    url=f"postgresql+asyncpg://{env.POSTGRES_USER}:{env.DATABASE_PASSWORD}@{env.POSTGRES_HOSTNAME}:"
        f"{env.POSTGRES_PORT}/{env.POSTGRES_DB}"
)
session_maker = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)


async def create_tables():
    async with engine.begin() as connection:
        for table in TABLES:
            await connection.run_sync(table.metadata.create_all)


@asynccontextmanager
async def database_session():
    async with session_maker() as session:
        try:
            yield session
        except OperationalError as database_error:
            await session.rollback()
            print(f"Erro de operação no banco de dados: {database_error}")

#EDIT

# async def database_unique_session(user_id: int):
#     if user_id not in active_sessions.keys():
#         try:
#             async with session_maker() as session:
#                 active_sessions[user_id] = session
#                 return session
#
#         except OperationalError as database_error:
#             session = active_sessions.pop(user_id)
#             await session.rollback()
#             print(database_error)
#
#     else:
#         return None
#
#
# async def database_delete_session(user_id: int):
#     if user_id in active_sessions.keys():
#         session = active_sessions.pop(user_id)
#         await session.close()
#
#     else:
#         return None
