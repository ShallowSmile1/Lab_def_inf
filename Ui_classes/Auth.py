from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from Ui_classes.Main_window import Window
from Ui_classes.Change_pass import ChangePassword
import db_work as db


class Login(QDialog):
    def __init__(self, db_df, key):
        super(Login, self).__init__()
        loadUi("UI/login.ui", self)
        self.auth_button.clicked.connect(self.auth_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_df = db_df
        self.key = key
        self.try_auth = 0

    def auth_func(self):
        self.try_auth += 1
        if self.try_auth != 3:
            login = self.login.text()
            password = self.password.text()
            try:
                user = db.find_user(self.db_df, login)
            except NameError:
                QMessageBox.critical(self, "Error ",
                                     f"User with that name is not exist",
                                     QMessageBox.Ok)
            finally:
                if user['block'].values[0] == '0':
                    if user['password'].values[0] == password:
                        if not(db.check_pass(password)) and user['limit'].values[0] == '1':
                            QMessageBox.critical(self, "Error",
                                                 f"Please change your password. It must have letters and digits",
                                                 QMessageBox.Ok)
                            prev_win = 'auth'
                            self.cng_pass_win = ChangePassword(self.db_df, user, prev_win, self.key)
                            self.cng_pass_win.show()
                            self.close()
                        else:
                            if user['first_ent'].values[0] == '1':
                                prev_win = 'auth'
                                self.cng_pass_win = ChangePassword(self.db_df, user, prev_win, self.key)
                                self.cng_pass_win.show()
                                self.close()
                            else:
                                self.main_win = Window(self.db_df, user, self.key)
                                self.main_win.show()
                                self.close()
                    else:
                        QMessageBox.critical(self, "Error",
                                             f"Wrong password. You have {3 - self.try_auth} more tries",
                                             QMessageBox.Ok)
                        self.password.setText("")
                else:
                    QMessageBox.critical(self, "Error",
                                         f"Your account is banned, please write to admin to know reason",
                                         QMessageBox.Ok)
                    self.close()
        else:
            QMessageBox.critical(self, "Error",
                                 f"You failed 3 times to auth. Access denied",
                                 QMessageBox.Ok)
            self.close()

    def cancel_func(self):
        self.close()
