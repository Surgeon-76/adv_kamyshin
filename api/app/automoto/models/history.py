from __future__ import annotations

from sqlalchemy import (
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


class History(Base):
    __tablename__ = 'history'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    transport_id: Mapped[int] = mapped_column(ForeignKey('transport.id',
                                                         ondelete='CASCADE'))
    condition: Mapped[str] = mapped_column(String(), default='б/у')
    odometer: Mapped[int] = mapped_column(Integer, default=0)
    orig_pts: Mapped[str] = mapped_column(String(), default='Оригинал')
    num_of_own: Mapped[int] = mapped_column(Integer, default=1)

    transport: Mapped['Transport'] = relationship(back_populates='history',
                                                  uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
condition  'Состояние: Новый, б/у, На запчасти'
odometer Пробег
orig_pts  'Оригинал, Дубликат, Электронный, нет'
num_of_own  'Количество владельцев'
"""
