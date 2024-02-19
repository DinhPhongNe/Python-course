import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QPushButton
from PyQt6 import uic


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        
        self.HocSinh_btn.clicked.connect(self.Login_hs)
        self.GiaoVien_btn.clicked.connect(self.Login_tc)
        
        
    #==--Phần của giáo viên--==
    #Login của giáo viên
    def Login_tc(self):
        uic.loadUi("gui/login-teacher.ui", self)
        self.GiaoVienLogin_btn.clicked.connect(self.GiaoVienClicked)

    def GiaoVienClicked(self):
        uic.loadUi("gui/main-tc.ui", self)
    
    
    
    #==--Phần của học sinh--== 
    #Login của học sinh
    def Login_hs(self):
        uic.loadUi("gui/login-student.ui", self)
        self.HocSinhLogin_btn.clicked.connect(self.HocSinhClicked) 
        
    def HocSinhClicked(self):
        uic.loadUi("gui/main-st.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())