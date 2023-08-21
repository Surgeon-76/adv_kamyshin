from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    google_id: Annotated[[int | None],
                         Field(description='google_id',
                               default=None)]
    yandex_id: Annotated[[int | None],
                         Field(description='yandex_id',
                               default=None)]
    telegram_id: Annotated[[int | None],
                           Field(description='telegram_id')]
    vk_id: Annotated[[int | None],
                     Field(description='vk_id',
                           default=None)]
    username: str = Field(description='Никнейм пользователя',
                          default='user')
    first_name: str | None = Field(description='Имя пользователя',
                                   default=None)
    last_name: str | None = Field(description='Фамилия пользователя',
                                  default=None)
    avatar: str | None = Field(description='URL аватара')


class UserID(BaseModel):
    id: int = Field(description='ID пользователя')


class CreateUser(BaseUser):
    pass


class UpdateUser(BaseUser, UserID):
    pass
