from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BasePts(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    transport_id: int = Field(description='--> transport.id')
    pts: str = Field(description='Номер ПТС',
                     default='Нет')


class PtsID(BaseModel):
    id: int = Field(description='ID ПТС')


class PtsView(BasePts, PtsID):
    pass


class PtsCreate(BasePts):
    pass


class PtsUpdate(BasePts, PtsID):
    pass

# #############################################################


class PtsResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: PtsView | None = None


class PtsError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class PtsPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[PtsView] | None = None
    total: int
    page: int
    size: int
    pages: int


class PtsPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class PtsDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    transport: Mapped['Transport'] = relationship(back_populates='pts',
                                                  uselist=False)

    pts 'Номер ПТС'
"""
