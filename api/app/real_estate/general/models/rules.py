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


class RulesOfSett(Base):
    __tablename__ = 'rules_of_sett'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    guest: Mapped[str | None] = mapped_column(String(), nullable=True)
    kinds: Mapped[bool] = mapped_column(Boolean, default=False)
    pets: Mapped[bool] = mapped_column(Boolean, default=False)
    smoking: Mapped[bool] = mapped_column(Boolean, default=False)
    paty: Mapped[bool | None] = mapped_column(Boolean, default=None)
    docs: Mapped[bool | None] = mapped_column(Boolean, default=None)
    monthly: Mapped[bool | None] = mapped_column(Boolean, default=None)

    rooms: Mapped['Rooms'] = relationship(back_populates='rules',
                                          uselist=False)
    apartment: Mapped['Apartment'] = relationship(back_populates='rules',
                                                  uselist=False)
    construction: Mapped['Construction'
                         ] = relationship(back_populates='rules',
                                          uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    guest   'Максимум гостей: 1, ... , 49, 50 и более'
    kinds   'Можно с детьми: Да, Нет'
    pets    'Можно с животными: Да, Нет'
    smoking 'Разрешено курить: Да, Нет'
    paty    'Разрешены вечеринки: Да, Нет'
    docs    'Есть отчетные документы: Да, Нет'
    monthly 'Возможна помесячная аренда: Да, Нет'
"""
