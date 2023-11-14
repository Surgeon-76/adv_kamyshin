from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseApartment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    term_id: int = Field(description='--> term_transaction.id')
    rules_id: int = Field(description='--> rules_of_sett.id')
    building_id: int = Field(description='--> building.id')
    number: int = Field(description='Номер квартиры', default=1)
    type: str = Field(description='Тип жилья', default='Квартира')
    level: int = Field(description='Этаж', default=0)
    rooms: str = Field(description='Количество комнат', default= '1')
    balcony: bool = Field(description='Балкон', default=True)
    loggia: bool | None = Field(description='Лоджия', default=None)
    dress_room: bool | None = Field(description='Гардеробная', default=None)
    pan_windows: bool | None = Field(description='Панорамные окна',
                                     default=None)
    isolated: bool | None = Field(description='Тип комнат', default=None)
    adjacent: bool | None = Field(description='Тип комнат', default=None)
    total_space: Decimal = Field(description='Общая площадь, м*2',
                                 max_digits=10,
                                 decimal_places=2,
                                 default=0.00)
    kitch_space: Decimal = Field(description='Площадь кухни, м*2',
                                 max_digits=10,
                                 decimal_places=2,
                                 default=0.00)
    living_space: Decimal = Field(description='Жилая площадь, м*2',
                                  max_digits=10,
                                  decimal_places=2,
                                  default=0.00)
    bathroom_combi: bool | None = Field(description='Санузел совмещенный',
                                        default=None)
    bathroom_separ: bool | None = Field(description='Санузел раздельный',
                                        default=None)
    window_rear: bool | None = Field(description='Окна во Двор', default=None)
    window_to_street: bool | None = Field(description='Окна на улицу',
                                          default=None)
    window_on_sunny: bool | None = Field(description='Окна на солнечную сторону',
                                         default=None)
    repair: str | None = Field(description='Ремон', default=None)
    heated_floor: bool | None = Field(description='Теплый пол',
                                      default=None)
    furn_kitchen: bool | None = Field(description='Кухня',
                                      default=None)
    furn_keeping: bool | None = Field(description='Хранение одежды',
                                      default=None)
    furn_sleep_places: bool | None = Field(description='Спальные места',
                                           default=None)
    tech_ac: bool | None = Field(description='Кондиционер',
                                 default=None)
    tech_freezer: bool | None = Field(description='Холодильник',
                                      default=None)
    tech_washing: bool | None = Field(description='Стиральная машина',
                                      default=None)
    tech_dishwasher: bool | None = Field(description='Посудомоечная машина',
                                         default=None)
    tech_waterheater: bool | None = Field(description='Водонагреватель',
                                          default=None)
    bedding: bool | None = Field(description='Постельное бельё',
                                 default=None)
    towels: bool | None = Field(description='Полотенца',
                                default=None)
    hygiene: bool | None = Field(description='Средства гигиены',
                                 default=None)


class ApartmentID(BaseModel):
    id: int = Field(description='ID квартиры')


class ApartmentView(BaseApartment, ApartmentID):
    pass


class ApartmentCreate(BaseApartment):
    pass


class ApartmentUpdate(BaseApartment, ApartmentID):
    pass

# #############################################################


class ApartmentResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ApartmentView | None = None


class ApartmentError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ApartmentPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ApartmentView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ApartmentPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ApartmentDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    building: Mappeds['Building'
                     ] = relationship(back_populates='apartment',
                                      uselist=False)
    term_transaction: Mappeds['TermTransaction'
                             ] = relationship(back_populates='apartment',
                                              uselist=False)
    rules: Mappeds['RulesOfSett'
                  ] = relationship(back_populates='apartment',
                                   uselist=False)

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
