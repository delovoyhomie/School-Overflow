from base64 import b64encode 
from base64 import b64decode
from random import choice
import json

def generate_name_files(len_token=20):
    GEN_CONST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    new_token = ""
    for _ in range(len_token):
        new_token += choice(GEN_CONST)
    return new_token

def save_document(user: str, text):
    # try:
    names = []
    text = text.split()
    doc = [b64decode(i.replace('\n', '').replace('\r', '').replace('\t', '')) for i in text]
    for i in doc:
        print(i)
        name = f"{user}_{generate_name_files()}"
        with open(f"/root/School-Overflow/static/{name}.jpg", 'wb') as file:
            file.write(i)
        names.append(name)
    print(names)
    names = ' '.join(names)
    return names
    # except Exception as _ex:
        # print(_ex)
    #     return 0
        
    
if __name__ == '__main__':
    import os
    current, dirs, files = os.walk('/home/dmodv/Изображения/Снимки экрана').__next__()
    dt = ''
    
    with open('/home/dmodv/Изображения/Снимки экрана/'+files[0], 'rb') as file:
        data = file.read()
    dt += b64encode(data).decode()
    with open(f"static/t.txt", 'w') as file:
        file.write(dt)
    print(dt)
