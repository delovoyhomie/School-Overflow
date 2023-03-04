import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Адрес электронной почты отправителя и получателя
sender_email = "example@yandex.ru"
recipient_email = "example2@gmail.com"

# Имя пользователя и пароль для доступа к учетной записи Yandex
smtp_username = "example@yandex.ru"
smtp_password = "password"

# Тема письма
subject = "Test email from Python"

# Текст письма
text = "Hello from Python!"

# Создание объекта MIMEMultipart и добавление темы и текста письма
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(text))

# Отправка письма через SMTP-сервер Yandex
try:
    smtp_connection = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    smtp_connection.login(smtp_username, smtp_password)
    smtp_connection.sendmail(sender_email, recipient_email, msg.as_string())
    smtp_connection.close()
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email: ", e)
