from middleware.db import DB

class User:
    def __init__(self) -> None:
        self.db = DB()

    def create_user(self, login, passw, tg_id):
        if self.db.write('users', "login,passw,tg_id", f"'{login}','{passw}','{tg_id}'"):
            pass