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


class BodyType(Base):
    __tablename__ = 'body_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    model_id: Mapped[int] = mapped_column(Integer, ForeignKey('model_auto.id'))
    type_body: Mapped[str] = mapped_column(String(), default='Седан')

    avtotth: Mapped['AvtoTth'] = relationship(back_populates='bodytype',
                                              uselist=False)
    model: Mapped['ModelAuto'] = relationship(back_populates='body')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type_body 'Тип кузова: Седан, Хэтчбек, Универсал, Кабриолет, Купе'
"""
