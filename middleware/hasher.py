import hashlib


def hash_password(password):
    hash_object = hashlib.sha1(password.encode())
    hash = hash_object.hexdigest()
    return hash


def check_password(hashed_password, user_password):
    return hashed_password == hash_password(user_password)