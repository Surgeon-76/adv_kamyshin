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


class TermTransaction(Base):
    __tablename__ = 'term_transaction'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ipoteka: Mapped[bool] = mapped_column(Boolean, default=False)
    part: Mapped[bool] = mapped_column(Boolean, default=False)

    rooms: Mapped['Rooms'] = relationship(back_populates='transaction')
    apartment: Mapped['Apartment'] = relationship(back_populates='transaction')
    construction: Mapped['Construction'
                         ] = relationship(back_populates='transaction')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    ipoteka  'Можно в ипотеку']
    part     'Продажа доли']
"""
