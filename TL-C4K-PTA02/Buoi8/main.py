import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import uic


class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("gi.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())