from typing import Annotated, Optional

from fastapi import (
    APIRouter,
    Body,
    Path,
    Query,
    status,
    Depends
)
from fastapi_pagination import (
    Params,
    add_pagination
)

# # from app.auth.services.get_user import get_current_user
from .services import (
    CategoryService,
    get_category_service
)
from . import schemas as cat_s


app = APIRouter(
    prefix='/api/v1/category',
    tags=['Категории:']
)


@app.get('/',
         summary='Список каетгорий',
         response_model=cat_s.CategoryPage,
         responses={
             200: {"model": cat_s.CategoryPage},
             404: {"model": cat_s.CategoryPageError}
             }
         )
async def get_users(*, descend: Annotated[bool, Query()] = False,
                    params: Annotated[Params, Depends()],
                    category_service: Annotated[CategoryService, Depends(
                        get_category_service)]
                    ):
    return await category_service.list(params, descend)


# @app.get('/{user_id}/',
#          summary='Пользователь по ID',
#          response_model=user.UserResp,
#         #  response_model_exclude_none=True,
#          responses={
#              200: {"model": user.UserResp},
#              404: {"model": user.UserError}
#              },
#          status_code=status.HTTP_200_OK
#          )
# async def get_user_one(user_id: Annotated[int, Path(ge=1)],
#                        user_service: Annotated[UserService, Depends(
#                            get_user_service)]
#                        ):
#     return await user_service.get_one(user_id)


# @app.post('/',
#           summary='Создание пользователя',
#           response_model=user.UserResp,
#           status_code=status.HTTP_201_CREATED,
#           responses={
#              201: {"model": user.UserResp},
#              400: {"model": user.UserError}
#              }
#           )
# async def user_create(users: Annotated[user.UserCreate, Body()],
#                       user_service: Annotated[UserService, Depends(
#                           get_user_service)],
#                     #   user_jwt: Annotated[str, Depends(get_current_user)]
#                       ):
#     return await user_service.create(users)


# @app.put('/{user_id}/',
#          summary='Редактирование пользователя с ID',
#          response_model=user.UserResp,
#          responses={
#              200: {"model": user.UserResp},
#              400: {"model": user.UserError}
#              }
#          )
# async def user_update(user_id: Annotated[int, Path(ge=1)],
#                       users: Annotated[user.UserUpdate, Body()],
#                       user_service: Annotated[UserService, Depends(
#                           get_user_service)],
#                       # user_jwt: Annotated[str, Depends(get_current_user)]
#                       ):
#     return await user_service.update(user_id, users)


# @app.delete('/{user_id}/',
#             summary='Удаление пользователя с ID',
#             response_model=user.UserDel,
#             responses={
#              400: {"model": user.UserError}
#              }
#             )
# async def user_delete(user_id: Annotated[int, Path()],
#                       user_service: Annotated[UserService, Depends(
#                           get_user_service)],
#                     #   user_jwt: annotated[str, Depends(get_current_user)]
#                       ):
#     return await user_service.delete(user_id)


add_pagination(app)
