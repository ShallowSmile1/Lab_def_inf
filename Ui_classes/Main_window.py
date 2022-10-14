from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QAction
from PyQt5.uic import loadUi
from Ui_classes.Change_pass import ChangePassword
from Ui_classes.Add_new_user import AddNewUser
from Ui_classes.User_list import UserList
import db_work as db


class Window(QtWidgets.QMainWindow):
    def __init__(self, db_df, auth_user, parent=None):
        super(Window, self).__init__(parent)
        loadUi("UI/main.ui", self)

        self.db_df = db_df
        self.user = auth_user
        print(self.user)
        print(self.user['login'].values[0])
        self.label_user.setText(self.user['login'].values[0])
        if self.user['login'].values[0] != 'admin':
            self.actionNew_User.setVisible(False)
            self.actionAll_User.setVisible(False)
        self.actionChangePass.triggered.connect(self.change_pass)
        self.actionNew_User.triggered.connect(self.new_user)
        self.actionAll_Users.triggered.connect(self.all_users)
        self.actionExit.triggered.connect(self.close)
        self.actionPassReq.triggered.connect(self.help)

    def change_pass(self):
        self.cng_pass_win = ChangePassword()
        self.cng_pass_win.show()
        self.close()

    def new_user(self):
        self.add_new_user_win = AddNewUser()
        self.add_new_user_win.show()
        self.close()

    def all_users(self):
        self.all_users_win = UserList()
        self.all_users_win.show()
        self.close()

    def exit(self):
        self.close()

    def help(self):
        print('1')
