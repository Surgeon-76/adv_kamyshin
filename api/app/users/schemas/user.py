from typing import Annotated, Any

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator
)

# TODO: сделать None в полях


class BaseUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    google_id: str | None = Field(description='google_id',
                                  default=None)
    yandex_id: str | None = Field(description='yandex_id',
                                  default=None)
    telegram_id: str | None = Field(description='telegram_id',
                                    default=None)
    vk_id: str | None = Field(description='vk_id',
                              default=None)
    username: str = Field(description='Никнейм пользователя',
                          default='user')
    first_name: str | None = Field(description='Имя пользователя',
                                   default='')
    last_name: str | None = Field(description='Фамилия пользователя',
                                  default='')
    email: str | None = Field(description='email пользователя',
                              default='')
    avatar: str | None = Field(description='URL аватара',
                               default='')

    is_admin: bool = Field(description='Админ', default=False)
    is_client: bool = Field(description='Пользователь', default=True)
    is_active: bool = Field(description='Активный', default=True)
    
    @field_validator('google_id',
                     'yandex_id',
                     'telegram_id',
                     'vk_id',
                     'first_name',
                     'last_name',
                     'email',
                     'avatar')
    @classmethod
    def check_field_none(cls, field) -> Any:
        if field in ['string', '']:
            field = None
        return field


class UserID(BaseModel):
    id: int = Field(description='ID пользователя')


class UserView(BaseUser, UserID):
    pass


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser, UserID):
    pass

# ##############################################################


class UserResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: UserView | None = None


class UserError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class UserPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[UserView] | None = None
    total: int
    page: int
    size: int
    pages: int


class UserPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class UserDel(BaseModel):     # TODO: Проверить явную необходимость этой модели
    status: str = 'succes'
    status_code: int
    payload: dict | None = None

################################################################
