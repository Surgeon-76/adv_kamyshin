from sqlalchemy import (
    or_,
    select
)
from sqlalchemy.ext.asyncio import AsyncSession

from ..users.models.client import Client
from ..users.models.manager import Manager


async def get_user_by_email_or_phone(username: str, db: AsyncSession):
    return (((await db.execute(select(Client)
                               .where(or_(Client.email == username,
                                          Client.phone == username)))).first())
            or
            ((await db.execute(select(Manager)
                               .where(Manager.email == username))).first()))
