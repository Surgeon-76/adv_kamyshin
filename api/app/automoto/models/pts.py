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


class Pts(Base):
    __tablename__ = 'pts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    transport_id: Mapped[int] = mapped_column(ForeignKey('transport.id',
                                                         ondelete='CASCADE'))
    pts: Mapped[str] = mapped_column(String(), default='Нет')

    transport: Mapped['Transport'] = relationship(back_populates='pts',
                                                  uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
