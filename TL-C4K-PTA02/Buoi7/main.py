import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        btn = QPushButton("press me")
        self.setCentralWidget(btn)

        btn.setCheckable(True)
        btn.clicked.connect(self.click)
        btn.clicked.connect(self.click_toggle)
        btn.clicked.connect(self.display_message)

    def click(self):
        print("button đc click nè ")

    def click_toggle(self, checked):
        print(checked)


    def display_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Lỗi")
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
        msg_box.setStyleSheet("background-color:#F8F2EC; color: #356a9c")
        msg_box.exec()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()