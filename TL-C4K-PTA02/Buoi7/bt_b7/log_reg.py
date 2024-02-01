import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic


class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Login")
        uic.loadUi("log.ui", self)
        
        # thầy ơi do là bài tập ở trường nhiều nên con chỉ mới làm đến đây thui mà đến hạn mất tiêu ròi:")
        btn = QPushButton()
        
        btn.setCheckable(True)
        btn.clicked.connect(self.display_message)

        
    def display_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Lỗi")
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
        msg_box.setStyleSheet("background-color:#F8F2EC; color: #356a9c")
        msg_box.exec()
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())