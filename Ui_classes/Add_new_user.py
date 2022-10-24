from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import db_work as db


class AddNewUser(QDialog):
    def __init__(self, db_df, user, key):
        super(AddNewUser, self).__init__()
        loadUi("UI/add_user.ui", self)
        self.ok_button.clicked.connect(self.ok_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_df = db_df
        self.key = key
        self.user = user

    def ok_func(self):
        from Ui_classes.Main_window import Window
        login = self.username.text()
        password = self.password.text()
        self.db_df = db.add_user(self.db_df, self.key, login, password)
        self.main_window = Window(self.db_df, self.user, self.key)
        self.main_window.show()
        self.close()

    def cancel_func(self):
        from Ui_classes.Main_window import Window
        self.main_window = Window(self.db_df, self.user, self.key)
        self.main_window.show()
        self.close()
