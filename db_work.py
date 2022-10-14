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
    print(user)
    print(user['password'].values[0])
    if user.shape[0] == 1:
        print('user is found')
        return user
    else:
        raise NameError('пользователь не найден')


def check_user(cur_user):

    return 1


def add_user(df, login, password):
    new_user = pd.DataFrame([login, password, '0', '0', '1'],
                            columns=['login', 'password', 'limit', 'block', 'first_ent'])
    df = pd.concat([df, new_user], ignore_index=True)
    return df


def change(df, login, password=-1, limit=-1, block=-1, first_ent=-1):
    if password != -1:
        df.loc[(df.login == login), 'password'] = password
    if limit != -1:
        df.loc[(df.login == login), 'limit'] = limit
    if block != -1:
        df.loc[(df.login == login), 'block'] = block
    if first_ent != -1:
        df.loc[(df.login == login), 'first_ent'] = first_ent
    return df
