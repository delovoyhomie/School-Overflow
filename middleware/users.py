import requests

from middleware.db import DB
from middleware.hasher import *


class User:
    def __init__(self) -> None:
        self.db = DB()
        self.db.create_db()
        self.token_tg = '5930876964:AAEqhx4l9dsJFK_Q9mVrCDncs2N33dfj0GU'

    def send_alert_tg(self, text, chat_id):
        url = f"https://api.telegram.org/bot{self.token_tg}/sendMessage"
        response = requests.post(url, data={'chat_id': chat_id, 'text': text})
        return response.json()['ok']

    def create_user(self, login, passw):
        if self.db.read_one('users', '*', f"login='{login}'") == None:
            if self.db.write('users', "login,passw", f"'{login}','{hash_password(passw)}'"):
                return {'status': 'True'}
            return {'status': 'False'}
        return {'status': 'Busy'}
    
    def check_user(self, login, passw):
        hpassw = self.db.read_one('users', 'passw', f"login='{login}'")[0]
        return check_password(hpassw, passw)
    
    def create_post(self, login, description, body, label, doc):
        self.db.write('posts', 'login, description, body, label, doc', f'{login}, {description}, {body}, {label}, {doc}')
