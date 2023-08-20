from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine

from .settings import settings


SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"
# print('settings.docker = ', settings.docker, 'in database')

if settings.docker:
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@db:5432/{settings.postgres_db}"
    )
# print(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)


class Base(DeclarativeBase):
    pass
