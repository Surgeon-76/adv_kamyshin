from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseCommTransaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str = Field(description='Тип сделки',
                      default='Продажа')
    renter: bool = Field(description='Арендатор',
                         default=False)
    price_type: str = Field(description='Цена',
                            default='За всё')


class CommTransactionID(BaseModel):
    id: int = Field(description='ID коммер усл сделки')


class CommTransactionView(BaseCommTransaction, CommTransactionID):
    pass


class CommTransactionCreate(BaseCommTransaction):
    pass


class CommTransactionUpdate(BaseCommTransaction, CommTransactionID):
    pass

# #############################################################


class CommTransactionResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: CommTransactionView | None = None


class CommTransactionError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class CommTransactionPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[CommTransactionView] | None = None
    total: int
    page: int
    size: int
    pages: int


class CommTransactionPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class CommTransactionDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    commerce: Mappeds['CommBuilding'
                     ] = relationship(back_populates='transaction',
                                      uselist=False)

    type       'Тип сделки: Продажа, Переуступка права аренды'
    renter     'Арендатор: Помещение сдано'
    price_type 'Цена: За всё, За м*2'
"""
