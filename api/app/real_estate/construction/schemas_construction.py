from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseConstruction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    term_id: int | None = Field(description='--> term_transaction.id')
    rules_id: int | None = Field(description='--> rules_of_sett.id')
    type: str= Field(description='Тип строения',
                     default='Дом')
    bath_sauna: bool | None = Field(description='Баня или сауна',
                                    default=None)
    pool: bool | None = Field(description='Бассейн',
                              default=None)
    plot_status: str | None = Field(description='Статус участка',
                                    default=None)
    year_constr: int | None = Field(description='Год посторйки',
                                    default=None)
    wall_material: str | None = Field(description='Материал стен',
                                      default=None)
    levels: int = Field(description='Количество этажей',
                        default=1)
    rooms: str = Field(description='Количество комнат',
                       default='1')
    terrace: bool | None = Field(description='Терраса или веранда',
                                 default=None)
    house_space: Decimal = Field(description='Площадь дома, м*2',
                                 max_digits=10,
                                 decimal_places=2,
                                 default=0.00)
    plot_space: Decimal | None = Field(description='Площадь участка, сот.',
                                       max_digits=10,
                                       decimal_places=2,
                                       default=None)
    bathroom_home: bool | None = Field(description='Санузел в доме',
                                       default=None)
    bathroom_yard: bool | None = Field(description='Санузел на улице',
                                       default=None)
    repair: str | None = Field(description='Ремонт',
                               default=None)
    electricity: bool | None = Field(description='Электричество',
                                     default=None)
    gas: bool | None = Field(description='Газ',
                             default=None)
    heating: bool | None = Field(description='Отопление',
                                 default=None)
    canalization: bool | None = Field(description='Канализация',
                                      default=None)
    wifi: bool | None = Field(description='Wi-Fi',
                              default=None)
    tv: bool | None = Field(description='Телевидение',
                            default=None)
    parking: str = Field(description='Парковка',
                         default='Гараж')
    asphalt: bool | None = Field(description='Асфальтированная дорога',
                                 default=None)
    bus_station: bool | None = Field(description='Остановка',
                                     default=None)
    railway_station: bool | None = Field(description='Железнодорожная станция',
                                         default=None)
    shop: bool | None = Field(description='Магазин',
                              default=None)
    pharmacy: bool | None = Field(description='Аптека',
                                  default=None)
    kindergarten: bool | None = Field(description='Детский сад',
                                      default=None)
    school: bool | None = Field(description='Школа',
                                default=None)
    bedding: bool | None = Field(description='Постельное бельё',
                                 default=None)
    towels: bool | None = Field(description='Полотенца',
                                default=None)
    hygiene: bool | None = Field(description='Средства гигиены',
                                 default=None)


class ConstructionID(BaseModel):
    id: int = Field(description='ID объявления')


class ConstructionView(BaseConstruction, ConstructionID):
    pass


class ConstructionCreate(BaseConstruction):
    pass


class ConstructionUpdate(BaseConstruction, ConstructionID):
    pass

# #############################################################


class ConstructionResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ConstructionView | None = None


class ConstructionError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ConstructionPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ConstructionView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ConstructionPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ConstructionDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
     transaction: Mapped['TermTransaction'
                        ] = relationship(back_populates='construction',
                                         uselist=False)
    rules: Mapped['Construction'
                  ] = relationship(back_populates='construction',
                                   uselist=False)

    type            'Дом, Дача, Коттедж, Таунхаус'
    bath_sauna      'Баня или сауна'
    pool            'Бассейн'
    plot_status     'Статус участка: нет,
                         Индивидуальное жилищное строительство(ИЖС),
                         Садовое некомерческое товарищество(СНТ),
                         Дачное некомерческое партнерство(ДНП),
                         Фермерское хозяйство,
                         Личное подсобное хозяйство(ЛПХ)'
    year_constr     'Год посторйки'
    wall_material   'Материал стен: Кирпич, Брус, Бревно, Газоблоки, Металл,
                             Пеноблоки, Сендвич-панели, Ж/б панели,
                             Экспериментальные материалы'
    levels          'Количество этажей'
    rooms           'Студия, 1, ... , 9, 10 комнат и более,
                             Свободная планировка'
    terrace         'Терраса или веранда'
    house_space     'Площадь дома, м*2'
    plot_space      'Площадь участка, сот.'
    bathroom_home   'Санузел в доме'
    bathroom_yard   'Санузел на улице'
    repair          'Ремонт:Тебуется, Косметический, Евро, Дизайнерский'
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
