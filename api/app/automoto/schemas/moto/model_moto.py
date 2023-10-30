from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseModelMoto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand_id: int = Field(description='--> brand_moto.id')
    model: str = Field(description='Модель мото',
                       default='')


class ModelMotoID(BaseModel):
    id: int = Field(description='ID модели мото')


class ModelMotoView(BaseModelMoto, ModelMotoID):
    pass


class ModelMotoCreate(BaseModelMoto):
    pass


class ModelMotoUpdate(BaseModelMoto, ModelMotoID):
    pass

# #############################################################


class ModelMotoResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ModelMotoView | None = None


class ModelMotoError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ModelMotoPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ModelMotoView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ModelMotoPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ModelMotoDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    brand: Mapped['ModelMoto'] = relationship(back_populates='model')
    mototype: Mapped[list['MotoType']] = relationship(back_populates='model')

    model 'Модель мото'
"""
