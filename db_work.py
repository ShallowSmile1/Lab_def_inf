import numpy
import pandas
import pandas as pd
from cryptography.fernet import Fernet
import base64


def create_df(key):
    f = Fernet(key)
    with open('database.txt', 'rb') as file:
        file_b = file.read()
        file_b = f.decrypt(file_b)
        file_b = file_b.decode()
        list_df = [[j for j in i.split()] for i in file_b.split('\n')]
    df = pd.DataFrame(list_df, columns=['login', 'password', 'limit', 'block', 'first_ent'])
    print(df)
    return df


def find_user(df, login):
    user = df[df['login'] == login]
    if user.shape[0] == 1:
        return user
    else:
        raise NameError('пользователь не найден')


def get_user_by_num(df: pd.DataFrame, num):
    return df.iloc[num]


def add_user(df, key, login, password):
    f = Fernet(key)
    new_user = pd.DataFrame([[login, password, '0', '0', '1']],
                            columns=['login', 'password', 'limit', 'block', 'first_ent'])
    df = pd.concat([df, new_user], ignore_index=True)
    strin = f'\n{login} {password} 0 0 1'
    strin = strin.encode('utf-8')
    strin = f.encrypt(strin)
    with open('database.txt', 'wb') as file:
        file.write(strin)
    return df


def change(df, key, login, password=None, limit=None, block=None):
    import os

    f = Fernet(key)
    new_line = login
    user = find_user(df, login)
    if password:
        df.loc[(df.login == login), 'password'] = password
        new_line = new_line + " " + password
    else:
        new_line = new_line + " " + user['password'].values[0]
    if limit:
        df.loc[(df.login == login), 'limit'] = limit
        new_line = new_line + " " + limit
    else:
        new_line = new_line + " " + user['limit'].values[0]
    if block:
        df.loc[(df.login == login), 'block'] = block
        new_line = new_line + " " + block
    else:
        new_line = new_line + " " + user['block'].values[0]

    df.loc[(df.login == login), 'first_ent'] = '0'
    new_line = new_line + " " + '0\n'
    new_line = f.encrypt(new_line.encode('utf-8'))

    with open('database.txt', 'rb') as file_in, open('database_out.txt', 'wb') as file_out:
        text = file_in.read()
        text = f.decrypt(text)
        text = text.decode()
        for line in text.split('\n'):
            if not(line.startswith(login + ' ')):
                line = f.encrypt(line.encode('utf-8'))
                file_out.write(line)
            else:
                file_out.write(new_line)
    os.remove('database.txt')
    os.rename('database_out.txt', 'database.txt')
    return df


def create_base(key):
    try:
        open('database.txt', 'rb')
    except FileNotFoundError:
        with open('database.txt', 'wb') as file:
            f = Fernet(key)
            strin = b'ADMIN ADMIN 0 0 0'
            strin = f.encrypt(strin)
            file.write(strin)
    finally:
        db_df = create_df(key)
    return db_df


def check_pass(password: str):
    alpha = False
    digit = False
    for char in password:
        if char.isalpha():
            alpha = True
        if char.isdigit():
            digit = True
        if alpha and digit:
            return True
    return False


def get_base64(my_str):
    while len(my_str) < 32:
        my_str += b'a'
    return base64.b64encode(my_str[:32])