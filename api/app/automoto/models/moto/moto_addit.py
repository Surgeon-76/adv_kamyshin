from __future__ import annotations

from sqlalchemy import (
    Boolean,
    Integer
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class MotoAddit(Base):
    __tablename__ = 'moto_addit'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    starter: Mapped[bool] = mapped_column(Boolean, default=False)
    abs: Mapped[bool] = mapped_column(Boolean, default=False)
    tcs: Mapped[bool] = mapped_column(Boolean, default=False)
    start_stop: Mapped[bool] = mapped_column(Boolean, default=False)
    windscreen: Mapped[bool] = mapped_column(Boolean, default=False)
    trunk: Mapped[bool] = mapped_column(Boolean, default=False)

    tth: Mapped['MotoTth'] = relationship(back_populates='addit',
                                          uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    starter    'Электростартер'
    abs        'Антиблокировочная система'
    tcs        'Противопробуксовочная система(трэкшн-контроль)'
    start_stop 'Система "старт-стоп"'
    windscreen 'Ветровое стекло'
    trunk      'Кофр'
"""
