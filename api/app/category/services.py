from typing import Annotated

from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi_pagination import Params
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.repository import BaseRepository
from .schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryView,
    CategoryResp,
    CategoryError,
    CategoryPage,
    CategoryPageError,
    CategoryDel
)

from .model import Category
from config.sessions import get_session


class CategoryService(BaseRepository[Category,
                                     CategoryView,
                                     CategoryCreate,
                                     CategoryUpdate]):
    def __init__(self, db_session: AsyncSession):
        super(CategoryService, self).__init__(Category, db_session)

    async def list(self, params: Params, descend: bool = False):
        resp = await super().list(params, descend)
        return (CategoryPage(status_code=200,
                             payload=resp.items,
                             page=resp.page,
                             total=resp.total,
                             size=resp.size,
                             pages=resp.pages
                             )
                if resp.items
                else
                JSONResponse(status_code=404,
                             content=CategoryPageError(
                                 status_code=404).model_dump())
                )

    async def get_one(self, object_id: int):
        if resp := await super().get_one(object_id):
            return CategoryResp(status_code=200,
                                payload=CategoryView
                                .model_validate(resp))
        else:
            return JSONResponse(status_code=404,
                                content=CategoryError(
                                    status_code=404).model_dump())

    async def create(self, Categorys: CategoryCreate):
        if resp := await super().create(Categorys):
            return CategoryResp(status_code=201,
                                payload=CategoryView
                                .model_validate(resp))
        else:
            return JSONResponse(status_code=400,
                                content=CategoryError(
                                    status_code=400).model_dump())

    async def update(self, Category_id: int, Categorys: CategoryCreate):
        if resp := await super().update(Category_id, Categorys):
            return CategoryResp(status_code=200,
                                payload=CategoryView
                                .model_validate(resp))
        else:
            return JSONResponse(status_code=400,
                                content=CategoryError(
                                    status_code=400).model_dump())

    async def delete(self, object_id: int):
        return (CategoryResp(status_code=204,
                             payload=None)
                if await super().delete(object_id)
                else
                JSONResponse(status_code=400,
                             content=CategoryError(
                                status_code=400).model_dump())
                )


async def get_category_service(db_session: Annotated[AsyncSession,
                                                     Depends(get_session)]
                               ):
    return CategoryService(db_session)
