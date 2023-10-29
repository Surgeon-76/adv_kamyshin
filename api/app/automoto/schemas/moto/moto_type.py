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


class MotoType(Base):
    __tablename__ = 'moto_type'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    model_id: Mapped[int] = mapped_column(Integer, ForeignKey('model_moto.id'))
    type_moto: Mapped[str] = mapped_column(String(), default='Туристический')

    mototth: Mapped['MotoTth'] = relationship(back_populates='mototype',
                                              uselist=False)
    model: Mapped['ModelMoto'] = relationship(back_populates='mototype')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type_moto 'Спортивный, Туристический, Чоппер и т.д.'
"""
