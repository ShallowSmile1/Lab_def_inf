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
    return df


def find_user(df, login):
    user = df[df['login'] == login]
    if user.shape[0] == 1:
        return user
    else:
        raise NameError()


def get_user_by_num(df: pd.DataFrame, num):
    return df.iloc[num]


def add_user(df, key, login, password):
    import os
    f = Fernet(key)
    new_user = pd.DataFrame([[login, password, '0', '0', '1']],
                            columns=['login', 'password', 'limit', 'block', 'first_ent'])
    df = pd.concat([df, new_user], ignore_index=True)
    strin = f'\n{login} {password} 0 0 1'
    with open('database.txt', 'rb') as file:
        db = file.read()
    db = f.decrypt(db)
    db = db.decode()
    strin = db + strin
    strin = strin.encode('utf-8')
    strin = f.encrypt(strin)
    with open('database_out.txt', 'wb') as file:
        file.write(strin)
    os.remove('database.txt')
    os.rename('database_out.txt', 'database.txt')
    return df


def change(df, key, login, password=None, limit=None, block=None, first_ent=None):
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
    if first_ent:
        df.loc[(df.login == login), 'first_ent'] = first_ent
        new_line = new_line + " " + first_ent
    else:
        new_line = new_line + " " + user['first_ent'].values[0]

    with open('database.txt', 'rb') as file_in, open('database_out.txt', 'wb') as file_out:
        text = file_in.read()
        text = f.decrypt(text)
        text = text.decode()
        new_text = ''
        for i, line in enumerate(text.split('\n')):
            if i != 0:
                new_text = new_text + "\n"
            if not(line.startswith(login + ' ')):
                new_text = new_text + line
            else:
                new_text = new_text + new_line
        new_text = new_text.encode('utf-8')
        new_text = f.encrypt(new_text)
        file_out.write(new_text)
    os.remove('database.txt')
    os.rename('database_out.txt', 'database.txt')
    return df


def create_base(key):
    try:
        open('database.txt', 'rb')
    except FileNotFoundError:
        with open('database.txt', 'wb') as file:
            f = Fernet(key)
            strin = b'ADMIN ADMIN 0 0 1'
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