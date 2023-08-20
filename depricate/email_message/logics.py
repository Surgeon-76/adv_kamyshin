import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings.settings import settings


def send_message_mail(email, message, subject):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = settings.email_login
    msg['To'] = email
    part2 = MIMEText(message, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.yandex.ru', 465)
    mail.ehlo()
    mail.starttls()
    mail.login(settings.email_login, settings.email_password)
    mail.sendmail(settings.email_login, email, msg.as_string())
    mail.quit()
