from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from Ui_classes.Auth import Login
import db_work as db


class Crypto(QDialog):
    def __init__(self):
        super(Crypto, self).__init__()
        loadUi("UI/crypto.ui", self)
        self.ok_button.clicked.connect(self.ok_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.key.setEchoMode(QtWidgets.QLineEdit.Password)

    def ok_func(self):
        key = self.key.text().encode("utf-8")
        self.key.setText("")
        try:
            if key == b'':
                raise Exception()
            key = db.get_base64(key)
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Incorrect token', QMessageBox.Ok)
            self.close()
        db_df = db.create_base(key)
        self.log_win = Login(db_df, key)
        self.log_win.show()
        self.close()

    def cancel_func(self):
        self.close()
