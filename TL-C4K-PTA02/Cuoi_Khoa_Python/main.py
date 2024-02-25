import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QMainWindow, QApplication, QWidget, QMessageBox, QPushButton
from PyQt6 import uic


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        
        self.HocSinh_btn.clicked.connect(self.Login_hs)
        self.GiaoVien_btn.clicked.connect(self.Login_tc)
        self.Register_btn.clicked.connect(self.regis)
        
        # Lưu trữ các giao diện con
        self.teacher_login = None
        self.student_login = None
        self.register = None
        self.teacher_main = None
        self.student_main = None
        self.renewpass = None
        
        
        
        
    # Phần của giáo viên
    def Login_tc(self):
        if not self.teacher_login:
            self.teacher_login = uic.loadUi("gui/login-teacher.ui")
            self.teacher_login.GiaoVienLogin_btn.clicked.connect(self.GiaoVienClicked)
            self.teacher_login.goback_tc_btn.clicked.connect(self.goback_tc_Clicked)
            self.teacher_login.forgo_pass_tc.clicked.connect(self.renew)

        self.teacher_login.show()
        self.hide()

    def GiaoVienClicked(self):
        if not self.teacher_main:
            self.teacher_main = uic.loadUi("gui/main-tc.ui")
        
        self.teacher_main.show()
        self.hide()
        
    def goback_tc_Clicked(self):
        self.teacher_login.hide()
        self.show()




    # Phần của học sinh
    def Login_hs(self):
        if not self.student_login:
            self.student_login = uic.loadUi("gui/login-student.ui")
            self.student_login.HocSinhLogin_btn.clicked.connect(self.HocSinhClicked)
            self.student_login.goback_hs_btn.clicked.connect(self.goback_hs_Clicked)
            self.student_login.forgo_pass_hs.clicked.connect(self.renew)

        self.student_login.show()
        self.hide()

    def HocSinhClicked(self):
        if not self.student_main:
            self.student_main = uic.loadUi("gui/main-st.ui")
        
        self.student_main.show()
        self.hide()
        
    def goback_hs_Clicked(self):
        self.student_login.hide()
        self.show()


    def renew(self):
        if not self.renewpass:
            self.renewpass = uic.loadUi("gui/renewpass.ui")
            
        self.renewpass.show()
        self.hide

    # Phần đăng ký
    def regis(self):
        if not self.register:
            self.register = uic.loadUi("gui/register.ui")
            self.register.register_btn.clicked.connect(self.menu_return)
            self.register.goback_reg.clicked.connect(self.menu_return)
        
        self.register.show()
        self.hide()
        
    
        
        
        
    def menu_return(self):
        self.register.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
