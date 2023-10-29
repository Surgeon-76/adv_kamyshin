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


class MotoTth(Base):
    __tablename__ = 'moto_tth'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    moto_id: Mapped[int] = mapped_column(ForeignKey('moto_type.id',
                                                    ondelete='CASCADE'))
    addit_id: Mapped[int] = mapped_column(ForeignKey('moto_addit.id',
                                                     ondelete='CASCADE'))
    release_year: Mapped[date] = mapped_column(Date,
                                               default=date.today()
                                               .strftime("%YYYY"))
    engine_type: Mapped[str] = mapped_column(String(), default='Бензин')
    power: Mapped[int] = mapped_column(Integer, nullable=True)
    volume: Mapped[int] = mapped_column(Integer, nullable=True)
    fuel_supply: Mapped[str] = mapped_column(String(), default='Карбюратор')
    drive_type: Mapped[str] = mapped_column(String(), default='Цепь')
    cycles: Mapped[str] = mapped_column(String(), default='2')
    cylinders: Mapped[int] = mapped_column(Integer, default=1)
    gearbox: Mapped[str] = mapped_column(String(), default='Механика')
    scheme: Mapped[str | None] = mapped_column(String(), nullable=True)
    cooling: Mapped[str] = mapped_column(String(), default='Воздушное')

    transport: Mapped['Transport'] = relationship(back_populates='avto_tth',
                                                  uselist=False)
    addit: Mapped['MotoAddit'] = relationship(back_populates='tth')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    release_year  'Год выпуска'
    engine_type   'Тип двигателя(Бензин, Электро)'
    power         'Мощность двигателя л/с'
    volume        'Объём двигателя см*3'
    fuel_supply   'Подача топлива: Карбюратор, Инжектор'
    drive_type    'Привод: Цепь, Ремень, Кардан'
    cycles        'Число тактов: 2, 4'
    cylinders     'Число цилиндров: 1-...-6'
    gearbox       'КПП: Механика, Автомат, Вариатор, Робот'
    scheme        'Раположение цилиндров: V-образное, Оппозитное, Рядное'
    cooling       'Охлаждение: Воздушное, Жидкостное'
"""
