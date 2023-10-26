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


class Building(Base):
    __tablename__ = 'building'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    term_id: Mapped[int] = mapped_column(Integer,
                                         ForeignKey('term_transaction.id',
                                                    ondelete='CASCADE'))
    rules_id: Mapped[int] = mapped_column(Integer,
                                          ForeignKey('rules_of_sett.id',
                                                     ondelete='CASCADE'))
    building_id: Mapped[int] = mapped_column(Integer,
                                             ForeignKey('building.id',
                                                        ondelete='CASCADE'))
    number: Mapped[int] = mapped_column(Integer, default=1)
    type: Mapped[str] = mapped_column(String(), default='Квартира')
    level: Mapped[int] = mapped_column(Integer, default=0)
    rooms: Mapped[str] = mapped_column(String(), default= '1')
    balcony: Mapped[bool] = mapped_column(Boolean, default=True)
    loggia: Mapped[bool | None] = mapped_column(Boolean, default=None)
    dress_room: Mapped[bool | None] = mapped_column(Boolean, default=None)
    pan_windows: Mapped[bool | None] = mapped_column(Boolean, default=None)
    isolated: Mapped[bool | None] = mapped_column(Boolean, default=None)
    adjacent: Mapped[bool | None] = mapped_column(Boolean, default=None)
    total_space: Mapped[decimal] = mapped_column(DECIMAL, default=0.00)
    kitch_space: Mapped[decimal] = mapped_column(DECIMAL, default=0.00)
    living_space: Mapped[decimal] = mapped_column(DECIMAL, default=0.00)
    bathroom_combi: Mapped[bool | None] = mapped_column(Boolean, default=None)
    bathroom_separ: Mapped[bool | None] = mapped_column(Boolean, default=None)
    window_rear: Mapped[bool | None] = mapped_column(Boolean, default=None)
    window_to_street: Mapped[bool | None] = mapped_column(Boolean, default=None)
    window_on_sunny: Mapped[bool | None] = mapped_column(Boolean, default=None)
    repair: Mapped[str]  = mapped_column(String(), default='')
    heated_floor: Mapped[bool | None] = mapped_column(Boolean, default=None)
    furn_kitchen: Mapped[bool | None] = mapped_column(Boolean, default=None)
    furn_keeping: Mapped[bool | None] = mapped_column(Boolean, default=None)
    furn_sleep_places: Mapped[bool | None
                              ] = mapped_column(Boolean, default=None)
    tech_ac: Mapped[bool| None] = mapped_column(Boolean, default=None)
    tech_freezer: Mapped[bool | None] = mapped_column(Boolean, default=None)
    tech_washing: Mapped[bool | None] = mapped_column(Boolean, default=None)
    tech_dishwasher: Mapped[bool | None] = mapped_column(Boolean, default=None)
    tech_waterheater: Mapped[bool | None] = mapped_column(Boolean, default=None)
    bedding: Mapped[bool | None] = mapped_column(Boolean, default=None)
    towels: Mapped[bool | None] = mapped_column(Boolean, default=None)
    hygiene: Mapped[bool | None] = mapped_column(Boolean, default=None)

    building: Mapped['Building'
                     ] = relationship(back_populates='apartment',
                                      uselist=False)
    term_transaction: Mapped['TermTransaction'
                     ] = relationship(back_populates='apartment',
                                      uselist=False)
    rules_of_sett: Mapped['RulesOfSett'
                     ] = relationship(back_populates='apartment',
                                      uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"

table building [note: 'О доме(многоквартирном)'] {
  id int [PK]
  type enum[string] [note: 'Тип дома: Кирпичный,
                                      Панельный,
                                      Блочный,
                                      Монолитный,
                                      Монолитно-кирпичный,
                                      Деревянный']
  concierge bool[False] [note: 'Консьерж']
  garb_chute bool[False] [note: 'Мусоропровод']
  gas bool[False] [note: 'Газ']
  year_constr int [note: 'Год посторйки']
  dismant bool[False] [note: 'Запланирован снос']
  el_pass enum[string] [note: 'Лифт пассажирский: нет, 1, 2, 3, 4']
  el_freight enum[string] [note: 'Лифт грузовой: нет, 1, 2, 3, 4']
  yard_closed bool[False] [note: 'Двор: Закрытая территория']
  yard_playground bool[False] [note: 'Двор: Детская площадка']
  yard_sports bool[False] [note: 'Двор: Спортивная площадка']
  park_undegr bool[False] [note: 'Парковка: Подземная']
  park_abov bool[False] [note: 'Парковка: Надземная многоуровневая']
  park_open bool[False] [note: 'Парковка: Открытая во дворе']
  park_behbarrier bool[False] [note: 'Парковка: За шлагбаумом во дворе']
}
"""
    number            'Номер квартиры'
    type              'Тип жилья: Квартира, Апартаменты'
    level             'Этаж'
    rooms             'Студия, 1, ... , 9, 10 комнат и более,
                              Свободная планировка'
    balcony           'Балкон'
    loggia            'Лоджия'
    dress_room        'Гардеробная'
    pan_windows       'Панорамные окна'
    isolated          'Тип комнат: изолированные'
    adjacent          'Тип комнат: смежные'
    total_space       'Общая площадь м*2'
    kitch_space       'Площадь кухни м*2'
    living_space      'Жилая площадь м*2'
    bathroom_combi    'Санузел совмещенный'
    bathroom_separ    'Санузел раздельный'
    window_rear       'Окна во Двор'
    window_to_street  'Окна на улицу'
    window_on_sunny   'Окна на солнечную сторону'
    repair            'Тебуется, Косметический, Евро, Дизайнерский'
    heated_floor      'Теплый пол'
    furn_kitchen      'Мебель: Кухня'
    furn_keeping      'Мебель: Хранение одежды'
    furn_sleep_places 'Мебель: Спальные места'
    tech_ac           'Техника: Кондиционер'
    tech_freezer      'Техника: Холодильник'
    tech_washing      'Техника: Стиральная машина'
    tech_dishwasher   'Техника: Посудомоечная машина'
    tech_waterheater  'Техника: Водонагреватель'
    bedding           'Постельное бельё'
    towels            'Полотенца'
    hygiene           'Средства гигиены'
"""
