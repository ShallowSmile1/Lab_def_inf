from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi


class Window(QtWidgets.QMainWindow):
    def __init__(self, db_df, auth_user, key, parent=None):
        super(Window, self).__init__(parent)
        loadUi("UI/main.ui", self)

        self.key = key
        self.db_df = db_df
        self.user = auth_user
        self.label_user.setText(self.user['login'].values[0])
        if self.user['login'].values[0] != 'ADMIN':
            self.actionNew_User.setVisible(False)
            self.actionAll_Users.setVisible(False)
        self.actionChangePass.triggered.connect(self.change_pass)
        self.actionNew_User.triggered.connect(self.new_user)
        self.actionAll_Users.triggered.connect(self.all_users)
        self.actionExit.triggered.connect(self.close)
        self.actionPassReq.triggered.connect(self.help)

    def change_pass(self):
        from Ui_classes.Change_pass import ChangePassword
        prev_win = 'main'
        self.cng_pass_win = ChangePassword(self.db_df, self.user, prev_win, self.key)
        self.cng_pass_win.show()
        self.close()

    def new_user(self):
        from Ui_classes.Add_new_user import AddNewUser
        self.add_new_user_win = AddNewUser(self.db_df, self.user, self.key)
        self.add_new_user_win.show()
        self.close()

    def all_users(self):
        from Ui_classes.User_list import UserList
        self.all_users_win = UserList(self.db_df, self.user, self.key)
        self.all_users_win.show()
        self.close()

    def exit(self):
        self.close()

    def help(self):
        QMessageBox.information(self, "Info",
                             f"Variation 3:\nHaving letters and digits",
                             QMessageBox.Ok)
