import os
from base64 import b64encode as b64e

path = os.listdir('/home/dmodv/Изображения/Снимки экрана')[3:5]
outp = ' '
for i in path:
    with open('/home/dmodv/Изображения/Снимки экрана/'+i, 'rb') as f:
        data = b64e(f.read())
    outp += data.decode() + ' '

with open('static/outp.txt', 'wb') as f:
    f.write(data)