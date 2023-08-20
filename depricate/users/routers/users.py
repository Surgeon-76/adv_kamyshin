from fastapi import (
                    APIRouter,
                    HTTPException,
                    status,
                    Depends
                    )

from ..models.users import User
from ..schemas.user import (
    UpdateUser,
    UpdateUserPassword
)
from services.auth import AuthJWT


app = APIRouter(
                prefix='/api/v1/users',
                tags=['Пользователи:']
                )


@app.get("/", summary=('Список пользователей'))
async def get_list():
    return await User.objects.all()


@app.get('/{id}/', summary=('Пользователь по id'))
async def get_one(id: int):
    user = await User.objects.get_or_none(id=id)
    if not user:
        raise HTTPException(status_code=404, detail="Нет такого пользователя")
    return user


@app.put('/update/{id}/', summary='Редактирование пользователя',
         status_code=status.HTTP_201_CREATED)
async def update(id: int, item: UpdateUser):
    user = await User.objects.get_or_none(id=id)
    return await user.update(**item.dict())


@app.put('/change-password/', summary='Обновление пароля',
         status_code=status.HTTP_201_CREATED)
async def update_password(item: UpdateUserPassword,
                          Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    if item.phone:
        user = await User.objects.get_or_none(phone=item.phone)
    if item.email:
        user = await User.objects.get_or_none(email=item.email)
    if user.id == current_user:
        return await user.update(**item.dict())
    return HTTPException(status_code=409,
                         detail="Попытка изменить не свои данные!")


@app.get('/user/get/', summary='User по токену')
async def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    user = await User.objects.get(id=current_user)
    return user


@app.delete('/delete/', summary='Удаление Пользователя'
            )
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    user = await User.objects.get(id=current_user)
    deluser = await User.objects.get_or_none(id=id)
    if not deluser:
        raise HTTPException(status_code=404, detail="Not found!")
    if user.admission == 0:
        await deluser.advts.clear()
        return await deluser.delete()
    return HTTPException(status_code=401, detail="No access!")


@app.get('/phone/{phone}/')
async def code_reset_password(phone: str):
    user = await User.objects.get_or_none(phone=phone)
    if not user:
        raise HTTPException(status_code=404, detail="Нет такого пользователя")
    return {'message': 'ok'}


@app.get('/email/{email}/')
async def code_reset_password_2(email: str):
    user = await User.objects.get_or_none(email=email)
    if not user:
        raise HTTPException(status_code=404, detail="Нет такого пользователя")
    return {'message': 'ok'}
