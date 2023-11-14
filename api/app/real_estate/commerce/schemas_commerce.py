from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseCommerce(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    term_transaction_id: int = Field(description='--> commerce_transaction.id')
    entrance: str = Field(description='Вход',
                          default='')
    entrance_private: bool = Field(description='Отдельный вход',
                                   default=False)
    level: int = Field(description='Этаж(Подвальный(-1), Цокольный(0))',
                       default=1)
    multi_levels: bool = Field(description='Несколько этажей',
                               default=False)
    office_layout: bool | None = Field(description='Планировка: Кабинетная',
                                       default=None)
    open_layout: bool | None = Field(description='Планировка: Открытая',
                                     default=None)
    space: Decimal = Field(description='Общая площадь, м*2',
                           max_digits=10,
                           decimal_places=2,
                           default=0.00)
    height: Decimal = Field(description='Высота потолков, м',
                            max_digits=10,
                            decimal_places=2,
                            default=0.00)
    finishing: str = Field(description='Отделка',
                           default='Чистовая')
    energosale: Decimal = Field(description='Мощность электросети, кВт',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00)
    energosale_max: bool = Field(description='Можно увеличить',
                                 default=False)
    heating: str = Field(description='Отопление',
                         default='Центральное')
    building_read: str = Field(description='Готовность',
                               default='В эксплуатации')
    building_type: str = Field(description='Тип здания',
                               default='')
    dist_road: str = Field(description='Удаленность от дороги',
                           default='Первая линия')
    parking: str = Field(description='Парковка',
                         default='На улице')
    parking_free: bool = Field(description='Бесплатная парковка',
                               default=True)
    parking_truck: bool = Field(description='Подходит для грузового  транспорта',
                                default=False)
    parking_quantity: int = Field(description='Количество мест',
                                  default=2)


class CommerceID(BaseModel):
    id: int = Field(description='ID коммер недвиж')


class CommerceView(BaseCommerce, CommerceID):
    pass


class CommerceCreate(BaseCommerce):
    pass


class CommerceUpdate(BaseCommerce, CommerceID):
    pass

# #############################################################


class CommerceResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: CommerceView | None = None


class CommerceError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class CommercePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[CommerceView] | None = None
    total: int
    page: int
    size: int
    pages: int


class CommercePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class CommerceDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    term_transaction: Mappeds['CommTransaction'
                             ] = relationship(back_populates='commerce')

    entrance         'Вход: С улицы, Со двора'
    entrance_private 'Отдельный вход'
    level            'Этаж: Подвальный(-1), Цокольный(0), 1, ... , 99'
    multi_levels     'Несколько этажей'
    office_layout    'Планировка: Кабинетная'
    open_layout      'Планировка: Открытая'
    space            'Общая площадь, м*2'
    height           'Высота потолков, м'
    finishing        'Без отделки, Чистовая, Офисная'
    energosale       'Мощность электросети, кВт'
    energosale_max   'Можно увеличить(мощность электросети)'
    heating          'Отопление: Нет, Центральное, Автономное'
    building_read    'Готовность: Проект, Строится, В  эксплуатации'
    building_type    'Тип здания: нет, Бизнес-центр,
                                       Торговый центр,
                                       Административное здание,
                                       Жилой дом,
                                       Другое'
    dist_road        'Удаленность от дороги: Первая линия,
                                             Вторая  линия и дальше'
    parking          'Парковка: Нет, На улице, В здании'
    parking_free     'Паковка: Бесплатная'
    parking_truck    'Парковка: Подходит для грузового  транспорта'
    parking_quantity 'Парковка: Количество мест'
"""
