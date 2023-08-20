from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)

from ..models.users import User
from ..schemas.user import CreateUser
from services.auth import AuthJWT
from services.user_hash import verify_password


app = APIRouter(
    prefix='/api/v1/auth',
    tags=['Авторизация:']
)


@app.post('/registration/', summary=('Регистрация нового Пользователя'),
          status_code=status.HTTP_201_CREATED)
async def create(new_user: CreateUser):
    return await User(**new_user.dict()).save()


@app.post('/verefication', summary=('Верификация нового Пользователя'),
          status_code=status.HTTP_201_CREATED)
async def verefication_data(new_user: CreateUser):
    if new_user.phone:
        user = await User.objects.get_or_none(phone=new_user.phone)
        if user:
            raise HTTPException(
                status_code=400,
                detail="Пользователь с таким телефоном уже зарегистрирован"
            )
    if new_user.email:
        user = await User.objects.get_or_none(email=new_user.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="Пользователь с таким email уже зарегистрирован"
            )
    if not new_user.agreement:
        raise HTTPException(
            status_code=403,
            detail="Необходимо подтвердить согласие на обработку \
                персональных данных!"
        )

    return {'message': 'регистрация может быть продолжена'}


@app.post('/login')
async def login(auth_user: CreateUser, Authorize: AuthJWT = Depends()):
    if auth_user.email:
        user = await User.objects.get_or_none(email=auth_user.email)
        if not user:
            raise HTTPException(
                status_code=401, detail="Неверный логин или пароль")
    if auth_user.phone:
        user = await User.objects.get_or_none(phone=auth_user.phone)
        if not user:
            raise HTTPException(
                status_code=401, detail="Неверный логин или пароль")
    if verify_password(user.password, auth_user.password):
        access_token = Authorize.create_access_token(subject=user.id)
        refresh_token = Authorize.create_refresh_token(subject=user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}
    else:
        raise HTTPException(
            status_code=401, detail="Неверный логин или пароль")


@app.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}
