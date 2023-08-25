from sqlalchemy import (
    or_,
    select
)
from sqlalchemy.ext.asyncio import AsyncSession

from ..users.models.users import User


async def get_user_by_id(userid: str, db: AsyncSession):
    return ((await db.execute(select(User)
                               .where(or_(User.google_id == userid,
                                          User.yandex_id == userid,
                                          User.telegram_id == userid,
                                          User.vk_id == userid)))).first())
           
