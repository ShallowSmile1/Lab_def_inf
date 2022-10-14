from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from Ui_classes import Main_window


class UserList(QDialog):
    def __init__(self):
        super(UserList, self).__init__()
        loadUi("UI/user_list.ui", self)
        self.ok_button.clicked.connect(self.ok_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.next_button.clicked.connect(self.next_func)
        self.save_button.clicked.connect(self.save_func)
        self.prev_button.clicked.connect(self.prev_func)

    def prev_func(self):
        pass

    def ok_func(self):
        pass

    def cancel_func(self):
        pass

    def next_func(self):
        pass

    def save_func(self):
        username = self.username.text()
        block = self.block.isChecked()
        limit = self.limit.isChecked()
        pass