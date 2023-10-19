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


class Transport(Base):
    __tablename__ = 'transport'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ads_id: Mapped[int] = mapped_column(ForeignKey('ads.id'))
    auto_id: Mapped[int | None] = mapped_column(ForeignKey('avto_tth.id'))
    moto_id: Mapped[int | None] = mapped_column(ForeignKey('moto_tth.id'))
    #TODO: Решить с каскадностью

    color: Mapped[int] = mapped_column(Integer, default=0)
    #TODO: Решить с кодировкой цветов(#XXXX)
    vin: Mapped[str] = mapped_column(String(), default='Нет')

    ads: Mapped['Ads'] = relationship(back_populates='transport',
                                      uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
