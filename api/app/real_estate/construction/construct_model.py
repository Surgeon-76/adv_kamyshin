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


class Construction(Base):
    __tablename__ = 'construction'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    term_id: Mapped[int | None
                    ] = mapped_column(Integer,
                                      ForeignKey('term_transaction.id',
                                                 ondelete='CASCADE'))
    rules_id: Mapped[int | None
                     ] = mapped_column(Integer,
                                       ForeignKey('rules_of_sett.id',
                                                  ondelete='CASCADE'))
    type: Mapped[str] = mapped_column(String(), default='Дом')
    bath_sauna: Mapped[bool | None] = mapped_column(Boolean, default=None)
    pool: Mapped[bool | None] = mapped_column(Boolean, default=None)
    plot_status: Mapped[str | None] = mapped_column(String(), default=None)
    year_constr: Mapped[int | None] = mapped_column(Integer, default=None)
    wall_material: Mapped[str | None] = mapped_column(String(), default=None)
    levels: Mapped[int] = mapped_column(Integer, default=1)
    rooms: Mapped[str] = mapped_column(String(), default='1')
    terrace: Mapped[bool | None] = mapped_column(Boolean, default=None)
    house_space: Mapped[decimal.Decimal
                        ] = mapped_column(DECIMAL(precision=10, scale=2),
                                          default=0.00)
    plot_space: Mapped[decimal.Decimal | None
                       ] = mapped_column(DECIMAL(precision=10, scale=2),
                                         default=None)
    bathroom_home: Mapped[bool | None] = mapped_column(Boolean, default=None)
    bathroom_yard: Mapped[bool | None] = mapped_column(Boolean, default=None)
    repair: Mapped[str | None] = mapped_column(String(), default=None)
    electricity: Mapped[bool | None] = mapped_column(Boolean, default=None)
    gas: Mapped[bool | None] = mapped_column(Boolean, default=None)
    heating: Mapped[bool | None] = mapped_column(Boolean, default=None)
    canalization: Mapped[bool | None] = mapped_column(Boolean, default=None)
    wifi: Mapped[bool | None] = mapped_column(Boolean, default=None)
    tv: Mapped[bool | None] = mapped_column(Boolean, default=None)
    parking: Mapped[str] = mapped_column(String(), default='Гараж')
    asphalt: Mapped[bool | None] = mapped_column(Boolean, default=None)
    bus_station: Mapped[bool | None] = mapped_column(Boolean, default=None)
    railway_station: Mapped[bool | None] = mapped_column(Boolean, default=None)
    shop: Mapped[bool | None] = mapped_column(Boolean, default=None)
    pharmacy: Mapped[bool | None] = mapped_column(Boolean, default=None)
    kindergarten: Mapped[bool | None] = mapped_column(Boolean, default=None)
    school: Mapped[bool | None] = mapped_column(Boolean, default=None)
    bedding: Mapped[bool | None] = mapped_column(Boolean, default=None)
    towels: Mapped[bool | None] = mapped_column(Boolean, default=None)
    hygiene: Mapped[bool | None] = mapped_column(Boolean, default=None)

    transaction: Mapped['TermTransaction'
                        ] = relationship(back_populates='construction',
                                         uselist=False)
    rules: Mapped['Construction'
                  ] = relationship(back_populates='construction',
                                   uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    type            'Дом, Дача, Коттедж, Таунхаус'
    bath_sauna      'Баня или сауна'
    pool            'Бассейн'
    plot_status     'нет,
                         Индивидуальное жилищное строительство(ИЖС),
                         Садовое некомерческое товарищество(СНТ),
                         Дачное некомерческое партнерство(ДНП),
                         Фермерское хозяйство,
                         Личное подсобное хозяйство(ЛПХ)'
    year_constr     'Год посторйки'
    wall_material   'Кирпич, Брус, Бревно, Газоблоки, Металл,
                             Пеноблоки, Сендвич-панели, Ж/б панели,
                             Экспериментальные материалы'
    levels          'Количество этажей'
    rooms           'Студия, 1, ... , 9, 10 комнат и более,
                             Свободная планировка'
    terrace         'Терраса или веранда'
    house_space     'Площадь дома м*2'
    plot_space      'Площадь участка сот.'
    bathroom_home   'Санузел в доме'
    bathroom_yard   'Санузел на улице'
    repair          'Тебуется, Косметический, Евро, Дизайнерский'
    electricity     'Электричество'
    gas             'Газ'
    heating         'Отопление'
    canalization    'Канализация'
    wifi            'Wi-Fi'
    tv              'Телевидение'
    parking         'Парковка: нет, Гараж, Парковочное место'
    asphalt         'Асфальтированная дорога'
    bus_station     'Остановка общественного транспорта'
    railway_station 'Железнодорожная станция'
    shop            'Магазин'
    pharmacy        'Аптека'
    kindergarten    'Детский сад'
    school          'Школа'
    bedding         'Постельное бельё'
    towels          'Полотенца'
    hygiene         'Средства гигиены'
"""
