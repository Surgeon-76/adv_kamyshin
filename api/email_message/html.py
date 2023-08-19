def get_message_code(code):
    style = """
    <style>
        .header{
            max-width: 100%;
            min-height: 20vh;
            padding: 1em;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header img{
            max-width: 100%;
        }
        .text-email{
            min-height: 60vh;
            max-width: 100%;
            padding: 1em;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .detail{
            font-size: 1.3em;
            font-weight: bold;
        }

        h3{

        }
        .text-detail{


        }
        span{
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """
    # </html>
    # '''.format(**locals())
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
            {style}
        </style>
    </head>
    <body>
        <div class="header">
            <img src="https://cdn1.ozone.ru/multimedia/c1200/1013943426.jpg" alt="">
        </div>
        <div class="text-email">
            <h3>Здравствуйте ,Уважаемый(ая)  пользователь сервиса Поиск Услуг!</h3>

            <h4>Код для восстановления пароля</h4>

            <div class="text-detail">
                <p class="detail">Детали сообщения :</p>
                <p><span>Ваш проверочный код: </span> {code}</p>
            </div>
            <div>
                <p>Благодарим за доверие к нашему сервису!</p>
            </div>
        </div>
    </body>
    </html>
    '''.format(**locals())
    return html
