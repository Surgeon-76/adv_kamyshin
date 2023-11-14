from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseRulesOfSett(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    guest: str | None = Field(description='Максимум гостей',
                              default=None)
    kinds: bool = Field(default='Можно с детьми',
                        default=False)
    pets: bool = Field(description='Можно с животными',
                       default=False)
    smoking: bool = Field(description='Разрешено курить',
                          default=False)
    paty: bool | None = Field(description='Разрешены вечеринки',
                              default=None)
    docs: bool | None = Field(description='Есть отчетные документы',
                              default=None)
    monthly: bool | None = Field(description='Возможна помесячная аренда',
                                 default=None)


class RulesOfSettID(BaseModel):
    id: int = Field(description='ID условий заселения')


class RulesOfSettView(BaseRulesOfSett, RulesOfSettID):
    pass


class RulesOfSettCreate(BaseRulesOfSett):
    pass


class RulesOfSettUpdate(BaseRulesOfSett, RulesOfSettID):
    pass

# #############################################################


class RulesOfSettResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: RulesOfSettView | None = None


class RulesOfSettError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class RulesOfSettPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[RulesOfSettView] | None = None
    total: int
    page: int
    size: int
    pages: int


class RulesOfSettPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class RulesOfSettDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    rooms: Mappeds['Rooms'] = relationship(back_populates='rules')
    apartment: Mappeds['Apartment'] = relationship(back_populates='rules')
    construction: Mappeds['Construction'
                         ] = relationship(back_populates='rules')

    guest   'Максимум гостей: 1, ... , 49, 50 и более'
    kinds   'Можно с детьми: Да, Нет'
    pets    'Можно с животными: Да, Нет'
    smoking 'Разрешено курить: Да, Нет'
    paty    'Разрешены вечеринки: Да, Нет'
    docs    'Есть отчетные документы: Да, Нет'
    monthly 'Возможна помесячная аренда: Да, Нет'
"""
