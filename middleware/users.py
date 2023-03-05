import requests

from middleware.db import DB
from middleware.hasher import *
from middleware.document import save_document
from middleware.sender_email import Emailer


class User:
    def __init__(self) -> None:
        self.db = DB()
        self.db.create_db()
        self.email = Emailer()

    def create_user(self, login, passw, mail):
        if self.db.read_one('users', '*', f"login='{login}'") == None:
            link = self.email.confirmation_by_email(mail)
            if self.db.write('users', "login,passw,mail,mail_status", f"'{login}','{hash_password(passw)}','{mail}','{link}'"):
                return {'status': 'True'}
            return {'status': 'False'}
        return {'status': 'Busy'}
    
    def confirmation_user(self, link):
        login = self.db.read_one('users', 'login', f"mail_status='{link}'")
        print(login)
        if login:
            if self.db.update('users', f"mail_status='1'", f"login='{login[0]}'"):
                return "<h1>Почта подтверждена успешно</h1>"
            return "<h1>Технические неполадки</h1>"
        else:
            return "<h1>Ссылка не действительна</h1>"
    
    def check_user(self, login, passw):
        hpassw = self.db.read_one('users', 'passw,mail_status', f"login='{login}'")[0]
        if 0:
            return 'mail'
        return check_password(hpassw, passw)
    
    def create_post(self, login, description, body, label, doc):
        if doc != None:
            doc = save_document(login, doc)
        self.db.write('posts', 'login, description, body, label, doc', f"'{login}', '{description}', '{body}', '{label}', '{doc}'")

    def create_answ(self, login, body, id_post, doc, id_answ):
        if doc != None:
            doc = save_document(login, doc)
        self.db.write('answ', 'login, body, id_post, doc, statis, id_answ', f"'{login}', '{body}', '{id_post}', '{doc}', '0', '{id_answ}'")

    def read_posts(self, filter):
        if filter != None:
            param = filter['param']
            values = filter['values']
        tbl = 'posts' if filter==None else f"posts WHERE {param}='{values}'"
        ans = self.db.read(tbl, 'id,login,description,body,label,doc,status,created_at')
        dt = {}
        for i in range(len(ans)):
            dt[str(i)] = {'id':ans[i][0],
                          'login':ans[i][1],
                          'description':ans[i][2],
                          'body':ans[i][3],
                          'label':ans[i][4],
                          'doc':ans[i][5],
                          'status':ans[i][6],
                          'created_at':ans[i][7]}
            


        return dt
    
    def read_current_post(self, id_post):
        ans = self.db.read(f"answ WHERE id_post='{id_post}'", 'id,statis,login,body,doc,created_at,id_answ')
        post = self.db.read(f"posts WHERE id='{id_post}'", 'id,login,description,body,label,doc,status,created_at')[0]
        print(ans, post)
        dt = {'post':   {'id':post[0],
                          'login':post[1],
                          'description':post[2],
                          'body':post[3],
                          'label':post[4],
                          'doc':post[5],
                          'status':post[6],
                          'created_at':post[7]},
                'answer' : []}
        print(ans)
        if ans != 0:
            for i in range(len(ans)):
                dt['answer'].append({'id':ans[i][0],
                            'statis':ans[i][1],
                            'login':ans[i][2],
                            'text_body':ans[i][3],
                            'doc':ans[i][4],
                            'create_at':ans[i][5],
                            'id_answ':ans[i][6]})
        else: dt['answer'] = 'None'
            
        return dt
    
    def read_current_user(self, login):
        user = self.db.read_one('users', 'id,login,mail,created_at' , f"login='{login}'")
        print(user)
        dt = {'user':   { 'id':user[0],
                          'login':user[1],
                          'mail': user[2],
                          'created_at': user[3]},
                          'answer': [],
                          'posts': []}
        posts = self.db.read(f"posts WHERE login='{login}'", 'id,description,label,status')
        ans = self.db.read(f"answ WHERE login='{login}'", 'id,body,statis')
        print(posts, ans)
        if ans:
            for i in range(len(ans)):
                dt['answer'].append({'id':ans[i][0],
                                        'text_body':ans[i][1],
                                        'statis':ans[i][2]
                                        })
        else: dt['answer'].append('None')

        if posts != []:
            for i in range(len(posts)):
                dt['posts'].append({ 'id': posts[i][0],
                                        'description':posts[i][1],
                                        'label':posts[i][2],
                                        'status':posts[i][3]})
        else: dt['posts'].append('None')

        return dt
    
    def upd_statis(self, id, operator):
        stat = self.db.read(f"answ WHERE id='{id}'", 'statis')[0][0]
        print(stat)
        if operator == '+':
            stat = int(stat)+1
        elif operator == '-':
            stat = int(stat)-1
        return self.db.update('answ', f"statis='{stat}'", f"id='{id}'")
    
    def upd_status(self, id, login, operator):
        data = self.db.read(f"answ WHERE id='{id}'", 'id_post')[0][0]
        print(data)
        login_is = self.db.read(f"posts WHERE id='{data}'", 'login')[0][0]
        print(login, login_is)
        if login==login_is:
            print('YEEES')
            if operator == '+':
                stat = 1
            elif operator == '-':
                stat = 0
        self.db.update('answ', f"status='{stat}'", f"id='{id}'")
        return self.db.update('posts', f"status='{stat}'", f"id='{data}'")

# dmodv
