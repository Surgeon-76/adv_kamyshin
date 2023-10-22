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


class CommTransaction(Base):
    __tablename__ = 'commerce_transaction'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    type: Mapped[str] = mapped_column(String(), default='Продажа')
    renter: Mapped[bool] = mapped_column(Boolean, default=False)
    price_type: Mapped[str] = mapped_column(String(), default='За всё')

    commerce: Mapped['CommBuilding'
                     ] = relationship(back_populates='transaction',
                                      uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type       'Тип сделки: Продажа, Переуступка права аренды'
    renter     'Арендатор: Помещение сдано'
    price_type 'Цена: За всё, За м*2'
"""
