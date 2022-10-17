from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import db_work as db


class ChangePassword(QDialog):
    def __init__(self, db_df, user, prev_win):
        super(ChangePassword, self).__init__()
        loadUi("UI/Change_pass.ui", self)
        self.change_button.clicked.connect(self.change_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.old_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_df = db_df
        self.user = user
        self.prev_win = prev_win

    def change_func(self):
        old_password = self.old_pass.text()
        new_password = self.new_pass.text()
        confirm_password = self.confirm.text()

        if self.user['password'].values[0] == old_password:
            if new_password == confirm_password:
                if ((db.check_pass(new_password) and self.user['limit'].values[0] == '1') or
                    (self.user['limit'].values[0] == '0')):
                    db.change(self.db_df, self.user['login'].values[0], new_password)
                    if self.prev_win == 'auth':
                        from Ui_classes.Auth import Login
                        self.log_win = Login(self.db_df)
                        self.log_win.show()
                        self.close()
                    else:
                        from Ui_classes.Main_window import Window
                        self.main_win = Window(self.db_df, self.user)
                        self.main_win.show()
                        self.close()
                elif not(db.check_pass(new_password)) and self.user['limit'].values[0] == '1':
                    QMessageBox.critical(self, "Error",
                                         f"Please change your password. It must have letters and digits",
                                         QMessageBox.Ok)
                    self.confirm.setText("")
                    self.old_pass.setText("")
                    self.new_pass.setText("")

            else:
                QMessageBox.critical(self, "Error",
                                     f"Passwords not match",
                                     QMessageBox.Ok)
                self.confirm.setText("")
                self.old_pass.setText("")
                self.new_pass.setText("")
        else:
            QMessageBox.critical(self, "Error",
                                 f"Wrong old password",
                                 QMessageBox.Ok)
            self.old_pass.setText("")
            self.new_pass.setText("")
            self.confirm.setText("")

    def cancel_func(self):
        if self.prev_win == 'auth':
            from Ui_classes.Auth import Login
            self.log_win = Login(self.db_df)
            self.log_win.show()
            self.close()
        else:
            from Ui_classes.Main_window import Window
            self.main_win = Window(self.db_df, self.user)
            self.main_win.show()
            self.close()
