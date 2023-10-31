from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseMotoType(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    model_id: int = Field(description='--> model_moto.id')
    type_moto: str = Field(description='Тип',
                           default='Туристический')


class MotoTypeID(BaseModel):
    id: int = Field(description='ID бренда мото')


class MotoTypeView(BaseMotoType, MotoTypeID):
    pass


class MotoTypeCreate(BaseMotoType):
    pass


class MotoTypeUpdate(BaseMotoType, MotoTypeID):
    pass

# #############################################################


class MotoTypeResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: MotoTypeView | None = None


class MotoTypeError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class MotoTypePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[MotoTypeView] | None = None
    total: int
    page: int
    size: int
    pages: int


class MotoTypePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class MotoTypeDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    mototth: Mapped['MotoTth'] = relationship(back_populates='mototype',
                                              uselist=False)
    model: Mapped['ModelMoto'] = relationship(back_populates='mototype')

    type_moto 'Спортивный, Туристический, Чоппер и т.д.'
"""
