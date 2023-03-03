from base64 import b64encode 
from base64 import b64decode 

def save_document(text: str):
    text = text.split('^$&')
    doc = [b64decode(i.encode()) for i in text]
    print(doc)
if __name__ == '__main__':
    with open('README.md', 'r') as file:
        data = file.read()
    data = b64encode(data).decode()
    print(data)
    data = data+'^$&'+data+'^$&'+data+'^$&'+data
    save_document(data)