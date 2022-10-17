import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Ui_classes.Auth import Login
import db_work as db


if __name__ == '__main__':
    db_df = db.create_base()
    app = QApplication(sys.argv)
    login_window = Login(db_df)
    login_window.setFixedWidth(640)
    login_window.setFixedHeight(420)
    login_window.show()
    sys.exit(app.exec())

