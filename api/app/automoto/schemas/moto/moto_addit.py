from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseMotoAddit(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    starter: bool = Field(description='Электростартер',
                          default=False)
    abs: bool = Field(description='Антиблокировочная система',
                      default=False)
    tcs: bool = Field(
        description='Противопробуксовочная система(трэкшн-контроль)',
        default=False)
    start_stop: bool = Field(description='Система "старт-стоп"',
                             default=False)
    windscreen: bool = Field(description='Ветровое стекло',
                             default=False)
    trunk: bool = Field(description='Кофр',
                        default=False)


class MotoAdditID(BaseModel):
    id: int = Field(description='ID дополнительных параметров мото')


class MotoAdditView(BaseMotoAddit, MotoAdditID):
    pass


class MotoAdditCreate(BaseMotoAddit):
    pass


class MotoAdditUpdate(BaseMotoAddit, MotoAdditID):
    pass

# #############################################################


class MotoAdditResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: MotoAdditView | None = None


class MotoAdditError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class MotoAdditPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[MotoAdditView] | None = None
    total: int
    page: int
    size: int
    pages: int


class MotoAdditPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class MotoAdditDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    tth: Mappeds['MotoTth'] = relationship(back_populates='addit',
                                          uselist=False)

    starter    'Электростартер'
    abs        'Антиблокировочная система'
    tcs        'Противопробуксовочная система(трэкшн-контроль)'
    start_stop 'Система "старт-стоп"'
    windscreen 'Ветровое стекло'
    trunk      'Кофр'
"""
