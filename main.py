import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Ui_classes.Auth import Login
import pandas as pd
import numpy as np
import db_work as db


if __name__ == '__main__':
    try:
        with open('database.txt', 'r', encoding='utf-8') as file:
            db_text = file.read()
    except FileNotFoundError:
        with open('database.txt', 'w', encoding='utf-8') as file:
            file.write('admin abs1 0 0 0')
    finally:
        db_df = db.create_df()
        print(db_df)
        with open('database.txt', 'r', encoding='utf-8') as file:
            db_text = file.read()

    app = QApplication(sys.argv)
    login_window = Login(db_df)
    login_window.setFixedWidth(640)
    login_window.setFixedHeight(420)
    login_window.show()
    sys.exit(app.exec())

