from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    postgres_user: str = None
    postgres_password: str = None
    postgres_db: str = None
    debug: bool = False
    docker: bool = False
    secret_key: str = "626887326a8aac7a3c93ff0173e442653c60afc46be9a192502dba2b77ff5a93"


settings: Settings = Settings()
