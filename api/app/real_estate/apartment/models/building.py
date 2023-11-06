from __future__ import annotations

from sqlalchemy import (
    Boolean,
    Integer,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class Building(Base):
    __tablename__ = 'building'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    type: Mapped[str] = mapped_column(String(), default='')
    concierge: Mapped[bool] = mapped_column(Boolean, default=False)
    garb_chute: Mapped[bool] = mapped_column(Boolean, default=False)
    gas: Mapped[bool] = mapped_column(Boolean, default=False)
    year_constr: Mapped[int] = mapped_column(Integer, default=1976)
    dismant: Mapped[bool] = mapped_column(Boolean, default=False)
    el_pass: Mapped[int] = mapped_column(Integer, nullable=True)
    el_freight: Mapped[int] = mapped_column(Integer, nullable=True)
    yard_closed: Mapped[bool] = mapped_column(Boolean, default=False)
    yard_playground: Mapped[bool] = mapped_column(Boolean, default=False)
    yard_sports: Mapped[bool] = mapped_column(Boolean, default=False)
    park_undegr: Mapped[bool] = mapped_column(Boolean, default=False)
    park_abov: Mapped[bool] = mapped_column(Boolean, default=False)
    park_open: Mapped[bool] = mapped_column(Boolean, default=False)
    park_behbarrier: Mapped[bool] = mapped_column(Boolean, default=False)

    apartment: Mapped['Apartment'
                      ] = relationship(back_populates='building')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type             'Тип дома: Кирпичный,
                                Панельный,
                                Блочный,
                                Монолитный,
                                Монолитно-кирпичный,
                                Деревянный'
    concierge        'Консьерж'
    garb_chute       'Мусоропровод'
    gas              'Газ'
    year_constr      'Год постройки'
    dismant:         'Запланирован снос'
    el_pass          'Лифт пассажирский: нет, 1, 2, 3, 4'
    el_freight       'Лифт грузовой: нет, 1, 2, 3, 4'
    yard_closed      'Двор: Закрытая территория'
    yard_playground  'Двор: Детская площадка'
    yard_sports      'Двор: Спортивная площадка'
    park_undegr      'Парковка: Подземная'
    park_abov        'Парковка: Надземная многоуровневая'
    park_open        'Парковка: Открытая во дворе'
    park_behbarrier  'Парковка: За шлагбаумом во дворе'
"""
