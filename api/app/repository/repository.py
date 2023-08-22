from typing import (
    Generic,
    Type,
    TypeVar
)
from dataclasses import dataclass

from fastapi import status
from fastapi_pagination import Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from pydantic import BaseModel
from sqlalchemy import (
    desc,
    update,
    delete
)
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from config.database import Base


ModelType = TypeVar('ModelType', bound=Base)
GetSchemaType = TypeVar('GetSchemaType', bound=BaseModel)
CreateSchemaType = TypeVar('CreateSchemaType', BaseModel, dataclass)
UpdateSchemaType = TypeVar('UpdateSchemaType', BaseModel, dataclass)


class BaseRepository(Generic[ModelType,
                             GetSchemaType,
                             CreateSchemaType,
                             UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.table = model
        self.db_session = db_session

    async def list(self, params: Params, descend: bool = False):

        match descend:
            case True:
                return (
                    await paginate(
                        self.db_session,
                        select(self.table).order_by(desc(self.table.id)),
                        params)
                    )
            case _:
                return (
                    await paginate(
                        self.db_session,
                        select(self.table).order_by(self.table.id), params)
                    )

    async def get_one(self, object_id: int):
        return await self.db_session.get(self.table, object_id)

    async def create(self, object: CreateSchemaType):
        try:
            db_instance = self.table(**object.model_dump())
            self.db_session.add(db_instance)
            await self.db_session.commit()
        except IntegrityError:
            await self.db_session.rollback()
            return None
        return db_instance

    async def update(self, object_id: int, object: UpdateSchemaType):
        try:
            await self.db_session.execute(update(self.table)
                                          .where(self.table.id == object_id)
                                          .values(object.model_dump(
                                              exclude_none=True)
                                                  )
                                          .execution_options(
                                              synchronize_session='fetch')
                                          )
            await self.db_session.commit()
        except Exception:
            await self.db_session.rollback()
            return None
        return await self.db_session.get(self.table, object_id)

    async def delete(self, object_id: int):
        match await BaseRepository.get_one(self, object_id):
            case None:
                return None
            case _:
                await self.db_session.execute(
                    delete(self.table)
                    .where(self.table.id == object_id)
                    )
                await self.db_session.commit()
                return status.HTTP_204_NO_CONTENT

    # Ядро фильтра
    async def filter(self, **kwargs):
        return (await self.db_session.execute(
            select(self.table).filter_by(**kwargs))
                ).scalars().all()

# TODO: Использовать getattr() для определения таблицы и её поля в подзапросе при вызове из локальных service.py
    # Ядро поиска по подстроке
    async def search(self, params: Params, **kwargs):
        query = [
            getattr(self.table, key).regexp_match(value, 'i')
            for key, value in kwargs.items()
        ]
        return (await paginate(self.db_session,
                               select(self.table)
                               .filter(*query),
                               params)
                )

    #  Шаблон(ядро) мульти-фильтра

    async def sample_multi_filter(self, **kwargs):
        #  Обернуть в try: except:

        #  Вариант 1
        query = []
        for key, value in kwargs.items():
            match key[-3:-1]:
                case '_gt':  # '>'
                    query.append(getattr(self.table, key[:-3]) > value)
                case '_ge':  # '>='
                    query.append(getattr(self.table, key[:-3]) >= value)
                case '_lt':  # '<'
                    query.append(getattr(self.table, key[:-3]) < value)
                case '_le':  # '>='
                    query.append(getattr(self.table, key[:-3]) <= value)
                case _:  # 'остальные варианты...как правило =='
                    query.append(getattr(self.table, key) == value)
        resp = select(self.table).filter(*query)
        result = (await self.db_session.execute(resp)
                  ).scalars().all()

        #  Вариант 2 ### Просто фильтр на мульти-равенство(аналог filter_by)
        query = [getattr(self.table, key) == value
                 for key, value in kwargs.items()]
        result = (await self.db_session.execute(
            select(self.table).filter(*query))
                  ).scalars().all()

        return result
