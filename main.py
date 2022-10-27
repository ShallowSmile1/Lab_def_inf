import sys
from PyQt5.QtWidgets import QApplication
from Ui_classes.Crypto import Crypto


if __name__ == '__main__':
    app = QApplication(sys.argv)
    crypto_window = Crypto()
    crypto_window.setFixedWidth(640)
    crypto_window.setFixedHeight(420)
    crypto_window.show()
    sys.exit(app.exec())
