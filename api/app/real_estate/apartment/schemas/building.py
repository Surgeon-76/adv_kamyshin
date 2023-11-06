from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseBuilding(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str = Field(description='Тип дома',
                      default='')
    concierge: bool = Field(description='Консьерж',
                            default=False)
    garb_chute: bool = Field(description='Мусоропровод',
                             default=False)
    gas: bool = Field(description='Газ',
                      default=False)
    year_constr: int = Field(description='Год постройки',
                             default=1976)
    dismant: bool = Field(description='Запланирован снос',
                          default=False)
    el_pass: int | None = Field(description='Лифт пассажирский',
                                default=None)
    el_freight: int | None = Field(description='Лифт грузовой',
                                   default=None)
    yard_closed: bool = Field(description='Закрытая территория',
                              default=False)
    yard_playground: bool = Field(description='Детская площадка',
                                  default=False)
    yard_sports: bool = Field(description='Спортивная площадка',
                              default=False)
    park_undegr: bool = Field(description='Подземная парковка',
                              default=False)
    park_abov: bool = Field(description='Надземная многоуровневая',
                            default=False)
    park_open: bool = Field(description='Открытая во дворе',
                            default=False)
    park_behbarrier: bool = Field(description='За шлагбаумом во дворе',
                                  default=False)


class BuildingID(BaseModel):
    id: int = Field(description='ID объявления')


class BuildingView(BaseBuilding, BuildingID):
    pass


class BuildingCreate(BaseBuilding):
    pass


class BuildingUpdate(BaseBuilding, BuildingID):
    pass

# #############################################################


class BuildingResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: BuildingView | None = None


class BuildingError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class BuildingPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[BuildingView] | None = None
    total: int
    page: int
    size: int
    pages: int


class BuildingPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class BuildingDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    apartment: Mappeds['Apartment'
                      ] = relationship(back_populates='building')

    type             'Тип дома: Кирпичный,
                                Панельный,
                                Блочный,
                                Монолитный,
                                Монолитно-кирпичный,
                                Деревянный'
    concierge        'Консьерж'
    garb_chute       'Мусоропровод'
    gas              'Газ'
    year_constr      'Год постройки'
    dismant:         'Запланирован снос'
    el_pass          'Лифт пассажирский: нет, 1, 2, 3, 4'
    el_freight       'Лифт грузовой: нет, 1, 2, 3, 4'
    yard_closed      'Двор: Закрытая территория'
    yard_playground  'Двор: Детская площадка'
    yard_sports      'Двор: Спортивная площадка'
    park_undegr      'Парковка: Подземная'
    park_abov        'Парковка: Надземная многоуровневая'
    park_open        'Парковка: Открытая во дворе']
    park_behbarrier  'Парковка: За шлагбаумом во дворе'
"""
