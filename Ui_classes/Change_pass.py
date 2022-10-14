from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class ChangePassword(QDialog):
    def __init__(self):
        super(ChangePassword, self).__init__()
        loadUi("UI/Change_pass.ui", self)
        self.change_button.clicked.connect(self.change_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)

    def auth_func(self):
        password = self.password.text()
        confirm = self.confirm.text()
        print(f"pass: {password}, confirm: {confirm}")

    def change_func(self):
        pass

    def cancel_func(self):
        pass
