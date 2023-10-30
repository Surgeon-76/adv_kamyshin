from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseHistory(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    transport_id: int = Field(description='--> ID transport')
    condition: str = Field(description='Состояние',
                           default='б/у')
    odometer: int = Field(description='Пробег',
                          default=0)
    orig_pts: str = Field(description='ПТС',
                          default='Оригинал')
    num_of_own: int = Field(description='Количество владельцев',
                            default=1)


class HistoryID(BaseModel):
    id: int = Field(description='ID истории транспортного средства')


class HistoryView(BaseHistory, HistoryID):
    pass


class HistoryCreate(BaseHistory):
    pass


class HistoryUpdate(BaseHistory, HistoryID):
    pass

# #############################################################


class HistoryResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: HistoryView | None = None


class HistoryError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class HistoryPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[HistoryView] | None = None
    total: int
    page: int
    size: int
    pages: int


class HistoryPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class HistoryDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    transport: 'Transport'] = relationship(back_populates='history',
                                                  uselist=False)

    condition  'Состояние: Новый, б/у, На запчасти'
    odometer Пробег
    orig_pts  'Оригинал, Дубликат, Электронный, нет'
    num_of_own  'Количество владельцев'
"""
