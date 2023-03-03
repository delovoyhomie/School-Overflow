if __name__ == '__main__':
    import requests
    print(requests.get('http://127.0.0.1:2023', data = {'Tony':'IamIronMan'}).content)
