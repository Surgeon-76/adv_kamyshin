from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseTermTransaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ipoteka: bool = Field(description='Можно в ипотеку',
                          default=False)
    part: bool = Field(description='Продажа доли',
                       default=False)


class TermTransactionID(BaseModel):
    id: int = Field(description='ID услов сделки')


class TermTransactionView(BaseTermTransaction, TermTransactionID):
    pass


class TermTransactionCreate(BaseTermTransaction):
    pass


class TermTransactionUpdate(BaseTermTransaction, TermTransactionID):
    pass

# #############################################################


class TermTransactionResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: TermTransactionView | None = None


class TermTransactionError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class TermTransactionPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[TermTransactionView] | None = None
    total: int
    page: int
    size: int
    pages: int


class TermTransactionPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class TermTransactionDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    rooms: Mappeds['Rooms'] = relationship(back_populates='transaction')
    apartment: Mappeds['Apartment'] = relationship(back_populates='transaction')
    construction: Mappeds['Construction'
                         ] = relationship(back_populates='transaction')

    ipoteka  'Можно в ипотеку']
    part     'Продажа доли']
"""
