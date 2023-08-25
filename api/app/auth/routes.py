from fastapi import (
                    APIRouter,
                    HTTPException,
                    status,
                    Depends
                    )
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from config.sessions import get_session
from ..system.ver_user import get_user_by_id
from .schemas import (
    SystemUser,
    UserOutSystem,
    TokenRefresh
)
from .services.black_list import (
    add_blacklist_token,
    is_token_blacklisted
)
from .services.get_user import get_current_user
from .services.token import (
    create_access_token,
    create_refresh_token,
    update_token
)
from .services.hash_pass import verify_password

app = APIRouter(
                prefix='/api/v1/auth',
                tags=['Авторизация:']
                )


@app.post('/login',
          summary="Создание токенов доступа и обновления для пользователя")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_session)):
    if '@' not in form_data.username:
        form_data.username = ''.join(
            [n for n in form_data.username if n.isdigit() or n == '+'])

    user = (await get_user_by_id(
        form_data.username, db))

    if (user is None) or (not verify_password(form_data.password,
                                              user[0].password)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не верный email, телефон или пароль!"
        )

    return {
        "access_token": create_access_token(user[0].email),
        "refresh_token": create_refresh_token(user[0].email),
    }


@app.get('/me', summary='Информация о вошедшем в систему пользователе',
         response_model=UserOutSystem)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user


@app.post("/logout")
async def logout(token_refresh: TokenRefresh,
                 user: str = Depends(get_current_user)):

    if add_blacklist_token(token_refresh.refresh):
        return {"result": "ok"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Недействительный токен доверия!",
    )


@app.post("/refresh/")
async def refresh(token_refresh: TokenRefresh):

    token = token_refresh.refresh
    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Недействительный токен доверия!",
        )
    return update_token(token)
