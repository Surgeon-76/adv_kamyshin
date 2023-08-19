from datetime import datetime
import decimal
from enum import Enum
from typing import Optional

import ormar

from users.models.users import User
from .address import Address
from .categorie import Categorie

from settings.db import (
    database,
    metadata
    )


class NumberOfRooms(Enum):
    nr_0 = 'студия'
    nr_1 = '1-комнатная'
    nr_2 = '2-комнатная'
    nr_3 = '3-комнатная'
    nr_4 = '4-комнатная'
    nr_5 = '5 и более комнатная'
    nr_6 = 'свободная планировка'


class Recency(Enum):
    rc_0 = 'новостройка'
    rc_1 = 'вторичное'


class Finishing(Enum):
    fs_0 = 'с отделкой'
    fs_1 = 'без отделки'


class AuxiliaryPremises(Enum):
    ap_0 = 'нет'
    ap_1 = 'балкон'
    ap_2 = 'лоджия'


class SanNode(Enum):
    sn_0 = 'совмещенный'
    sn_1 = 'раздельный'
    sn_2 = 'уличный'


class TypeHouse(Enum):
    th_0 = 'кирпичный'
    th_1 = 'панельный'
    th_2 = 'блочный'
    th_3 = 'монолитный'
    th_4 = 'монолитно-кирпичный'
    th_5 = 'деревянный'
    th_6 = 'каркасный'


"""
    id: int
    title: str              Заголовок объявления
    body: str               Описание
    rooms: str              Количество комнат(NumberOfRooms)
    originality: str        Тип жилья(Recency)
    price: decimal          Цена
    total: float            Общая площадь
    living: float           Жилая площадь
    finish: str             Отделка(Finishing)
    auxiliary: str          Вспомогательные помещ(AuxiliaryPremises)
    sanitary: str           Санузел(SanNode)
    buildingtype: str       Тип(материал) строения(TypeHouse)
    created_on: datetime    Дата создания объявления
    updated_on: datetime    Дата обновления
    closed: bool            Флаг зактрытия объявления
    category: Optional[Categorie] ForeignKey(Categorie)
    address: Optional[Address] ForeignKey(Address)
    user: Optional[User] ForeignKey(User)

"""


class ADSAppart(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    title: str = ormar.String(max_length=255, nullable=True)
    body: str = ormar.String(max_length=1000, nullable=True)
    rooms: str = ormar.String(max_length=50, choices=list(NumberOfRooms))
    originality: str = ormar.String(max_length=100, choices=list(Recency))
    price: decimal = ormar.Decimal(
        precision=10,
        scale=2,
        default=0)
    total: float = ormar.Float()
    living: float = ormar.Float()
    finish: str = ormar.String(max_length=30, choices=list(Finishing))
    auxiliary: str = ormar.String(
        max_length=20,
        choices=list(AuxiliaryPremises))
    sanitary: str = ormar.String(max_length=20, choices=list(SanNode))
    buildingtype: str = ormar.String(max_length=20, choices=list(TypeHouse))
    created_on: datetime = ormar.DateTime(default=datetime.now(),
                                          index=True)
    updated_on: datetime = ormar.DateTime(default=datetime.now(),
                                          onupdate=datetime.now(),
                                          index=True)
    closed: bool = ormar.Boolean(default=False)
    category: Optional[Categorie] = ormar.ForeignKey(Categorie)
    address: Optional[Address] = ormar.ForeignKey(Address)
    user: Optional[User] = ormar.ForeignKey(User)
