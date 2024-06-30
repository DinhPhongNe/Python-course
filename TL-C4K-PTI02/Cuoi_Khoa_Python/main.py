import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QLabel, QComboBox, QDialog, QVBoxLayout, QGridLayout
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
        self.chon_hoc_sinh_dialog = None
        self.nhap_diem_dialog = None
        self.sua_thong_tin_dialog = None
        self.sua_diem_dialog = None
        self.load_data()

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
            self.msg_box.setText("Vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("Vui lòng nhập mật khẩu!")
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
            self.teacher_main.nhap_diem_mon_btn.clicked.connect(self.show_chon_hoc_sinh_dialog)
            self.teacher_main.update_btn.clicked.connect(self.show_sua_thong_tin_dialog)
            self.teacher_main.delete_btn.clicked.connect(self.delete_information)
            self.teacher_main.search_btn.clicked.connect(self.search)
            self.teacher_main.clear_btn.clicked.connect(self.clear_information)
            self.teacher_main.btvn_upload_btn.clicked.connect(self.upload_btvn)

            self.table = self.teacher_main.findChild(QTabWidget, "Semester_tab")
            self.tab_widget = self.teacher_main.findChild(QTabWidget, "Semester_tab")
            self.table_HK1 = self.teacher_main.findChild(QTableWidget, "student_Infor_table_HK1")
            self.table_HK2 = self.teacher_main.findChild(QTableWidget, "student_Infor_table_HK2")
            self.table_CN = self.teacher_main.findChild(QTableWidget, "student_Infor_table_CN")
            self.xem_hk1 = self.teacher_main.findChild(QComboBox, "xem_diem_mon_hk1")
            self.xem_hk2 = self.teacher_main.findChild(QComboBox, "xem_diem_mon_hk2")
            self.xem_cn = self.teacher_main.findChild(QComboBox, "xem_diem_mon_cn")
            self.search_bar = self.teacher_main.findChild(QLineEdit, "Search_bar")
            
            self.stt = self.teacher_main.findChild(QLineEdit, "so_thu_tu")    
            self.ho = self.teacher_main.findChild(QLineEdit, "ho")
            self.ten = self.teacher_main.findChild(QLineEdit, "ten")        
            
            
            self.tab_widget.currentChanged.connect(self.on_tab_changed)
            self.on_tab_changed(self.tab_widget.currentIndex())

            self.setup_table(self.table_HK1, "Học kỳ 1")
            self.setup_table(self.table_HK2, "Học kỳ 2")
            self.setup_table(self.table_CN, "Cả năm")
            self.fill_tables()

            self.xem_hk1.currentTextChanged.connect(lambda text: self.show_column(self.table_HK1, text))
            self.xem_hk2.currentTextChanged.connect(lambda text: self.show_column(self.table_HK2, text))
            self.xem_cn.currentTextChanged.connect(lambda text: self.show_column(self.table_CN, text))

        self.teacher_main.show()
        self.teacher_login.hide()

    def on_tab_changed(self, index):
        """Cập nhật self.table dựa trên tab hiện tại."""
        if index == 0:
            self.table = self.table_HK1
        elif index == 1:
            self.table = self.table_HK2
        elif index == 2:
            self.table = self.table_CN
            
    def load_data(self):
        try:
            with open("test.json", "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"Danh_sach_hoc_sinh": []}
        except Exception as e:
            print(f"Lỗi khi đọc file test.json: {e}") 

    def save_data(self):
        with open("test.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def setup_table(self, table, semester):
        table.setColumnCount(11)
        table.setHorizontalHeaderLabels(
            [
                "Số thứ tự",
                "Họ",
                "Tên",
                "TX1",
                "TX2",
                "TX3",
                "TX4",
                "GK",
                "HK",
                "ĐTB",
                "Điểm TB môn cả năm",
            ]
        )
        table.setColumnWidth(0, 50)
        table.setColumnWidth(1, 50)
        table.setColumnWidth(2, 80)
        table.setColumnWidth(3, 80)
        table.setColumnWidth(4, 40)
        table.setColumnWidth(5, 40)
        table.setColumnWidth(6, 40)
        table.setColumnWidth(7, 40)
        table.setColumnWidth(8, 40)
        table.setColumnWidth(9, 40)
        table.setColumnWidth(10, 50)

        table.setAlternatingRowColors(True)
        table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        for i in range(table.columnCount()):
            table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def fill_tables(self):
        self.table_HK1.setRowCount(len(self.data["Danh_sach_hoc_sinh"]))
        self.table_HK2.setRowCount(len(self.data["Danh_sach_hoc_sinh"]))
        self.table_CN.setRowCount(len(self.data["Danh_sach_hoc_sinh"]))

        for row, student in enumerate(self.data["Danh_sach_hoc_sinh"]):
            # Thêm thông tin học sinh vào các cột tương ứng (chỉnh sửa chỉ số cột)
            self.table_HK1.setItem(row, 0, QTableWidgetItem(student.get("Số thứ tự", ""))) 
            self.table_HK1.setItem(row, 1, QTableWidgetItem(student.get("Họ", "")))  
            self.table_HK1.setItem(row, 2, QTableWidgetItem(student.get("Tên", ""))) 

            self.table_HK2.setItem(row, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
            self.table_HK2.setItem(row, 1, QTableWidgetItem(student.get("Họ", "")))
            self.table_HK2.setItem(row, 2, QTableWidgetItem(student.get("Tên", "")))

            self.table_CN.setItem(row, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
            self.table_CN.setItem(row, 1, QTableWidgetItem(student.get("Họ", "")))
            self.table_CN.setItem(row, 2, QTableWidgetItem(student.get("Tên", "")))
            
            for i, subject in enumerate(
                [
                    "Toán",
                    "Văn",
                    "Anh",
                    "Khoa học tự nhiên",
                    "Lịch sử - địa lý",
                    "Tin học",
                    "Công nghệ",
                    "Giáo dục công dân",
                ]
            ):
                for semester_key, table in [
                    ("Học kỳ 1", self.table_HK1),
                    ("Học kỳ 2", self.table_HK2),
                ]:
                    if semester_key in student.get("Điểm trong năm", {}) and subject in student["Điểm trong năm"][
                        semester_key
                    ]:
                        for j, grade_type in enumerate(
                            ["TX1", "TX2", "TX3", "TX4", "GK1" if semester_key == "Học kỳ 1" else "GK2", "HK1" if semester_key == "Học kỳ 1" else "HK2", "ĐTBM"]
                        ):
                            table.setItem(
                                row,
                                i + 4 + j,
                                QTableWidgetItem(
                                    str(student["Điểm trong năm"][semester_key][subject].get(grade_type, ""))
                                ),
                            )

            if "Học kỳ 1" in student.get("Điểm trong năm", {}) and "Học kỳ 2" in student.get("Điểm trong năm", {}):
                try:
                    dtbm_hk1 = float(student["Điểm trong năm"]["Học kỳ 1"]["Toán"]["ĐTBM"])
                    dtbm_hk2 = float(student["Điểm trong năm"]["Học kỳ 2"]["Toán"]["ĐTBM"])
                    dtbm_cn = ((dtbm_hk1 + dtbm_hk2) * 2) / 3
                    self.table_CN.setItem(row, 11, QTableWidgetItem(f"{dtbm_cn:.2f}"))
                except KeyError:
                    pass

    def show_column(self, table, subject):
            # Ẩn các cột liên quan đến điểm môn học (từ cột "TX1" đến "ĐTBM")
            for column in range(10, 16):  # Thay đổi vòng lặp từ 10 đến 17
                table.setColumnHidden(column, True)

            if subject:
                column_index = 4
                for i, item in enumerate(
                    [
                        "Toán",
                        "Văn",
                        "Anh",
                        "Khoa học tự nhiên",
                        "Lịch sử - địa lý",
                        "Tin học",
                        "Công nghệ",
                        "Giáo dục công dân",
                    ]
                ):
                    if item == subject:
                        column_index += i
                        break

            # Hiển thị các cột liên quan đến môn học được chọn
            for column in range(column_index, column_index + 8):  # Thay đổi vòng lặp
                table.setColumnHidden(column, False)

            # Hiển thị cột "ĐTBM"
            table.setColumnHidden(10, False)

    def search(self):
        text = self.search_bar.text().strip().lower()
        for row in range(self.table_HK1.rowCount()):
            match = False
            for column in range(self.table_HK1.columnCount()):
                item = self.table_HK1.item(row, column)
                if item and text in item.text().strip().lower():
                    match = True
                    break
            self.table_HK1.setRowHidden(row, not match)

        for row in range(self.table_HK2.rowCount()):
            match = False
            for column in range(self.table_HK2.columnCount()):
                item = self.table_HK2.item(row, column)
                if item and text in item.text().strip().lower():
                    match = True
                    break
            self.table_HK2.setRowHidden(row, not match)

        for row in range(self.table_CN.rowCount()):
            match = False
            for column in range(self.table_CN.columnCount()):
                item = self.table_CN.item(row, column)
                if item and text in item.text().strip().lower():
                    match = True
                    break
            self.table_CN.setRowHidden(row, not match)

    def show_chon_hoc_sinh_dialog(self):
        if not self.chon_hoc_sinh_dialog:
            self.chon_hoc_sinh_dialog = QDialog(self)
            self.chon_hoc_sinh_dialog.setWindowTitle("Chọn học sinh")

            layout = QVBoxLayout()
            self.chon_hs_combo = QComboBox()
            for student in self.data["Danh_sach_hoc_sinh"]:
                self.chon_hs_combo.addItem(f"{student.get('Họ', '')} {student.get('Tên', '')}")
            layout.addWidget(self.chon_hs_combo)

            chon_btn = QPushButton("Chọn")
            chon_btn.clicked.connect(self.show_nhap_diem_dialog)
            layout.addWidget(chon_btn)

            self.chon_hoc_sinh_dialog.setLayout(layout)
        self.chon_hoc_sinh_dialog.show()


    def show_nhap_diem_dialog(self):
        if not self.nhap_diem_dialog:
            self.nhap_diem_dialog = QDialog(self)
            self.nhap_diem_dialog.setWindowTitle("Nhập điểm")

            layout = QVBoxLayout()
            self.nhap_diem_dialog.setLayout(layout)  # Thiết lập layout cho dialog trước

            label_hk = QLabel("Chọn học kỳ:")
            self.combo_hk = QComboBox()
            self.combo_hk.addItems(["Học kỳ 1", "Học kỳ 2"])
            self.combo_hk.currentTextChanged.connect(self.update_nhap_diem_dialog)
            layout.addWidget(label_hk)
            layout.addWidget(self.combo_hk)

            self.grid_layout = QGridLayout()
            self.create_nhap_diem_form("Học kỳ 1")
            layout.addLayout(self.grid_layout)

        self.nhap_diem_dialog.show()


    def update_nhap_diem_dialog(self, text):
        self.grid_layout.deleteLater()
        self.grid_layout = QGridLayout()  # Tạo layout mới 
        self.create_nhap_diem_form(text)
        self.nhap_diem_dialog.layout().addLayout(self.grid_layout)
        
        
    def create_nhap_diem_form(self, hoc_ki):
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(QLabel("Môn học:"), 0, 0)
        self.combo_mon = QComboBox()
        self.combo_mon.addItems(
            [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ]
        )
        self.grid_layout.addWidget(self.combo_mon, 0, 1)
        self.grid_layout.addWidget(QLabel("TX1:"), 1, 0)
        self.tx1 = QLineEdit()
        self.grid_layout.addWidget(self.tx1, 1, 1)
        self.grid_layout.addWidget(QLabel("TX2:"), 2, 0)
        self.tx2 = QLineEdit()
        self.grid_layout.addWidget(self.tx2, 2, 1)
        self.grid_layout.addWidget(QLabel("TX3:"), 3, 0)
        self.tx3 = QLineEdit()
        self.grid_layout.addWidget(self.tx3, 3, 1)
        self.grid_layout.addWidget(QLabel("TX4:"), 4, 0)
        self.tx4 = QLineEdit()
        self.grid_layout.addWidget(self.tx4, 4, 1)
        self.grid_layout.addWidget(QLabel("GK:"), 5, 0)
        self.gk = QLineEdit()
        self.grid_layout.addWidget(self.gk, 5, 1)
        self.grid_layout.addWidget(QLabel("HK:"), 6, 0)
        self.hk = QLineEdit()
        self.grid_layout.addWidget(self.hk, 6, 1)
        self.luu_btn = QPushButton("Lưu")
        self.luu_btn.clicked.connect(self.nhap_diem_luu)
        self.grid_layout.addWidget(self.luu_btn, 7, 0, 1, 2)

        self.nhap_diem_dialog.layout().addLayout(self.grid_layout)

    def nhap_diem_luu(self):
        selected_student_index = self.chon_hs_combo.currentIndex()
        if selected_student_index == -1:
            return

        hoc_ki = self.combo_hk.currentText()
        mon_hoc = self.combo_mon.currentText()
        tx1 = self.tx1.text()
        tx2 = self.tx2.text()
        tx3 = self.tx3.text()
        tx4 = self.tx4.text()
        gk = self.gk.text()
        hk = self.hk.text()

        student = self.data["Danh_sach_hoc_sinh"][selected_student_index]

        # Đảm bảo cấu trúc dữ liệu chính xác
        if "Điểm trong năm" not in student:
            student["Điểm trong năm"] = {}
        if hoc_ki not in student["Điểm trong năm"]:
            student["Điểm trong năm"][hoc_ki] = {}
        if mon_hoc not in student["Điểm trong năm"][hoc_ki]:
            student["Điểm trong năm"][hoc_ki][mon_hoc] = {}

        # Lưu điểm vào cấu trúc dữ liệu
        student["Điểm trong năm"][hoc_ki][mon_hoc]["TX1"] = tx1
        student["Điểm trong năm"][hoc_ki][mon_hoc]["TX2"] = tx2
        student["Điểm trong năm"][hoc_ki][mon_hoc]["TX3"] = tx3
        student["Điểm trong năm"][hoc_ki][mon_hoc]["TX4"] = tx4
        student["Điểm trong năm"][hoc_ki][mon_hoc]["GK1" if hoc_ki == "Học kỳ 1" else "GK2"] = gk
        student["Điểm trong năm"][hoc_ki][mon_hoc]["HK1" if hoc_ki == "Học kỳ 1" else "HK2"] = hk

        dtbm = self.calculate_dtbm(tx1, tx2, tx3, tx4, gk, hk)
        if dtbm is not None:
            student["Điểm trong năm"][hoc_ki][mon_hoc]["ĐTBM"] = f"{dtbm:.2f}"

        # Cập nhật table tương ứng
        if hoc_ki == "Học kỳ 1":
            self.table_HK1.setItem(selected_student_index, 10, QTableWidgetItem(f"{dtbm:.2f}"))
        elif hoc_ki == "Học kỳ 2":
            self.table_HK2.setItem(selected_student_index, 10, QTableWidgetItem(f"{dtbm:.2f}"))

        self.save_data()
        self.nhap_diem_dialog.close()

    def calculate_dtbm(self, tx1, tx2, tx3, tx4, gk, hk):
        try:
            tx1 = float(tx1)
            tx2 = float(tx2)
            tx3 = float(tx3)
            tx4 = float(tx4)
            gk = float(gk)
            hk = float(hk)
            dtbm = ((tx1 + tx2 + tx3 + tx4) + (gk * 2) + (hk * 3)) / 9
            return dtbm
        except ValueError:
            self.msg_box.setText("Vui lòng nhập số cho điểm.")
            self.msg_box.exec()
            return None

    def show_sua_thong_tin_dialog(self):
        self.sua_thong_tin_dialog = QDialog(self)
        self.sua_thong_tin_dialog.setWindowTitle("Thêm thông tin học sinh")
        layout = QGridLayout()

        layout.addWidget(QLabel("Số thứ tự:"), 1, 0)
        self.stt = self.teacher_main.findChild(QLineEdit, "so_thu_tu") # Sử dụng QLineEdit "so_thu_tu" có sẵn
        layout.addWidget(self.stt, 1, 1)

        layout.addWidget(QLabel("Họ:"), 2, 0)
        self.ho = self.teacher_main.findChild(QLineEdit, "ho")  # Sử dụng QLineEdit "ho" có sẵn
        layout.addWidget(self.ho, 2, 1)

        layout.addWidget(QLabel("Tên:"), 3, 0)
        self.ten = self.teacher_main.findChild(QLineEdit, "ten")  # Sử dụng QLineEdit "ten" có sẵn
        layout.addWidget(self.ten, 3, 1)

        luu_btn = QPushButton("Lưu")
        luu_btn.clicked.connect(self._add_information_to_table)
        layout.addWidget(luu_btn, 4, 0, 1, 2)

        self.sua_thong_tin_dialog.setLayout(layout)

    def show_sua_thong_tin_dialog_hoc_sinh(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            self.sua_thong_tin_dialog = QDialog(self)
            self.sua_thong_tin_dialog.setWindowTitle("Sửa thông tin học sinh")
            layout = QGridLayout()

            layout.addWidget(QLabel("Số thứ tự:"), 0, 0)
            self.stt = QLineEdit(student["Số thứ tự"])
            layout.addWidget(self.stt, -1, 1)

            layout.addWidget(QLabel("Họ:"), 1, 0)
            self.ho = QLineEdit(student["Họ"])
            layout.addWidget(self.ho, 0, 1)

            layout.addWidget(QLabel("Tên:"), 2, 0)
            self.ten = QLineEdit(student["Tên"])
            layout.addWidget(self.ten, 1, 1)

            luu_btn = QPushButton("Lưu")
            luu_btn.clicked.connect(self.update_thong_tin_hoc_sinh)
            layout.addWidget(luu_btn, 4, 0, 1, 2)

            self.sua_thong_tin_dialog.setLayout(layout)
            self.sua_thong_tin_dialog.show()

    def update_thong_tin_hoc_sinh(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            new_stt = self.stt.text()
            new_ho = self.ho.text()
            new_ten = self.ten.text()
            
            if new_stt:
                student["Số thứ tự"] = new_stt
                self.table_HK1.setItem(current_row, 1, QTableWidgetItem(new_stt))
                self.table_HK2.setItem(current_row, 1, QTableWidgetItem(new_stt))
                self.table_CN.setItem(current_row, 1, QTableWidgetItem(new_stt))
            if new_ho:
                student["Họ"] = new_ho
                self.table_HK1.setItem(current_row, 2, QTableWidgetItem(new_ho))
                self.table_HK2.setItem(current_row, 2, QTableWidgetItem(new_ho))
                self.table_CN.setItem(current_row, 2, QTableWidgetItem(new_ho))
            if new_ten:
                student["Tên"] = new_ten
                self.table_HK1.setItem(current_row, 3, QTableWidgetItem(new_ten))
                self.table_HK2.setItem(current_row, 3, QTableWidgetItem(new_ten))
                self.table_CN.setItem(current_row, 3, QTableWidgetItem(new_ten))

            self.save_data()
            self.sua_thong_tin_dialog.close()

    def show_sua_diem_dialog(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            self.sua_diem_dialog = QDialog(self)
            self.sua_diem_dialog.setWindowTitle("Sửa điểm học sinh")
            layout = QGridLayout()

            layout.addWidget(QLabel("Chọn học kỳ:"), 0, 0)
            self.combo_hk_sua = QComboBox()
            self.combo_hk_sua.addItems(["Học kỳ 1", "Học kỳ 2"])
            self.combo_hk_sua.currentTextChanged.connect(self.update_sua_diem_dialog)
            layout.addWidget(self.combo_hk_sua, 0, 1)

            self.grid_layout_sua = QGridLayout()
            self.create_sua_diem_form("Học kỳ 1", student)

            layout.addLayout(self.grid_layout_sua, 1, 0, 1, 2)

            self.sua_diem_dialog.setLayout(layout)
            self.sua_diem_dialog.show()

    def update_sua_diem_dialog(self, text):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            self.grid_layout_sua.deleteLater()
            self.grid_layout_sua = QGridLayout()
            self.create_sua_diem_form(text, student)
            self.sua_diem_dialog.layout().addLayout(self.grid_layout_sua, 1, 0, 1, 2)

    def create_sua_diem_form(self, hoc_ki, student):
        self.grid_layout_sua.addWidget(QLabel("Môn học:"), 0, 0)
        self.combo_mon_sua = QComboBox()
        self.combo_mon_sua.addItems(
            [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ]
        )
        self.combo_mon_sua.currentTextChanged.connect(self.update_sua_diem_form_mon_hoc)
        self.grid_layout_sua.addWidget(self.combo_mon_sua, 0, 1)

        self.update_sua_diem_form_mon_hoc("Toán")

    def update_sua_diem_form_mon_hoc(self, mon_hoc):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            hoc_ki = self.combo_hk_sua.currentText()
            self.grid_layout_sua.addWidget(QLabel("TX1:"), 1, 0)
            self.tx1_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX1"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.tx1_sua, 1, 1)
            self.grid_layout_sua.addWidget(QLabel("TX2:"), 2, 0)
            self.tx2_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX2"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.tx2_sua, 2, 1)
            self.grid_layout_sua.addWidget(QLabel("TX3:"), 3, 0)
            self.tx3_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX3"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.tx3_sua, 3, 1)
            self.grid_layout_sua.addWidget(QLabel("TX4:"), 4, 0)
            self.tx4_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX4"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.tx4_sua, 4, 1)
            self.grid_layout_sua.addWidget(QLabel("GK:"), 5, 0)
            self.gk_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["GK1" if hoc_ki == "Học kỳ 1" else "GK2"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.gk_sua, 5, 1)
            self.grid_layout_sua.addWidget(QLabel("HK:"), 6, 0)
            self.hk_sua = QLineEdit(
                student["Điểm trong năm"][hoc_ki][mon_hoc]["HK1" if hoc_ki == "Học kỳ 1" else "HK2"] if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki] else ""
            )
            self.grid_layout_sua.addWidget(self.hk_sua, 6, 1)
            
            luu_btn_sua = QPushButton("Lưu")
            luu_btn_sua.clicked.connect(self.update_diem_hoc_sinh)
            self.grid_layout_sua.addWidget(luu_btn_sua, 7, 0, 1, 2)

    def update_diem_hoc_sinh(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            hoc_ki = self.combo_hk_sua.currentText()
            mon_hoc = self.combo_mon_sua.currentText()

            if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki]:
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX1"] = self.tx1_sua.text()
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX2"] = self.tx2_sua.text()
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX3"] = self.tx3_sua.text()
                student["Điểm trong năm"][hoc_ki][mon_hoc]["TX4"] = self.tx4_sua.text()
                student["Điểm trong năm"][hoc_ki][mon_hoc][
                    "GK1" if hoc_ki == "Học kỳ 1" else "GK2"
                ] = self.gk_sua.text()
                student["Điểm trong năm"][hoc_ki][mon_hoc][
                    "HK1" if hoc_ki == "Học kỳ 1" else "HK2"
                ] = self.hk_sua.text()
                dtbm = self.calculate_dtbm(
                    self.tx1_sua.text(),
                    self.tx2_sua.text(),
                    self.tx3_sua.text(),
                    self.tx4_sua.text(),
                    self.gk_sua.text(),
                    self.hk_sua.text(),
                )
                if dtbm is not None:
                    student["Điểm trong năm"][hoc_ki][mon_hoc]["ĐTBM"] = f"{dtbm:.2f}"
                    if hoc_ki == "Học kỳ 1":
                        self.table_HK1.setItem(current_row, 10, QTableWidgetItem(f"{dtbm:.2f}"))
                    else:
                        self.table_HK2.setItem(current_row, 10, QTableWidgetItem(f"{dtbm:.2f}"))

                self.save_data()
                self.sua_diem_dialog.close()

    def add_information(self):
        # Kiểm tra xem người dùng đã nhập đủ thông tin hay chưa
        if not self.stt.text() or not self.ho.text() or not self.ten.text():
            self.msg_box.setText("Vui lòng nhập đầy đủ thông tin!")
            self.msg_box.exec()
            return
        # Thêm thông tin học sinh mới vào dữ liệu
        new_student = {
            "Số thứ tự": self.stt.text(),
            "Họ": self.ho.text(),
            "Tên": self.ten.text(),
            "Điểm trong năm": {},
        }
        self.data["Danh_sach_hoc_sinh"].append(new_student)
        
        # Cập nhật lại bảng sau khi thêm
        self.fill_tables()

        # Xóa nội dung trong các QLineEdit
        self.stt.clear()
        self.ho.clear()
        self.ten.clear()



    def clear_information(self):
        self.msg_box.setText(
            "Hệ thống đang thông báo đến hiệu trưởng. Đang chờ hiệu trưởng đồng ý hoặc không đồng ý."
        )
        self.msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msg_box.exec()

        approval = random.choice(["Đồng ý", "Không đồng ý"])

        if approval == "Đồng ý":
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("Hiệu trưởng đã đồng ý. Toàn bộ học sinh sẽ bị xóa.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            
            result = confirm_box.exec()
            if result == QMessageBox.StandardButton.Ok:
                self._clear_all_fields()
        else:
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("Hiệu trưởng không đồng ý.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.exec()

    def _clear_all_fields(self):
        self.data["Danh_sach_hoc_sinh"] = []
        self.fill_tables()

    def delete_information(self):
        current_row = self.table.currentRow()
        if current_row != -1:
            del self.data["Danh_sach_hoc_sinh"][current_row]
            self.fill_tables()

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
            self.btvn_upload.pushButton.clicked.connect(self.upload_click)
            #self.btvn_upload.return_btn.clicked.connect(self.return_upload)

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
            self.student_login = uic.loadUi("gui/login-student.ui")
            self.student_login.HocSinhLogin_btn.clicked.connect(self.HocSinhClicked)
            self.student_login.goback_hs_btn.clicked.connect(self.goback_hs_Clicked)

        self.student_login.show()
        self.hide()

    def HocSinhClicked(self):
        Phone = self.student_login.Phone_HS.text()
        password = self.student_login.Pass_HS.text()
        
        if not Phone:
            self.msg_box.setText("vui lòng nhập số điện thoại!")
            self.msg_box.exec()
            return
        if not password:
            self.msg_box.setText("vui lòng nhập mật khẩu!")
            self.msg_box.exec()
            return
        
        self.HocSinhClicked()

    def goback_hs_Clicked(self):
        self.student_login.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
