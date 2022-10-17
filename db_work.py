import numpy
import pandas
import pandas as pd


def create_df():
    with open('database.txt', 'r', encoding='utf-8') as file:
        list_df = [[j for j in i.split()] for i in file]
    df = pd.DataFrame(list_df, columns=['login', 'password', 'limit', 'block', 'first_ent'])
    return df


def find_user(df, login):
    user = df[df['login'] == login]
    if user.shape[0] == 1:
        return user
    else:
        raise NameError('пользователь не найден')


def get_user_by_num(df: pd.DataFrame, num):
    return df.iloc[num]


def add_user(df, login, password):
    new_user = pd.DataFrame([[login, password, '0', '0', '1']],
                            columns=['login', 'password', 'limit', 'block', 'first_ent'])
    df = pd.concat([df, new_user], ignore_index=True)
    str = f'\n{login} {password} 0 0 1'
    with open('database.txt', 'a', encoding='utf-8') as file:
        file.write(str)
    return df


def change(df, login, password=None, limit=None, block=None):
    import os

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

    with open('database.txt', encoding='utf-8') as file_in, open('database_out.txt', 'w', encoding='utf-8') as file_out:
        for line in file_in:
            if not(line.startswith(login + ' ')):
                file_out.write(line)
            else:
                file_out.write(new_line)
    os.remove('database.txt')
    os.rename('database_out.txt', 'database.txt')
    return df


def create_base():
    try:
        open('database.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        with open('database.txt', 'w', encoding='utf-8') as file:
            file.write('ADMIN ADMIN 0 0 0')
    finally:
        db_df = create_df()
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
