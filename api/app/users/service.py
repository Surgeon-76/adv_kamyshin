from typing import Annotated

from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi_pagination import Params
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.repository import BaseRepository
from .schemas.user import (
    UserCreate,
    UserUpdate,
    UserView,
    UserResp,
    UserError,
    UserPage,
    UserPageError,
    UserDel
)

from .models.users import User
from config.sessions import get_session


class UserService(BaseRepository[User,
                                 UserView,
                                 UserCreate,
                                 UserUpdate]):
    def __init__(self, db_session: AsyncSession):
        super(UserService, self).__init__(User, db_session)

    async def list(self, params: Params, descend: bool = False):
        resp = await super().list(params, descend)
        return (UserPage(status_code=200,
                         payload=resp.items,
                         page=resp.page,
                         total=resp.total,
                         size=resp.size,
                         pages=resp.pages
                         )
                if resp.items
                else
                JSONResponse(status_code=404,
                             content=UserPageError(
                                 status_code=404).model_dump())
                )

    async def get_one(self, object_id: int):
        if resp := await super().get_one(object_id):
            return UserResp(status_code=200,
                            payload=UserView
                            .model_validate(resp))
        else:
            return JSONResponse(status_code=404,
                                content=UserError(
                                    status_code=404).model_dump())

    async def create(self, users: UserCreate):
        if resp := await super().create(users):
            return UserResp(status_code=201,
                            payload=UserView
                            .model_validate(resp))
        else:
            return JSONResponse(status_code=400,
                                content=UserError(
                                    status_code=400).model_dump())

    async def update(self, User_id: int, Users: UserCreate):
        if resp := await super().update(User_id, Users):
            return UserResp(status_code=200,
                            payload=UserView
                            .model_validate(resp))
        else:
            return JSONResponse(status_code=400,
                                content=UserError(
                                    status_code=400).model_dump())

    async def delete(self, object_id: int):
        return (UserResp(status_code=204,
                         payload=None)
                if await super().delete(object_id)
                else
                JSONResponse(status_code=400,
                             content=UserError(
                                status_code=400).model_dump())
                )


async def get_user_service(db_session: Annotated[AsyncSession,
                                                 Depends(get_session)]
                           ):
    return UserService(db_session)
