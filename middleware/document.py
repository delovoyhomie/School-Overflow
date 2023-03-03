from base64 import b64encode 
from base64 import b64decode
from random import choice


def generate_name_files(len_token=20):
    GEN_CONST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(len(GEN_CONST))
    new_token = ""
    for _ in range(len_token):
        new_token += choice(GEN_CONST)
    return new_token

def save_document(user: str, text: str):
    try:
        names = []
        text = text.split(' ')
        doc = [b64decode(i.encode()) for i in text]
        for i in doc:
            name = f"{user}_{generate_name_files()}"
            with open(f"static/{name}.jpg", 'wb') as file:
                file.write(i)
            names.append(name)
        names = ' '.join(names)
        return names
    except:
        return 0
        
    
if __name__ == '__main__':
    with open('README.md', 'rb') as file:
        data = file.read()
    data = b64encode(data).decode()
    data = data+' '+data+' '+data+' '+data
    print(data)
    save_document('5', data)