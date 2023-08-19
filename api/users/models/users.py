from datetime import datetime
from enum import Enum

import ormar
from pydantic import validator

from services.user_hash import is_hash, hash_password
from settings.db import (
    database,
    metadata
)


class TypeUser(Enum):
    t_user1 = 'Физическое лицо'
    t_user2 = 'Самозанятый'
    t_user3 = 'Индивидуальный предприниматель'
    t_user4 = 'Юридическое лицо'


class User(ormar.Model):
    """
    <pk>                          id
    Имя                           first_name
    Фамилия                       family
    Отчество                      last_name
    Email                         email
    Номер телефона                phone
    Тип пользователя(TypeUser)    type_user
    Права доступа                 admission
    адрес личной страницы         pers_web_site
    Уникальное имя для обьявлений nickname
    О себе                        about_me
    Сайт                          site
    Фото профиля                  avatar
    Согласие на обработку ПД      agreement
    дата создания                 created_on
    дата обновления               updated_on
    """

    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    password: str = ormar.String(max_length=1000)
    first_name: str = ormar.String(max_length=100, nullable=True)
    family: str = ormar.String(max_length=100, nullable=True)
    last_name: str = ormar.String(max_length=100, nullable=True)
    email: str = ormar.String(max_length=200, nullable=True)
    phone: str = ormar.String(max_length=55, nullable=True)
    type_user: str = ormar.String(max_length=100, choices=list(TypeUser),
                                  nullable=True)
    admission: int = ormar.Integer(default=2)
    pers_web_site: str = ormar.String(max_length=255, nullable=True)
    niсkname: str = ormar.String(max_length=50, nullable=True)
    about_me: str = ormar.Text(nullable=True)
    site: str = ormar.String(max_length=255, nullable=True)
    avatar: str = ormar.String(max_length=255, nullable=True)
    agreement: bool = ormar.Boolean(default=False)
    created_on: datetime = ormar.DateTime(default=datetime.now())
    updated_on: datetime = ormar.DateTime(default=datetime.now(),
                                          onupdate=datetime.now())

    @validator('password')
    def hash_password(cls, pw: str) -> str:
        if is_hash(pw):
            return pw
        return hash_password(pw)

    class Config:
        orm_mode = True
