import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6 import uic
import random
import json

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("gui/menu.ui", self)
        self.phone_validator = QIntValidator()
        self.phone_validator.setBottom(0)
        self.phone_validator.setTop(999999999)
        self.HocSinh_btn.clicked.connect(self.Login_hs)
        self.GiaoVien_btn.clicked.connect(self.Login_tc)
        self.Register_btn.clicked.connect(self.regis)
        self.quit_btn.clicked.connect(self.quit)
        
        self.teacher_login = None
        self.student_login = None
        self.register = None
        self.teacher_main = None
        self.student_main = None
        self.renewpass = None
        self.btvn_upload = None

        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Lỗi")
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
        
    def quit(self):
        window.close()

    def Login_tc(self):
        if not self.teacher_login:
            self.teacher_login = uic.loadUi("gui/login-teacher.ui")
            self.PhoneTC = self.teacher_login.findChild(QLineEdit, "PhoneTC")
            self.PhoneTC.setValidator(self.phone_validator)
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
            
        phone_number = self.PhoneTC.text()
        if len(phone_number) != 10 or not phone_number.startswith('0'):
            self.msg_box.setText("Số điện thoại không hợp lệ!")
            self.msg_box.exec()
            return
        
        if Phone == "0987654321" and password == "admin":
            self.close()
            self.GiaoVienClicked()
        else:
            self.msg_box.setText("Số điện thoại hoặc mật khẩu sai")
            self.msg_box.exec()
            
        
    def GiaoVienClicked(self):
        if not self.teacher_main:
            self.teacher_main = uic.loadUi("gui/main-tc.ui")
            self.teacher_main.logOut_btn_tc.clicked.connect(self.GiaoVienMain_Return)
            
            self.teacher_main.add_btn.clicked.connect(self.add_information)
            self.teacher_main.update_btn.clicked.connect(self.update_information)
            self.teacher_main.delete_btn.clicked.connect(self.delete_information)
            self.teacher_main.search_btn.clicked.connect(self.search)
            self.teacher_main.clear_btn.clicked.connect(self.clear_information)
            self.teacher_main.btvn_upload_btn.clicked.connect(self.upload_btvn)
            
            self.table = self.teacher_main.findChild(QTableWidget, "student_Infor_table")
            self.search_bar = self.teacher_main.findChild(QLineEdit, "Search_bar")
            self.stt = self.teacher_main.findChild(QLineEdit, "so_thu_tu")
            self.ho = self.teacher_main.findChild(QLineEdit, "ho")
            self.ten = self.teacher_main.findChild(QLineEdit, "ten")
            self.toan = self.teacher_main.findChild(QLineEdit, "diem_toan")
            self.van = self.teacher_main.findChild(QLineEdit, "diem_van")
            self.anh = self.teacher_main.findChild(QLineEdit, "diem_anh")
            self.ly = self.teacher_main.findChild(QLineEdit, "diem_ly")
            self.hoa = self.teacher_main.findChild(QLineEdit, "diem_hoa")
            self.sinh = self.teacher_main.findChild(QLineEdit, "diem_sinh")
            self.dia = self.teacher_main.findChild(QLineEdit, "diem_dia")
            self.su = self.teacher_main.findChild(QLineEdit, "diem_su")
            self.diemTB = self.teacher_main.findChild(QLineEdit, "diem_tb")
            self.hoc_luc = self.teacher_main.findChild(QLineEdit, "hoc_luc")
            self.hanh_kiem = self.teacher_main.findChild(QLineEdit, "hanh_kiem")

        self.teacher_main.show()
        self.teacher_login.hide()

    def search(self):
        text = self.search_bar.text().strip().lower()
        for row in range(self.table.rowCount()):
            match = False
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item and text in item.text().strip().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

                
    def add_information(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

        self.table.setItem(rowPosition, 0, QTableWidgetItem(self.stt.text()))
        self.table.setItem(rowPosition, 1, QTableWidgetItem(self.ho.text()))
        self.table.setItem(rowPosition, 2, QTableWidgetItem(self.ten.text()))
        self.table.setItem(rowPosition, 3, QTableWidgetItem(self.toan.text()))
        self.table.setItem(rowPosition, 4, QTableWidgetItem(self.van.text()))
        self.table.setItem(rowPosition, 5, QTableWidgetItem(self.anh.text()))
        self.table.setItem(rowPosition, 6, QTableWidgetItem(self.ly.text()))
        self.table.setItem(rowPosition, 7, QTableWidgetItem(self.hoa.text()))
        self.table.setItem(rowPosition, 8, QTableWidgetItem(self.sinh.text()))
        self.table.setItem(rowPosition, 9, QTableWidgetItem(self.dia.text()))
        self.table.setItem(rowPosition, 10, QTableWidgetItem(self.su.text()))
        self.table.setItem(rowPosition, 11, QTableWidgetItem(self.diemTB.text()))
        self.table.setItem(rowPosition, 12, QTableWidgetItem(self.hoc_luc.text()))
        self.table.setItem(rowPosition, 13, QTableWidgetItem(self.hanh_kiem.text()))

    def select_information(self):
        current_row = self.table.currentRow()
        self.stt.setText(self.table.item(current_row, 0).text())
        self.ho.setText(self.table.item(current_row, 1).text())
        self.ten.setText(self.table.item(current_row, 2).text())
        self.toan.setText(self.table.item(current_row, 3).text())
        self.van.setText(self.table.item(current_row, 4).text())
        self.anh.setText(self.table.item(current_row, 5).text())
        self.ly.setText(self.table.item(current_row, 6).text())
        self.hoa.setText(self.table.item(current_row, 7).text())
        self.sinh.setText(self.table.item(current_row, 8).text())
        self.dia.setText(self.table.item(current_row, 9).text())
        self.su.setText(self.table.item(current_row, 10).text())
        self.diemTB.setText(self.table.item(current_row, 11).text())
        self.hoc_luc.setText(self.table.item(current_row, 12).text())
        self.hanh_kiem.setText(self.table.item(current_row, 13).text())

    def update_information(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            self.msg_box.setText("Please select a row to update.")
            self.msg_box.exec()
            return

        self.table.setItem(current_row, 0, QTableWidgetItem(self.stt.text()))
        self.table.setItem(current_row, 1, QTableWidgetItem(self.ho.text()))
        self.table.setItem(current_row, 2, QTableWidgetItem(self.ten.text()))
        self.table.setItem(current_row, 3, QTableWidgetItem(self.toan.text()))
        self.table.setItem(current_row, 4, QTableWidgetItem(self.van.text()))
        self.table.setItem(current_row, 5, QTableWidgetItem(self.anh.text()))
        self.table.setItem(current_row, 6, QTableWidgetItem(self.ly.text()))
        self.table.setItem(current_row, 7, QTableWidgetItem(self.hoa.text()))
        self.table.setItem(current_row, 8, QTableWidgetItem(self.sinh.text()))
        self.table.setItem(current_row, 9, QTableWidgetItem(self.dia.text()))
        self.table.setItem(current_row, 10, QTableWidgetItem(self.su.text()))
        self.table.setItem(current_row, 11, QTableWidgetItem(self.diemTB.text()))
        self.table.setItem(current_row, 12, QTableWidgetItem(self.hoc_luc.text()))
        self.table.setItem(current_row, 13, QTableWidgetItem(self.hanh_kiem.text()))

    def clear_information(self):
        self.msg_box.setText("Hệ thống đang thông báo đến hiệu trưởng. Đang chờ hiệu trưởng đồng ý hoặc không đồng ý.")
        self.msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msg_box.exec()

        # Random đồng ý hoặc không đồng ý
        approval = random.choice(["Đồng ý", "Không đồng ý"])

        if approval == "Đồng ý":
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("hiệu trưởng đã đồng ý. Toàn học sinh sẽ biến mất.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.exec()
            self._clear_all_fields()
        else:
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("hiệu trưởng không đã đồng ý.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.exec()

    def _clear_all_fields(self):
        self.stt.clear()
        self.ho.clear()
        self.ten.clear()
        self.toan.clear()
        self.van.clear()
        self.anh.clear()
        self.ly.clear()
        self.hoa.clear()
        self.sinh.clear()
        self.dia.clear()
        self.su.clear()
        self.diemTB.clear()
        self.hoc_luc.clear()
        self.hanh_kiem.clear()
        self.table.setRowCount(0)  # Clear all rows in the table


    def delete_information(self):
        self.table.removeRow(self.table.currentRow())

    def GiaoVienMain_Return(self):
        self.teacher_main.hide()
        self.show()

    def goback_tc_Clicked(self):
        self.teacher_login.hide()
        self.show()

    def renew(self):
        if not self.renewpass:
            self.renewpass = uic.loadUi("gui/renewpass.ui")
            self.renewpass.renew_btn.clicked.connect(self.renew_Clicked)
            self.renewpass.return_btn.clicked.connect(self.renew_Return)
            self.phone_validator = QIntValidator()
            self.phone_validator.setBottom(0)
            self.phone_validator.setTop(999999999)
            self.renewpass.PhoneRC.setValidator(self.phone_validator)
            self.renewpass.PassRC.setEchoMode(QLineEdit.EchoMode.Password)
            self.renewpass.RePassRC.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.renewpass.show()
        self.hide()

    def renew_Clicked(self):
        Phone = self.renewpass.PhoneRC.text()
        password = self.renewpass.PassRC.text()
        repass = self.renewpass.RePassRC.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        if not repass:
            self.msg_box.setText("vui lòng nhập lại mật khẩu!")
            self.msg_box.exec()
            return
        if password != repass:
            self.msg_box.setText("mật khẩu không trùng khớp!")
            self.msg_box.exec()
            return

        self.renewpass.hide()
        self.show()

    def renew_Return(self):
        self.renewpass.hide()
        self.teacher_login.show()
        
    def upload_btvn(self):
        if not self.btvn_upload:
            self.btvn_upload = uic.loadUi("gui/btvn-upload.ui")
            self.btvn_upload.renew_btn.clicked.connect(self.upload_click)
            self.btvn_upload.return_btn.clicked.connect(self.return_upload)

        self.btvn_upload.show()
        self.hide()
        
    def upload_click(self):
        self.btvn_upload.hide()
        self.teacher_main.show()

    def return_upload(self):
        self.btvn_upload.hide()
        self.teacher_main.show()

    def regis(self):
        if not self.register:
            self.register = uic.loadUi("gui/regis.ui")
            self.register.female.toggled.connect(lambda: self.btnstate(self.register.female))
            self.register.male.toggled.connect(lambda: self.btnstate(self.register.male))
            self.phone_validator = QIntValidator()
            self.phone_validator.setBottom(0)
            self.phone_validator.setTop(999999999)
            self.register.Phone.setValidator(self.phone_validator)
            self.register.Register_btn.clicked.connect(self.re_register)
            self.register.return_btn.clicked.connect(self.return_register)
            self.register.Pass.setEchoMode(QLineEdit.EchoMode.Password)
            self.register.RePass.setEchoMode(QLineEdit.EchoMode.Password)

        self.register.show()
        self.hide()

    def re_register(self):
        Phone = self.register.Phone.text()
        password = self.register.Pass.text()
        repass = self.register.RePass.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        if not repass:
            self.msg_box.setText("vui lòng nhập lại mật khẩu!")
            self.msg_box.exec()
            return
        if password != repass:
            self.msg_box.setText("mật khẩu không trùng khớp!")
            self.msg_box.exec()
            return

        self.register.hide()
        self.show()

    def return_register(self):
        self.register.hide()
        self.show()

    def btnstate(self, btn):
        if btn.text() == "Nữ":
            if btn.isChecked():
                print(btn.text() + " is selected")
        if btn.text() == "Nam":
            if btn.isChecked():
                print(btn.text() + " is selected")

    def Login_hs(self):
        if not self.student_login:
            self.student_login = uic.loadUi("gui/login-hs.ui")
            self.student_login.HocSinhLogin_btn.clicked.connect(self.HocSinhClicked)
            self.student_login.goback_hs_btn.clicked.connect(self.goback_hs_Clicked)

        self.student_login.show()
        self.hide()

    def HocSinhClicked(self):
        Phone = self.student_login.PhoneHS.text()
        password = self.student_login.PassHS.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        
        self.GiaoVienClicked()

    def goback_hs_Clicked(self):
        self.student_login.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
