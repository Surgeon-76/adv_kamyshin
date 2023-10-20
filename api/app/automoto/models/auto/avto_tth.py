from __future__ import annotations

from datetime import date

from sqlalchemy import (
    Date,
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


class AvtoTth(Base):
    __tablename__ = 'avto_tth'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    body_id: Mapped[int] = mapped_column(ForeignKey('body_type.id',
                                                    ondelete='CASCADE'))
    addit_id: Mapped[int] = mapped_column(ForeignKey('avto_addit.id',
                                                     ondelete='CASCADE'))
    release_year: Mapped[date] = mapped_column(Date,
                                               default=date.today()
                                               .strftime("%YYYY"))
    doors: Mapped[int] = mapped_column(Integer, default=4)
    generation: Mapped[int | None] = mapped_column(Integer, nullable=True)
    engine_type: Mapped[str] = mapped_column(String(), default='Бензин')
    transmission: Mapped[str] = mapped_column(String(), default='Передний')
    gearbox: Mapped[str] = mapped_column(String(), default='Механическая')
    version: Mapped[str | None] = mapped_column(String(), nullable=True)
    package: Mapped[str | None] = mapped_column(String(), nullable=True)
    wheel: Mapped[str] = mapped_column(String(), default='Правый')

    transport: Mapped['Transport'] = relationship(back_populates='avto_tth',
                                                  uselist=False)
    addit: Mapped['AvtoAddit'] = relationship(back_populates='tth')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    release_year 'Год выпуска'
    doors 'Количество дверей'
    generation 'Поколение'
    engine_type 'Тип двигателя(Бензин, Дизель, Газ, Гибрид, Электро)'
    transmission  'Привод: Задний, Передний, Полный'
    gearbox  'КПП: Механическая, Автоматическая, Вариатор, Роботизированная,
            Прямой привод'
    version 'Модификация(1.6 МТ (125 л.с.))'
    package 'Комплектация: Базовая, Trend, Trend Sport, Titanium'
    wheel 'Руль: Правый, Левый'
"""
