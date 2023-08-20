from fastapi_jwt_auth import AuthJWT

from settings.settings import Settings


@AuthJWT.load_config
def get_config():
    return Settings()
