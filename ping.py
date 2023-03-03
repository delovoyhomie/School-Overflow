if __name__ == '__main__':
    data = {'login':'test', 'passw':'lol'}
    import requests
    print(requests.post('http://127.0.0.1:2023/posts', data = data).json())
