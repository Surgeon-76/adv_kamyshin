from datetime import datetime
from typing import Optional

import ormar

from buysell_advertisement.categories.models.categories import Category

from users.models.users import User
from settings.db import (
    database,
    metadata
    )


class ADVT(ormar.Model):

    """
    <pk>                        id: int
    Соглашение с условиями      agreement: bool
    user                        user: ForeignKey(User)
    Телефон для обьявления      phone: str
    Доп. телефон для обьявления phone_optional: str
    Регион объявления           region: ManyToMany(Region)
    Город объявления            city: ManyToMany(City)
    Заголовок обьявления        title: str
    Описание обьявления         specification: str
    Категория                   category: ForeignKey(Category)
    дата создания               created_on: datetime
    дата обновления             updated_on: datetime
    Логотип                     logo_URL
    """
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    slug: str = ormar.String(max_length=55, default='', nullable=True)
    agreement: bool = ormar.Boolean(default=False)
    user: User = ormar.ForeignKey(User)
    phone: str = ormar.String(max_length=55)
    title: str = ormar.String(max_length=255, index=True)
    descriptions: str = ormar.String(max_length=3000)
    category: Optional[Category] = ormar.ForeignKey(Category)
    count_views: Optional[int] = ormar.Integer(default=0, nullable=True)
    created_on: datetime = ormar.DateTime(default=datetime.now(),
                                          index=True)
    updated_on: datetime = ormar.DateTime(default=datetime.now(),
                                          onupdate=datetime.now(),
                                          index=True)
    logo: str = ormar.String(max_length=255,
                             default='static/images/images.jpeg')

    class Config:
        orm_mode = True
