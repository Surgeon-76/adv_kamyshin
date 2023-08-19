import random

from fastapi import (
    APIRouter,
    BackgroundTasks
)

from .logics import send_message_mail
from .html import get_message_code


app = APIRouter(
                prefix='/api/v1/email',
                tags=['Email:']
                )


@app.post('/{email}/')
async def code_reset_password(email: str, background_tasks: BackgroundTasks):
    # user = await User.objects.get_or_none(email=email)
    # if not user:
    #     raise HTTPException(status_code=404,
    #                         detail="Нет такого пользователя")
    code = ''.join([str(random.randint(0, 9)) for i in range(0, 6)])
    message = get_message_code(code)
    send_message_mail(email, message=message, subject='Восстановление пароля')
    # background_tasks.add_task(send_message_mail, email, message=message,
    # subject='Восстановление пароля')
    return {'code': code}
