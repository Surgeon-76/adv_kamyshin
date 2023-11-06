from __future__ import annotations

import decimal

from sqlalchemy import (
    Boolean,
    DECIMAL,
    Float,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class Commerce(Base):
    __tablename__ = 'commerce_building'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    term_transaction_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('commerce_transaction.id', ondelete='CASCADE')
        )
    entrance: Mapped[str] = mapped_column(String(), default='')
    entrance_private: Mapped[bool] = mapped_column(Boolean, default=False)
    level: Mapped[int] = mapped_column(Integer, default=1)
    multi_levels: Mapped[bool] = mapped_column(Boolean, default=False)
    office_layout: Mapped[bool | None] = mapped_column(Boolean, default=None)
    open_layout: Mapped[bool | None] = mapped_column(Boolean, default=None)
    space: Mapped[decimal.Decimal
                  ] = mapped_column(DECIMAL(precision=10,
                                            scale=2),
                                    default=0.00)
    height: Mapped[decimal.Decimal
                   ] = mapped_column(DECIMAL(precision=10,
                                             scale=2),
                                     default=0.00)
    finishing: Mapped[str] = mapped_column(String(), default='Чистовая')
    energosale: Mapped[decimal.Decimal
                       ] = mapped_column(DECIMAL(precision=10,
                                                 scale=2),
                                         default=0.00)
    energosale_max: Mapped[bool] = mapped_column(Boolean, default=False)
    heating: Mapped[str] = mapped_column(String(), default='Центральное')
    building_read: Mapped[str] = mapped_column(String(),
                                               default='В  эксплуатации')
    building_type: Mapped[str] = mapped_column(String(), default='')
    dist_road: Mapped[str] = mapped_column(String(), default='Первая линия')
    parking: Mapped[str] = mapped_column(String(), default='На улице')
    parking_free: Mapped[bool] = mapped_column(Boolean, default=True)
    parking_truck: Mapped[bool] = mapped_column(Boolean, default=False)
    parking_quantity: Mapped[int] = mapped_column(Integer, default=2)

    term_transaction: Mapped['CommTransaction'
                             ] = relationship(back_populates='commerce')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    entrance         'Вход: С улицы, Со двора'
    entrance_private 'Отдельный вход'
    level            'Этаж: Подвальный(-1), Цокольный(0), 1, ... , 99'
    multi_levels     'Несколько этажей'
    office_layout    'Планировка: Кабинетная'
    open_layout      'Планировка: Открытая'
    space            'Общая площадь, м*2'
    height           'Высота потолков, м'
    finishing        'Без отделки, Чистовая, Офисная'
    energosale       'Мощность электросети, кВт'
    energosale_max   'Можно увеличить(мощность электросети)'
    heating          'Отопление: Нет, Центральное, Автономное'
    building_read    'Готовность: Проект, Строится, В эксплуатации'
    building_type    'Тип здания: нет, Бизнес-центр,
                                       Торговый центр,
                                       Административное здание,
                                       Жилой дом,
                                       Другое'
    dist_road        'Удаленность от дороги: Первая линия,
                                             Вторая  линия и дальше'
    parking          'Парковка: Нет, На улице, В здании'
    parking_free     'Паковка: Бесплатная'
    parking_truck    'Парковка: Подходит для грузового  транспорта'
    parking_quantity 'Парковка: Количество мест'
"""
