# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# import smtplib
# login = 'shooloverflow@yandex.ru'
# password = 'voikyszpsjtqypsj'

# def send_email(to_addr, subject, text):
#     msg = MIMEMultipart()
#     msg['From'] = login
#     msg['TO'] = login
#     msg['Subject'] = subject
#     msg.attach(
#         MIMEText(text, 'plain')
#     )

#     server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
#     server.ehlo(login)
#     server.login(login, password)
#     server.auth_plain()
#     server.send_message(msg)
#     server.quit()

import smtplib

def send_email(from_addr, to_addr, subject, text, encode='utf-8'):

    # оставшиеся настройки
    passwd = "xDdlAOe?CXD#TxjT"
    server = "smtp.yandex.ru"
    port = 587
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}", 
           f"Subject: {subject}", mime, charset, "", text))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

if __name__ == "__main__":
    from_addr = "schooloverflow@yandex.ru"
    to_addr = "dmodv@vk.com"
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(from_addr, to_addr, subject, text)


# if __name__=='__main__':
#     send_email('dmodv@vk.com', 'HEader', 'testing msg')