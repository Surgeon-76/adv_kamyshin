from __future__ import annotations

import decimal

from sqlalchemy import (
    Boolean,
    DECIMAL,
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


class Rooms(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)    
    term_id: Mapped[int | None
                    ] = mapped_column(Integer,
                                      ForeignKey('term_transaction.id',
                                                 ondelete='CASCADE'))
    rules: Mapped[int | None
                  ] = mapped_column(Integer,
                                    ForeignKey('rules_of_sett.id',
                                               ondelete='CASCADE'))
    type: Mapped[str | None] = mapped_column(String(), default=None)
    rooms: Mapped[str | None] = mapped_column(String(), default=None)
    level: Mapped[int] = mapped_column(Integer, default=1)
    room_space: Mapped[decimal.Decimal | None
                       ] = mapped_column(DECIMAL(precision=10,
                                                 scale=2),
                                         default=None)
    beds: Mapped[str | None] = mapped_column(String(), default=None)
    sleep: Mapped[str | None] = mapped_column(String(), default=None)
    wifi: Mapped[bool | None] = mapped_column(Boolean, default=None)
    tv: Mapped[bool | None] = mapped_column(Boolean, default=None)
    plate: Mapped[bool | None] = mapped_column(Boolean, default=None)
    microwave: Mapped[bool | None] = mapped_column(Boolean, default=None)
    fridge: Mapped[bool | None] = mapped_column(Boolean, default=None)
    washing: Mapped[bool | None] = mapped_column(Boolean, default=None)
    fan: Mapped[bool | None] = mapped_column(Boolean, default=None)
    iron: Mapped[bool | None] = mapped_column(Boolean, default=None)
    ac: Mapped[bool | None] = mapped_column(Boolean, default=None)
    fireplace: Mapped[bool | None] = mapped_column(Boolean, default=None)
    balcony: Mapped[bool | None] = mapped_column(Boolean, default=None)
    parking: Mapped[bool | None] = mapped_column(Boolean, default=None)  
    bedding: Mapped[bool | None] = mapped_column(Boolean, default=None)
    towels: Mapped[bool | None] = mapped_column(Boolean, default=None)
    hygiene: Mapped[bool | None] = mapped_column(Boolean, default=None)

    realest: Mapped['RealEstate'
                    ] = relationship(back_populates='rooms')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type        'Тип дома: Кирпичный,
                           Панельный,
                           Блочный,
                           Монолитный,
                           Монолитно-кирпичный,
                           Деревянный'
    rooms       'Комнат в квартире: 1, ... , 9, > 9'
    level       'Этажей в доме'
    room_space  'Площадь комнаты, м*2'
    beds        'Количество кроватей: 1, ... , 8 и более'
    sleep       'Количество спальных мест: 1, ... , 16 и    более'
    wifi        'Wi-Fi'
    tv          'Телевизор'
    plate       'Плита'
    microwave   'Мироволновка'
    fridge      'Холодильник'
    washing     'Стиральная машинка'
    fan         'Фен'
    iron        'Утюг'
    ac          'Кондиционер/Сплит'
    fireplace   'Камин'
    balcony     'Балкон/Лоджия'
    parking     'Парковка'
    bedding     'Постельное бельё'
    towels      'Полотенца'
    hygiene     'Средства гигиены'
"""
