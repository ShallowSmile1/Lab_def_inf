from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from Ui_classes import Main_window


class AddNewUser(QDialog):
    def __init__(self):
        super(AddNewUser, self).__init__()
        loadUi("UI/add_user.ui", self)
        self.ok_button.clicked.connect(self.ok_func)
        self.cancel_button.clicked.connect(self.cancel_func)

    def ok_func(self):
        login = self.login.text()
        password = self.password.text()

    def cancel_func(self):
        self.main_window = Main_window()
        self.main_window.show()
        self.close()


