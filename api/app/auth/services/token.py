from datetime import datetime, timedelta, timezone
from typing import (
    Union,
    Any
)

from jose import jwt
from fastapi import (
    HTTPException,
    status
)

from .black_list import add_blacklist_token


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = 'cc2efdfaff2550ffb10f7492a685fdce9759281baf270b7c4573a045845\
3b45f'
JWT_REFRESH_SECRET_KEY = 'dd4395b7963c5343e9e9dd70a4ee3bb03a8e1296b0c08074843\
694a667614ddb'


def create_access_token(subject: Union[str, Any],
                        expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    return jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)


def create_refresh_token(subject: Union[str, Any],
                         expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    return jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)


def update_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token,
                             JWT_REFRESH_SECRET_KEY,
                             algorithms=[ALGORITHM])
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Недействительный токен доверия!",
        ) from e

    if datetime.fromtimestamp(payload.get("exp"), timezone.utc) > datetime.now(
        timezone.utc
    ):
        add_blacklist_token(refresh_token)
        return {
            "access_token": create_access_token(payload["sub"]),
            "refresh_token": create_refresh_token(payload["sub"]),
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Недействительный токен доверия!",
        )
