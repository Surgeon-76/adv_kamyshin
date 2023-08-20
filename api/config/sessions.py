from sqlalchemy.ext.asyncio import async_sessionmaker

from .database import engine


async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
