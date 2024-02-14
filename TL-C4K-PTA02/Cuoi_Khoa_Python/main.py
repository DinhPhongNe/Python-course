import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt6 import uic


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        
        self.HocSinh_btn.clicked.connect(self.Login_hs)
        self.GiaoVien_btn.clicked.connect(self.Login_tc)
        
    def Login_hs(self):
        uic.loadUi("gui/login-student.ui", self)
            
    def Login_tc(self):
        uic.loadUi("gui/login-teacher.ui", self)
        

class Main_ST(QMainWindow):
    pass

class Main_TC(QMainWindow):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    st_page = Main_ST()
    tc_page = Main_TC()
    
    #thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    sys.exit(app.exec())