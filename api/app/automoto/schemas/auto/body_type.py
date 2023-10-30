from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseBodyType(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    model_id: int = Field(description='--> ID модели авто')
    type_body: str = Field(description='Тип кузова',
                           default='Седан')


class BodyTypeID(BaseModel):
    id: int = Field(description='ID типа кузова')


class BodyTypeView(BaseBodyType, BodyTypeID):
    pass


class BodyTypeCreate(BaseBodyType):
    pass


class BodyTypeUpdate(BaseBodyType, BodyTypeID):
    pass

# #############################################################


class BodyTypeResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: BodyTypeView | None = None


class BodyTypeError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class BodyTypePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[BodyTypeView] | None = None
    total: int
    page: int
    size: int
    pages: int


class BodyTypePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class BodyTypeDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    avtotth: Mapped['AvtoTth'] = relationship(back_populates='bodytype',
                                              uselist=False)
    model: Mapped['ModelAuto'] = relationship(back_populates='body')

    type_body 'Тип кузова: Седан, Хэтчбек, Универсал, Кабриолет, Купе'
"""
