from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from Ui_classes.Main_window import Window
import db_work as db


class Login(QDialog):
    def __init__(self, db_df):
        super(Login, self).__init__()
        loadUi("UI/login.ui", self)
        self.auth_button.clicked.connect(self.auth_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_df = db_df
        self.try_auth = 0

    def auth_func(self):
        self.try_auth += 1
        print(1)
        if self.try_auth != 3:
            login = self.login.text()
            password = self.password.text()
            try:
                user = db.find_user(self.db_df, login)
            except NameError:
                print('пользователь не зарегистрирован')
            finally:
                if user['password'].values[0] == password:
                    print('enter....')
                    self.main_win = Window(self.db_df, user)
                    self.main_win.show()
                    self.close()
                else:
                    print('неверный пароль')
        else:
            print('исчерпан лимит входов')

    def cancel_func(self):
        self.close()
