import requests

from middleware.db import DB
from middleware.hasher import *
from middleware.document import save_document


class User:
    def __init__(self) -> None:
        self.db = DB()
        self.db.create_db()
        self.token_tg = '5930876964:AAEqhx4l9dsJFK_Q9mVrCDncs2N33dfj0GU'

    def send_alert_tg(self, text, chat_id):
        url = f"https://api.telegram.org/bot{self.token_tg}/sendMessage"
        response = requests.post(url, data={'chat_id': chat_id, 'text': text})
        return response.json()['ok']

    def create_user(self, login, passw, mail):
        if self.db.read_one('users', '*', f"login='{login}'") == None:
            if self.db.write('users', "login,passw,mail", f"'{login}','{hash_password(passw)}','{mail}'"):
                return {'status': 'True'}
            return {'status': 'False'}
        return {'status': 'Busy'}
    
    def check_user(self, login, passw):
        hpassw = self.db.read_one('users', 'passw', f"login='{login}'")[0]
        return check_password(hpassw, passw)
    
    def create_post(self, login, description, body, label, doc):
        if doc != None:
            doc = save_document(login, doc)
        self.db.write('posts', 'login, description, body, label, doc', f"'{login}', '{description}', '{body}', '{label}', '{doc}'")

    def create_answ(self, login, body, id_post, doc):
        if doc != None:
            doc = save_document(login, doc)
        self.db.write('answ', 'login, body, id_post, doc, statis', f"'{login}', '{body}', '{id_post}', '{doc}', '0'")

    def read_posts(self, filter):
        param = filter['param']
        values = filter['values']
        tbl = 'posts' if filter==None else f"posts WHERE {param}='{values}'"
        ans = self.db.read(tbl, '*')
        dt = {}
        for i in range(len(ans)):
            dt[str(i)] = {'id':ans[i][0],
                          'login':ans[i][1],
                          'text_body':ans[i][2],
                          'description':ans[i][3],
                          'label':ans[i][4],
                          'doc':ans[i][5]}
        return dt
    
    def read_current_post(self, id_post):
        ans = self.db.read(f"answ WHERE id_post='{id_post}'", 'id,statis,login,text_body,doc, create_at')
        post = self.db.read(f"posts WHERE id='{id_post}'", 'id,login,text_body,description,label,doc,create_at')[0]
        print(ans, post)
        dt = {'post':   { 'id':post[0],
                          'login':post[1],
                          'text_body':post[2],
                          'description':post[3],
                          'label':post[4],
                          'doc':post[5],
                          'create_at':post[6]
                          }}
        
        for i in range(len(ans)):
            dt[str(i)] = {'id':ans[i][0],
                          'statis':ans[i][1],
                          'login':ans[i][2],
                          'text_body':ans[i][3],
                          'doc':ans[i][4],
                          'create_at':post[5]}
            
        return dt
    
    def read_current_user(self, login):
        user = self.db.read_one('users', '*' , f"login='{login}'")
        print(user)
        dt = {'user':   { 'id':user[0],
                          'login':user[1],
                          'mail': user[3]},
                            'answer': {},
                            'posts': {}}
        posts = self.db.read(f"posts WHERE login='{login}'", 'id,description,label')
        ans = self.db.read(f"answ WHERE login='{login}'", 'id,body,statis')
        print(posts, ans)
        if ans:
            for i in range(len(ans)):
                dt['answer'][str(i)] = {'id':ans[i][0],
                            'statis':ans[i][2],
                            'text_body':ans[i][1]}
        else: dt['answer']['0'] = 'None'

        if posts != []:
            for i in range(len(posts)):
                dt['posts'][str(i)] = {
                                'id': posts[i][0],
                                'label':posts[i][2],
                                'description':posts[i][1]}
        else: dt['posts']['0']='None'

        return dt
# igorkravchenko
# dmodv