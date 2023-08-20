from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = None
    postgres_password: str = None
    postgres_db: str = None
    debug: bool = True
    authjwt_secret_key: str = "secret"
    email_login: str = 'tumanov.gl@yandex.ru'
    email_password: str = 'Glebtumanov89@'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
