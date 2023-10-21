from __future__ import annotations

from sqlalchemy import (
    Boolean,
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


class Contacts(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    realest_id: Mapped[int] = mapped_column(Integer,
                                            ForeignKey('real_estate.id',
                                                       ondelete='CASCADE'))
    place_ads: Mapped[str] = mapped_column(String(), default='Собственник')
    email: Mapped[str | None] = mapped_column(String(), nullable=True)
    phone: Mapped[str] = mapped_column(String(), nullable=False)
    communication: Mapped[str] = mapped_column(String(),
                                               default='Звонки и сообщения')
    online: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"

    #TODO: Проверка телефона(валидатор)


"""
    place_ads 'Размещает объявление: Собственник, Посредник'
    email 'Email' 
    phone 'Телефон'
    communication'Способ связи: Звонки и сообщения, Только звонки,
                  Только сообщения'
    online 'Онлайн показ: Проведу, Не хочу'
"""
