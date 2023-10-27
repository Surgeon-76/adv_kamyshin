from __future__ import annotations

import decimal

from sqlalchemy import (
    Boolean,
    DECIMAL,
    Integer,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class ParkingSpace(Base):
    __tablename__ = 'parking_space'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    type: Mapped[str] = mapped_column(String(), default='Открытая стоянка')
    space: Mapped[decimal.Decimal
                  ] = mapped_column(DECIMAL(precision=10,
                                            scale=2),
                                    default=0.00)
    security: Mapped[bool] = mapped_column(Boolean, default=False)

    realest: Mapped['RealEstate'
                       ] = relationship(back_populates='parking_space')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type      'Тип машино места: Многоуровневый паркинг,
                                 Подземный паркинг,
                                 Крытая стоянка,
                                 Открытая стоянка'
    space     'Площадь машино места'
    security  'Охрана: Да, Нет'
"""
