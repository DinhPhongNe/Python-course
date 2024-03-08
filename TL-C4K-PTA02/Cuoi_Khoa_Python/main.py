import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit
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
        self.btvn_upload = None

        # Thiết lập hộp thoại thông báo lỗi
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Lỗi")
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")

    # Phần của giáo viên
    def Login_tc(self):
        if not self.teacher_login:
            self.teacher_login = uic.loadUi("gui/login-teacher.ui")
            # Assign PhoneTC and PassTC
            self.PhoneTC = self.teacher_login.findChild(QLineEdit, "PhoneTC")
            self.PassTC = self.teacher_login.findChild(QLineEdit, "PassTC")
            self.teacher_login.GiaoVienLogin_btn.clicked.connect(self.check_login)
            self.teacher_login.goback_tc_btn.clicked.connect(self.goback_tc_Clicked)
            self.teacher_login.forgo_pass_tc.clicked.connect(self.renew)

        self.teacher_login.show()
        self.hide()

    def check_login(self):
        Phone = self.PhoneTC.text()
        password = self.PassTC.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        
        # Check credentials
        if Phone == "1234567890" and password == "admin":
            self.close()
            self.GiaoVienClicked()
        else:
            self.msg_box.setText("Số điện thoại hoặc mật khẩu sai")
            self.msg_box.exec()
            
        
    def GiaoVienClicked(self):
        if not self.teacher_main:
            self.teacher_main = uic.loadUi("gui/main-tc.ui")
            self.teacher_main.btvn_upload.clicked.connect(self.upload_btvn)
            self.teacher_main.logOut_btn_tc.clicked.connect(self.GiaoVienMain_Return)
        
        self.teacher_main.show()
        self.teacher_login.hide()
        
    def upload_btvn(self):
        if not self.teacher_main:
            self.teacher_main = uic.loadUi("gui/btvn-upload.ui")
            self.teacher_main.show()
        else:
            self.teacher_main.show()
        
    def GiaoVienMain_Return(self):
        self.teacher_login.show()
        self.teacher_main.hide()
        
    def goback_tc_Clicked(self):
        self.teacher_login.hide()
        self.show()

    # Phần của học sinh
    def Login_hs(self):
        if not self.student_login:
            self.student_login = uic.loadUi("gui/login-student.ui")
            self.Phone_HS = self.student_login.findChild(QLineEdit, "Phone_HS")
            self.pass_HS = self.student_login.findChild(QLineEdit, "pass_HS")
            self.student_login.HocSinhLogin_btn.clicked.connect(self.check_login_hs)
            self.student_login.goback_hs_btn.clicked.connect(self.goback_hs_Clicked)
            self.student_login.forgo_pass_hs.clicked.connect(self.renew)

        self.student_login.show()
        self.hide()
        
    def check_login_hs(self):
        Phone = self.Phone_HS.text()
        password = self.pass_HS.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        
        # Check credentials
        if Phone == "1234567890" and password == "admin":
            self.close()
            self.HocSinhClicked()
        else:
            self.msg_box.setText("Số điện thoại hoặc mật khẩu sai")
            self.msg_box.exec()

    def HocSinhClicked(self):
        if not self.student_main:
            self.student_main = uic.loadUi("gui/main-st.ui")
            self.student_main.logOut_btn_hs.clicked.connect(self.HocSinhMain_Return)
        
        self.student_main.show()
        self.student_login.hide()
        
    def HocSinhMain_Return(self):
        self.student_login.show()
        self.student_main.hide()
        
    def goback_hs_Clicked(self):
        self.student_login.hide()
        self.show()

    #Phần renew pass
    def renew(self):
        if not self.renewpass:
            self.renewpass = uic.loadUi("gui/renewpass.ui")
            self.renewpass.reNew_btn.clicked.connect(self.renewClicked)
            
        self.renewpass.show()
        
    def renewClicked(self):
        self.newpass_Phone = self.renewpass.findChild(QLineEdit, "newpass_Phone")
        self.renewpass_newpass = self.renewpass.findChild(QLineEdit, "renewpass_newpass")
        self.reTypeNewPass = self.renewpass.findChild(QLineEdit, "reTypeNewPass")
            
        newpass_Phone = self.newpass_Phone.text()
        newpass = self.renewpass_newpass.text()
        retypepass = self.reTypeNewPass.text()
        
        if not newpass_Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not newpass:
            self.msg_box.setText("vui lòng nhập mật khẩu mới!")
            self.msg_box.exec()
            return
        if not retypepass:
            self.msg_box.setText("vui lòng nhập lại mật khẩu mới!")
            self.msg_box.exec()
            
            
        # Ẩn tất cả các giao diện cũ trước khi quay lại menu
        if self.teacher_login:
            self.teacher_login.hide()
        if self.student_login:
            self.student_login.hide()
        if self.register:
            self.register.hide()
        if self.teacher_main:
            self.teacher_main.hide()
        if self.student_main:
            self.student_main.hide()
        if self.renewpass:
            self.renewpass.hide()

        self.menu_return()

        # Hiển thị thông báo cần đăng nhập lại
        self.msg_box.setText("Mật khẩu đã được thay đổi")
        self.msg_box.exec()
        
        self.msg_box.setText("Vui lòng đăng nhập lại.")
        self.msg_box.exec()

    # Phần đăng ký
    def regis(self):
        if not self.register:
            self.register = uic.loadUi("gui/register.ui")
            self.register.register_btn.clicked.connect(self.regis_check)
            self.register.goback_reg.clicked.connect(self.menu_return)

        self.register.show()
        self.hide()

    def regis_check(self):
        self.Phone_reg = self.register.findChild(QLineEdit, "Phone_reg")
        self.pass_reg = self.register.findChild(QLineEdit, "pass_reg")
        self.re_pass_reg = self.register.findChild(QLineEdit, "re_pass_reg")
            
        Phone_reg = self.Phone_reg.text()
        pass_reg = self.pass_reg.text()
        re_pass_reg = self.re_pass_reg.text()
    
        if not Phone_reg:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not pass_reg:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        if not re_pass_reg:
            self.msg_box.setText("vui lòng nhập lại mật khẩu!")
            self.msg_box.exec()
            return


        self.msg_box.setText("đã tạo tài khoản mới")
        self.msg_box.exec()

        self.msg_box.setText("Vui lòng đăng nhập vào tài khoản mới của bạn.")
        self.msg_box.exec()
        self.register.hide()
        self.show()

    def menu_return(self):
        if self.register:
            self.register.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    
    app.exec()
