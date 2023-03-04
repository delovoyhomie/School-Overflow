import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from middleware.document import generate_name_files as gener
from common.preferences import FULL_LINK

class Emailer:
    def __init__(self) -> None:
        self.sender_email = "SchoolOverflows@yandex.ru"
        self.smtp_username = "SchoolOverflows@yandex.ru"
        self.smtp_password = "ftS-9Yh-mpq-A6p"


    def send_email(self, recipient_email, subject, text) -> bool:

        # Создание объекта MIMEMultipart и добавление темы и текста письма
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        # Отправка письма через SMTP-сервер Yandex
        try:
            smtp_connection = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            smtp_connection.login(self.smtp_username, self.smtp_password)
            smtp_connection.sendmail(self.sender_email, recipient_email, msg.as_string())
            smtp_connection.close()
            print("Email sent successfully!")
            return True
        except Exception as e:
            print("Error sending email: ", e)
            return False
        
    def confirmation_by_email(self, address):
        try:
            link = gener(30)
            text = f'''Здравствуйте!
На сайте schooloverflow.ru была произведена регистрация с использованием вашей электронной почты.
Email: {address}
Для подтверждения регистрации пройдите по ссылке:
{FULL_LINK}/{link}

С уважением,
Администрация schooloverflow.ru'''
            if self.send_email(address, 'Подтверждение аккаунта SchoolOverflow', text):
                return link
            return False
        except:
            return False
        
    def test(self):
        self.confirmation_by_email('georgeboiko0411@gmail.com')
