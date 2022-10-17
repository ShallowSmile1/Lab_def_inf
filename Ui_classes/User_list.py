import pandas
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import pandas as pd
import db_work as db


class UserList(QDialog):
    def __init__(self, db_df: pd.DataFrame, user):
        super(UserList, self).__init__()
        loadUi("UI/user_list.ui", self)
        self.ok_button.clicked.connect(self.ok_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.next_button.clicked.connect(self.next_func)
        self.save_button.clicked.connect(self.save_func)
        self.prev_button.clicked.connect(self.prev_func)
        self.username.setEnabled(False)
        self.db_df = db_df
        self.user = user
        self.cur_num = 1
        self.total_users = len(self.db_df.columns) + 1
        print(self.total_users)
        self.cur_user_at_list = db.get_user_by_num(self.db_df, self.cur_num % self.total_users)
        self.set_params()

    def set_params(self):
        block = True if self.cur_user_at_list['block'] == '1' else False
        limit = True if self.cur_user_at_list['limit'] == '1' else False
        login = self.cur_user_at_list['login']
        self.block.setChecked(block)
        self.limit.setChecked(limit)
        self.username.setText(login)

    def prev_func(self):
        self.cur_num -= 1
        if self.cur_num % self.total_users == 0:
            self.cur_num -= 1
        self.cur_user_at_list = db.get_user_by_num(self.db_df, self.cur_num % self.total_users)
        self.set_params()

    def next_func(self):
        self.cur_num += 1
        if self.cur_num % self.total_users == 0:
            self.cur_num += 1
        self.cur_user_at_list = db.get_user_by_num(self.db_df, self.cur_num % self.total_users)
        self.set_params()

    def ok_func(self):
        from Ui_classes.Main_window import Window
        self.main_window = Window(self.db_df, self.user)
        self.main_window.show()
        self.close()

    def cancel_func(self):
        from Ui_classes.Main_window import Window
        self.main_window = Window(self.db_df, self.user)
        self.main_window.show()
        self.close()

    def save_func(self):
        username = self.username.text()
        block = str(int(self.block.isChecked()))
        limit = str(int(self.limit.isChecked()))
        db.change(self.db_df, username, limit=limit, block=block)
        print(self.db_df)
