from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseModelAuto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand_id: int = Field(description='Модель авто')
    model: str = Field(description='Модель авто')


class ModelAutoID(BaseModel):
    id: int = Field(description='ID модели авто')


class ModelAutoView(BaseModelAuto, ModelAutoID):
    pass


class ModelAutoCreate(BaseModelAuto):
    pass


class ModelAutoUpdate(BaseModelAuto, ModelAutoID):
    pass

# #############################################################


class ModelAutoResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ModelAutoView | None = None


class ModelAutoError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ModelAutoPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ModelAutoView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ModelAutoPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ModelAutoDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    body: Mapped[list['BodyType']] = relationship(back_populates='model')
    brand: Mapped['BrandAuto'] = relationship(back_populates='model')

    model 'Модель авто'
"""
