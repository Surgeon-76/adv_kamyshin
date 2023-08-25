from datetime import datetime

from fastapi import (
    HTTPException,
    status,
    Depends
)
from fastapi.security import OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer
from jose import (
    jwt,
    JWTError
)
from pydantic import ValidationError

from ..schemas import TokenPayload, SystemUser
from app.system.ver_user import get_user_by_id
from config.sessions import get_session
from .token import (
    ALGORITHM,
    JWT_SECRET_KEY
)
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)
                           ) -> SystemUser:
    db = await anext(get_session())
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Срок действия токена истек",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Учетные данные не подтверждены!",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e

    user = await get_user_by_id(token_data.sub, db)
    # print(token_data.sub)
    # print(user)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Не удалось найти пользователя",
        )

    return user[0]
