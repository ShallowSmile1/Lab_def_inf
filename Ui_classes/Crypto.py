from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from Ui_classes.Main_window import Window
from Ui_classes.Change_pass import ChangePassword
import db_work as db


class Crypto(QDialog):
    def __init__(self, db_df):
        super(Crypto, self).__init__()
        loadUi("UI/login.ui", self)
        self.ok_button.clicked.connect(self.auth_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.db_df = db_df

    def ok_func(self):
        pass

    def cancel_func(self):
        pass
