from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = None
    postgres_password: str = None
    postgres_db: str = None
    debug: bool = False
    docker: bool = False
    secret_key: str = "18e5e4d5ac0f70718817f519d40990583bd629a99509855bfd70246aa72e7040"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings: Settings = Settings()
