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
        self.Register_btn.clicked.connect(self.regis)
        
        
    #==--Phần của giáo viên--==
    #Login của giáo viên
    def Login_tc(self):
        uic.loadUi("gui/login-teacher.ui", self)
        self.GiaoVienLogin_btn.clicked.connect(self.GiaoVienClicked)
        self.goback_tc_btn.clicked.connect(self.goback_tc_Clicked)

    def GiaoVienClicked(self):
        uic.loadUi("gui/main-tc.ui", self)
        
    def goback_tc_Clicked(self):
        uic.loadUi("gui/menu.ui",self)
        

    
    
    
    #==--Phần của học sinh--== 
    #Login của học sinh
    def Login_hs(self):
        uic.loadUi("gui/login-student.ui", self)
        self.HocSinhLogin_btn.clicked.connect(self.HocSinhClicked) 
        self.goback_hs_btn.clicked.connect(self.goback_hs_Clicked)
        
    def HocSinhClicked(self):
        uic.loadUi("gui/main-st.ui", self)
        
    def goback_hs_Clicked(self):
        uic.loadUi("gui/menu.ui",self)
        
        
        
        
    #==--Phần của Đăng ký--== 
    def regis(self):
        uic.loadUi("gui/register.ui", self)
        self.register_btn.clicked.connect(self.menu_return)
        
    def menu_return(self):
        uic.loadUi("gui/menu.ui",self)
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())