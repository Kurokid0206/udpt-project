from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.configs.base import settings

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# from sql-model import SQLModel


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    try:
        session = localSession()

        yield session
    finally:
        session.close()
