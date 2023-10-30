from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseMotoAddit(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand: str = Field(description='Бренд мото',
                       default='')
    logo: str = Field(description='Логотип',
                      default='')


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




class MotoAddit(Base):
    __tablename__ = 'moto_addit'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    starter: Mapped[bool] = mapped_column(Boolean, default=False)
    abs: Mapped[bool] = mapped_column(Boolean, default=False)
    tcs: Mapped[bool] = mapped_column(Boolean, default=False)
    start_stop: Mapped[bool] = mapped_column(Boolean, default=False)
    windscreen: Mapped[bool] = mapped_column(Boolean, default=False)
    trunk: Mapped[bool] = mapped_column(Boolean, default=False)

    tth: Mapped['MotoTth'] = relationship(back_populates='addit',
                                          uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    starter    'Электростартер'
    abs        'Антиблокировочная система'
    tcs        'Противопробуксовочная система(трэкшн-контроль)'
    start_stop 'Система "старт-стоп"'
    windscreen 'Ветровое стекло'
    trunk      'Кофр'
"""
