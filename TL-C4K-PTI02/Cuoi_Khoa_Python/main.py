import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QLabel, QComboBox, QDialog, QVBoxLayout, QGridLayout, QListWidget, QFileDialog, QInputDialog
from PyQt6 import uic
import random
import json
import os
import shutil

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
        
        self.chon_hs_combo = QComboBox()
        self.load_data()

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
        self.xem_bai_tap_dialog = None
        self.load_data()
        
        # Khởi tạo current_teacher_table và current_student_table
        self.current_teacher_table = None
        self.current_student_table = None

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
            self.teacher_main.xem_bai_tap.clicked.connect(self.show_xem_bai_tap_dialog)
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
        """Cập nhật self.current_teacher_table dựa trên tab hiện tại của giáo viên."""
        if index == 0:
            self.current_teacher_table = self.table_HK1
        elif index == 1:
            self.current_teacher_table = self.table_HK2
        elif index == 2:
            self.current_teacher_table = self.table_CN

        # Cập nhật lại combobox môn học cho tab hiện tại
        self.update_subject_combobox()
            
    def load_data(self):
        """Load data from JSON file and sort students."""
        try:
            with open("diem_database.json", "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"Danh_sach_hoc_sinh": []}
        except Exception as e:
            print(f"Lỗi khi đọc file diem_database.json: {e}")

        self.sort_students()  # Sort students after loading data

    def save_data(self):
        """Sort students before saving data to JSON file."""
        self.sort_students()
        with open("diem_database.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def sort_students(self):
        """Sort students based on their "Số thứ tự" in ascending order."""
        self.data["Danh_sach_hoc_sinh"].sort(key=lambda student: int(student["Số thứ tự"]))

    def setup_table(self, table, semester):
        """Thiết lập bảng, bao gồm cả bảng điểm trung bình cả năm."""
        if semester == "Cả năm":
            column_count = 8  # STT, Họ, Tên, GK1, HK1, GK2, HK2, ĐTBCN
            header_labels = ["STT", "Họ", "Tên", "GK1", "HK1", "GK2", "HK2", "ĐTBCN"]
        else:
            column_count = 11
            header_labels = [
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

        table.setColumnCount(column_count)
        table.setHorizontalHeaderLabels(header_labels)
        
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
        self.table_HK1.setRowCount(0)
        self.table_HK2.setRowCount(0)
        self.table_CN.setRowCount(0) 
        

    def fill_tables(self):
        """Điền dữ liệu vào bảng, bao gồm cả bảng điểm trung bình cả năm."""
        self.table_HK1.setRowCount(0)
        self.table_HK2.setRowCount(0)
        self.table_CN.setRowCount(0)

        for row, student in enumerate(self.data["Danh_sach_hoc_sinh"]):
            # Thêm thông tin học sinh vào các cột tương ứng
            row_position = self.table_HK1.rowCount()
            self.table_HK1.insertRow(row_position)
            self.table_HK2.insertRow(row_position)
            self.table_CN.insertRow(row_position)

            self.table_HK1.setItem(row, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
            self.table_HK1.setItem(row, 1, QTableWidgetItem(student.get("Họ", "")))
            self.table_HK1.setItem(row, 2, QTableWidgetItem(student.get("Tên", "")))

            self.table_HK2.setItem(row, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
            self.table_HK2.setItem(row, 1, QTableWidgetItem(student.get("Họ", "")))
            self.table_HK2.setItem(row, 2, QTableWidgetItem(student.get("Tên", "")))

            # Điền số thứ tự, họ và tên vào table_CN
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
                # Điền điểm cho học kỳ 1 và 2
                for semester_key, table in [
                    ("Học kỳ 1", self.table_HK1),
                    ("Học kỳ 2", self.table_HK2),
                ]:
                    if (
                        semester_key in student.get("Điểm trong năm", {})
                        and subject in student["Điểm trong năm"][semester_key]
                    ):
                        for j, grade_type in enumerate(
                            [
                                "TX1",
                                "TX2",
                                "TX3",
                                "TX4",
                                "GK1" if semester_key == "Học kỳ 1" else "GK2",
                                "HK1" if semester_key == "Học kỳ 1" else "HK2",
                                "ĐTBM",
                            ]
                        ):
                            table.setItem(
                                row,
                                i + 3 + j,
                                QTableWidgetItem(
                                    str(
                                        student["Điểm trong năm"][semester_key][
                                            subject
                                        ].get(grade_type, "")
                                    )
                                ),
                            )

                # Điền điểm trung bình cả năm, bắt đầu từ cột 3
                try:
                    # Lấy giá trị chuỗi và chuyển đổi sang float, xử lý trường hợp chuỗi rỗng
                    gk1_str = student["Điểm trong năm"]["Học kỳ 1"][subject].get("GK1", "0")
                    gk1 = float(gk1_str) if gk1_str else 0.0
                    hk1_str = student["Điểm trong năm"]["Học kỳ 1"][subject].get("HK1", "0")
                    hk1 = float(hk1_str) if hk1_str else 0.0
                    gk2_str = student["Điểm trong năm"]["Học kỳ 2"][subject].get("GK2", "0")
                    gk2 = float(gk2_str) if gk2_str else 0.0
                    hk2_str = student["Điểm trong năm"]["Học kỳ 2"][subject].get("HK2", "0")
                    hk2 = float(hk2_str) if hk2_str else 0.0

                    dtbm_cn = (gk1 + hk1 + (gk2 + hk2) * 2) / 6  # Tính ĐTBCN

                    self.table_CN.setItem(row, i * 5 + 3, QTableWidgetItem(str(gk1) if gk1 else ""))
                    self.table_CN.setItem(row, i * 5 + 4, QTableWidgetItem(str(hk1) if hk1 else ""))
                    self.table_CN.setItem(row, i * 5 + 5, QTableWidgetItem(str(gk2) if gk2 else ""))
                    self.table_CN.setItem(row, i * 5 + 6, QTableWidgetItem(str(hk2) if hk2 else ""))
                    self.table_CN.setItem(row, i * 5 + 7, QTableWidgetItem(f"{dtbm_cn:.2f}"))
                except KeyError:
                    # Xử lý trường hợp thiếu điểm
                    for col in range(5):
                        self.table_CN.setItem(row, i * 5 + 3 + col, QTableWidgetItem(""))
                        
                        
    def show_column(self, table, subject):
        """Hiển thị cột điểm của môn học được chọn và ẩn các cột khác."""

        # Xác định số cột điểm cho mỗi môn
        columns_per_subject = 5 if table == self.table_CN else 7

        # Duyệt qua tất cả các môn học
        for i, subject_name in enumerate(
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
            # Tính toán chỉ số cột bắt đầu và kết thúc cho môn học hiện tại
            start_column = 15 + i * columns_per_subject
            end_column = start_column + columns_per_subject

            # Ẩn hoặc hiện các cột dựa trên môn học được chọn
            if subject == subject_name:
                for column in range(start_column, end_column):
                    table.setColumnHidden(column, False)
            else:
                for column in range(start_column, end_column):
                    table.setColumnHidden(column, True)

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
            # Gán giá trị cho thuộc tính chon_hs_combo
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

        # Cập nhật table tương ứng
        self.update_table_after_nhap_diem(hoc_ki, selected_student_index, mon_hoc)
        self.save_data()
        self.nhap_diem_dialog.close()

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
            
        hoc_ki = self.combo_hk.currentText()
        mon_hoc = self.combo_mon.currentText()
        if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki]:
            try:
                dtbm_hk1 = float(student["Điểm trong năm"]["Học kỳ 1"][mon_hoc]["ĐTBM"])
                dtbm_hk2 = float(student["Điểm trong năm"]["Học kỳ 2"][mon_hoc]["ĐTBM"])
                dtbm_cn = (dtbm_hk1 + (dtbm_hk2 * 2)) / 3
                column_index = 4 + [
                    "Toán",
                    "Văn",
                    "Anh",
                    "Khoa học tự nhiên",
                    "Lịch sử - địa lý",
                    "Tin học",
                    "Công nghệ",
                    "Giáo dục công dân",
                ].index(mon_hoc)
                self.table_CN.setItem(selected_student_index, column_index, QTableWidgetItem(f"{dtbm_cn:.2f}"))
            except KeyError:
                pass
            
        # Cập nhật điểm trung bình cả năm
        self.update_diem_trung_binh_ca_nam(selected_student_index, mon_hoc)
        self.save_data()  # Lưu dữ liệu JSON đã cập nhật
        self.fill_tables()  # Làm mới tất cả các bảng
        self.nhap_diem_dialog.close()
        
    def update_diem_trung_binh_ca_nam(self, student_index, subject):
        """Cập nhật cột Điểm TB môn cả năm trong bảng."""
        student = self.data["Danh_sach_hoc_sinh"][student_index]

        try:
            dtbm_hk1 = float(
                student["Điểm trong năm"]["Học kỳ 1"][subject]["ĐTBM"]
            )
            dtbm_hk2 = float(
                student["Điểm trong năm"]["Học kỳ 2"][subject]["ĐTBM"]
            )
            dtbm_cn = (dtbm_hk1 + (dtbm_hk2 * 2)) / 3

            column_index = 4 + [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ].index(subject)

            self.table_CN.setItem(
                student_index, column_index, QTableWidgetItem(f"{dtbm_cn:.2f}")
            )

        except KeyError:
            # Xử lý trường hợp thiếu điểm
            column_index = 4 + [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ].index(subject)
            self.table_CN.setItem(student_index, column_index, QTableWidgetItem(""))
        
    def update_table_after_nhap_diem(self, hoc_ki, row_index, mon_hoc):
        """Cập nhật table sau khi nhập điểm."""
        student = self.data["Danh_sach_hoc_sinh"][row_index]
        if hoc_ki == "Học kỳ 1":
            table = self.table_HK1
        elif hoc_ki == "Học kỳ 2":
            table = self.table_HK2
        else:
            return

        subject_order = [
            "Toán",
            "Văn",
            "Anh",
            "Khoa học tự nhiên",
            "Lịch sử - địa lý",
            "Tin học",
            "Công nghệ",
            "Giáo dục công dân",
        ]
        if mon_hoc in subject_order:
            column_index = 4 + subject_order.index(mon_hoc)

            # Check if semester and subject exist
            if (
                hoc_ki in student["Điểm trong năm"]
                and mon_hoc in student["Điểm trong năm"][hoc_ki]
            ):
                for j, grade_type in enumerate(
                    [
                        "TX1",
                        "TX2",
                        "TX3",
                        "TX4",
                        "GK1" if hoc_ki == "Học kỳ 1" else "GK2",
                        "HK1" if hoc_ki == "Học kỳ 1" else "HK2",
                        "ĐTBM",
                    ]
                ):
                    # Create subject key if it doesn't exist
                    if grade_type not in student["Điểm trong năm"][hoc_ki][mon_hoc]:
                        student["Điểm trong năm"][hoc_ki][mon_hoc][grade_type] = ""
                    
                    table.setItem(
                        row_index,
                        column_index + j,
                        QTableWidgetItem(
                            str(student["Điểm trong năm"][hoc_ki][mon_hoc].get(grade_type, ""))
                        ),
                    )

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
            return 0

    def show_sua_thong_tin_dialog(self):
        """Hiển thị hộp thoại để sửa thông tin học sinh."""
        current_row = self.current_teacher_table.currentRow()
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
        luu_btn.clicked.connect(self.add_information_to_table)
        layout.addWidget(luu_btn, 4, 0, 1, 2)

        self.sua_thong_tin_dialog.setLayout(layout)

    def show_sua_thong_tin_dialog(self):
        """Hiển thị hộp thoại để sửa thông tin học sinh."""
        current_row = self.table.currentRow()
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            self.sua_thong_tin_dialog = QDialog(self)
            self.sua_thong_tin_dialog.setWindowTitle("Sửa thông tin học sinh")
            layout = QGridLayout()

            layout.addWidget(QLabel("Số thứ tự:"), 0, 0)
            self.stt_edit = QLineEdit(student["Số thứ tự"])  # Use a different name
            layout.addWidget(self.stt_edit, 0, 1)

            layout.addWidget(QLabel("Họ:"), 1, 0)
            self.ho_edit = QLineEdit(student["Họ"])  # Use a different name
            layout.addWidget(self.ho_edit, 1, 1)

            layout.addWidget(QLabel("Tên:"), 2, 0)
            self.ten_edit = QLineEdit(student["Tên"])  # Use a different name
            layout.addWidget(self.ten_edit, 2, 1)

            luu_btn = QPushButton("Lưu")
            luu_btn.clicked.connect(self.update_thong_tin_hoc_sinh)
            layout.addWidget(luu_btn, 3, 0, 1, 2)

            self.sua_thong_tin_dialog.setLayout(layout)
            self.sua_thong_tin_dialog.show()
        else:
            self.msg_box.setText("Vui lòng chọn học sinh để sửa thông tin.")
            self.msg_box.exec()

    def update_thong_tin_hoc_sinh(self):
        """Cập nhật thông tin học sinh từ hộp thoại sửa."""
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            student["Số thứ tự"] = self.stt_edit.text()  # Update with edited values
            student["Họ"] = self.ho_edit.text()
            student["Tên"] = self.ten_edit.text()

            # Update the table directly
            self.table.setItem(current_row, 0, QTableWidgetItem(student["Số thứ tự"]))
            self.table.setItem(current_row, 1, QTableWidgetItem(student["Họ"]))
            self.table.setItem(current_row, 2, QTableWidgetItem(student["Tên"]))

            self.save_data()
            self.sua_thong_tin_dialog.close()
            
    def show_sua_diem_dialog(self):
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
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
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
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
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
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
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
        if current_row != -1:
            student = self.data["Danh_sach_hoc_sinh"][current_row]
            
        hoc_ki = self.combo_hk_sua.currentText()
        mon_hoc = self.combo_mon_sua.currentText()
        if hoc_ki in student["Điểm trong năm"] and mon_hoc in student["Điểm trong năm"][hoc_ki]:
            try:
                dtbm_hk1 = float(student["Điểm trong năm"]["Học kỳ 1"][mon_hoc]["ĐTBM"])
                dtbm_hk2 = float(student["Điểm trong năm"]["Học kỳ 2"][mon_hoc]["ĐTBM"])
                dtbm_cn = (dtbm_hk1 + (dtbm_hk2 * 2)) / 3
                column_index = 4 + [
                    "Toán",
                    "Văn",
                    "Anh",
                    "Khoa học tự nhiên",
                    "Lịch sử - địa lý",
                    "Tin học",
                    "Công nghệ",
                    "Giáo dục công dân",
                ].index(mon_hoc)
                self.table_CN.setItem(current_row, column_index, QTableWidgetItem(f"{dtbm_cn:.2f}"))
            except KeyError:
                pass
        self.save_data() # Save updated JSON data
        self.sua_diem_dialog.close()

    def add_information(self):
        # Kiểm tra xem người dùng đã nhập đủ thông tin hay chưa
        if not self.stt.text() or not self.ho.text() or not self.ten.text():
            self.msg_box.setText("Vui lòng nhập đầy đủ thông tin!")
            self.msg_box.exec()
            return

        # Get the text from the QLineEdit
        stt = self.stt.text()

        # Now validate the stt string 
        if not stt or len(stt) != 5 or not stt.isdigit() or int(stt[2:]) == 0:
            self.msg_box.setText("Số thứ tự không hợp lệ. Vui lòng nhập theo định dạng 'Số lớp - Số thứ tự' (ví dụ: 88041).")
            self.msg_box.exec()
            return

        # Khởi tạo biến new_student với thông tin học sinh mới
        new_student = {
            "Số thứ tự": stt,
            "Họ": self.ho.text(),
            "Tên": self.ten.text(),
            "Điểm trong năm": {
                "Học kỳ 1": {
                    "Toán": {},
                    "Văn": {},
                    "Anh": {},
                    "Khoa học tự nhiên": {},
                    "Lịch sử - địa lý": {},
                    "Tin học": {},
                    "Công nghệ": {},
                    "Giáo dục công dân": {},
                },
                "Học kỳ 2": {
                    "Toán": {},
                    "Văn": {},
                    "Anh": {},
                    "Khoa học tự nhiên": {},
                    "Lịch sử - địa lý": {},
                    "Tin học": {},
                    "Công nghệ": {},
                    "Giáo dục công dân": {},
                },
            },
        }

        # Thêm thông tin điểm trung bình cả năm (khởi tạo là null)
        new_student["Điểm trung bình cả năm"] = {
            "Học kỳ 1": {subject: {"GK1": None, "HK1": None} for subject in [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ]},
            "Học kỳ 2": {subject: {"GK2": None, "HK2": None} for subject in [
                "Toán",
                "Văn",
                "Anh",
                "Khoa học tự nhiên",
                "Lịch sử - địa lý",
                "Tin học",
                "Công nghệ",
                "Giáo dục công dân",
            ]}
        }

        self.data["Danh_sach_hoc_sinh"].append(new_student)
        


        # Cập nhật combobox chọn học sinh
        self.chon_hs_combo.addItem(f"{new_student['Họ']} {new_student['Tên']}")

        # Lưu dữ liệu vào file JSON
        self.save_data()

        # Cập nhật bảng sau khi thêm
        self.fill_tables()

        # Xóa nội dung trong các QLineEdit
        self.stt.clear()
        self.ho.clear()
        self.ten.clear()

    def update_subject_combobox(self):
        """Cập nhật combobox môn học dựa trên tab hiện tại của giáo viên."""
        if self.current_teacher_table is self.table_HK1: # Sử dụng current_teacher_table
            combobox = self.xem_hk1
        elif self.current_teacher_table is self.table_HK2:
            combobox = self.xem_hk2
        elif self.current_teacher_table is self.table_CN:
            combobox = self.xem_cn
        else:
            return

        combobox.clear()
        combobox.addItem("")
        combobox.addItems(
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
        current_row = self.current_teacher_table.currentRow() # Sử dụng current_teacher_table
        if current_row != -1:
            # Remove student from data dictionary
            del self.data["Danh_sach_hoc_sinh"][current_row]

            # Update the tables
            self.fill_tables()

            # Save the updated data to JSON file
            self.save_data()

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
            self.btvn_upload.clickTo_Upload.clicked.connect(self.upload_click)
            #self.btvn_upload.return_btn.clicked.connect(self.return_upload)

        self.btvn_upload.show()
        self.hide()
        
    def upload_click(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Chọn file bài tập",
            "",
            "All Files (*);;PDF Files (*.pdf);;Word Documents (*.docx);;PowerPoint Presentations (*.pptx)",
            options=options,
        )

        if file_path:
            folder_path = "btvn"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            file_name = os.path.basename(file_path)
            destination_path = os.path.join(folder_path, file_name)

            try:
                # Sao chép file vào thư mục "btvn"
                os.replace(file_path, destination_path)
                self.msg_box.setWindowTitle("Thông báo")
                self.msg_box.setIcon(QMessageBox.Icon.Information)
                self.msg_box.setText("Tải lên bài tập thành công!")
                self.msg_box.exec()

                # Cập nhật danh sách file bài tập trong QDialog xem bài tập
                if self.xem_bai_tap_dialog:
                    self.update_btvn_list()

            except Exception as e:
                self.msg_box.setText(f"Lỗi khi tải lên: {e}")
                self.msg_box.exec()

        self.btvn_upload.hide()
        self.teacher_main.show()
        
    def update_btvn_list(self):
        self.btvn_list.clear()
        folder_path = "btvn"
        if os.path.exists(folder_path):
            file_list = os.listdir(folder_path)
            if file_list:
                for file_name in file_list:
                    self.btvn_list.addItem(file_name)
            else:
                self.btvn_list.addItem("Hiện tại không có bài tập")
                
    def delete_btvn(self):
        selected_item = self.btvn_list.currentItem()
        if selected_item and selected_item.text() != "Hiện tại không có bài tập":
            file_name = selected_item.text()
            folder_path = "btvn"
            file_path = os.path.join(folder_path, file_name)

            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Xác nhận xóa")
            confirm_box.setText(f"Bạn có chắc muốn xóa {file_name}?")
            confirm_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            result = confirm_box.exec()
            if result == QMessageBox.StandardButton.Yes:
                try:
                    os.remove(file_path)
                    self.update_btvn_list()  # Cập nhật danh sách sau khi xóa
                    self.msg_box.setWindowTitle("Thông báo")
                    self.msg_box.setIcon(QMessageBox.Icon.Information)
                    self.msg_box.setText("Xóa bài tập thành công!")
                    self.msg_box.exec()
                except Exception as e:
                    self.msg_box.setText(f"Lỗi khi xóa: {e}")
                    self.msg_box.exec()

    def rename_btvn(self):
        selected_item = self.btvn_list.currentItem()
        if selected_item and selected_item.text() != "Hiện tại không có bài tập":
            old_file_name = selected_item.text()
            folder_path = "btvn"
            old_file_path = os.path.join(folder_path, old_file_name)

            new_file_name, ok = QInputDialog.getText(
                self, "Đổi tên bài tập", "Nhập tên mới:", text=old_file_name
            )
            if ok and new_file_name:
                new_file_path = os.path.join(folder_path, new_file_name)
                try:
                    os.rename(old_file_path, new_file_path)
                    self.update_btvn_list()  # Cập nhật danh sách sau khi đổi tên
                    self.msg_box.setWindowTitle("Thông báo")
                    self.msg_box.setIcon(QMessageBox.Icon.Information)
                    self.msg_box.setText("Đổi tên bài tập thành công!")
                    self.msg_box.exec()
                except Exception as e:
                    self.msg_box.setText(f"Lỗi khi đổi tên: {e}")
                    self.msg_box.exec()
                
    def download_btvn(self):
        selected_item = self.btvn_list.currentItem()
        if selected_item:
            file_name = selected_item.text()
            folder_path = "btvn"
            file_path = os.path.join(folder_path, file_name)

            options = QFileDialog.Option.DontUseNativeDialog
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Lưu Bài Tập",
                file_name,
                "All Files (*);;PDF Files (*.pdf);;Word Documents (*.docx);;PowerPoint Presentations (*.pptx)",
                options=options,
            )

            if save_path:
                try:
                    # Sao chép file từ thư mục "btvn" đến vị trí lưu
                    shutil.copy2(file_path, save_path)  # Sử dụng shutil.copy2()
                    self.msg_box.setWindowTitle("Thông báo")
                    self.msg_box.setIcon(QMessageBox.Icon.Information)
                    self.msg_box.setText("Tải xuống bài tập thành công!")
                    self.msg_box.exec()
                except Exception as e:
                    self.msg_box.setText(f"Lỗi khi tải xuống: {e}")
                    self.msg_box.exec()
        
    def show_xem_bai_tap_dialog(self):
        if not self.xem_bai_tap_dialog:
            self.xem_bai_tap_dialog = QDialog(self)
            self.xem_bai_tap_dialog.setWindowTitle("Xem Bài Tập")

            layout = QVBoxLayout()
            self.btvn_list = QListWidget()
            self.update_btvn_list()  # Hiển thị danh sách file bài tập
            layout.addWidget(self.btvn_list)

            # Thêm nút xóa
            delete_btn = QPushButton("Xóa")
            delete_btn.clicked.connect(self.delete_btvn)
            layout.addWidget(delete_btn)

            # Thêm nút chỉnh sửa tên
            rename_btn = QPushButton("Chỉnh Sửa Tên")
            rename_btn.clicked.connect(self.rename_btvn)
            layout.addWidget(rename_btn)

            download_btn = QPushButton("Tải Về")
            download_btn.clicked.connect(self.download_btvn)
            layout.addWidget(download_btn)

            self.xem_bai_tap_dialog.setLayout(layout)

        self.xem_bai_tap_dialog.show()

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
            self.student_login.HocSinhLogin_btn.clicked.connect(self.check_login_hs)
            self.student_login.goback_hs_btn.clicked.connect(self.goback_tc_Clicked)
            self.student_login.id_hs.setValidator(self.phone_validator) # Giả sử ID là số, bạn có thể thay đổi validator nếu cần

        self.student_login.show()
        self.hide()
    
    def check_login_hs(self):
        """Kiểm tra thông tin đăng nhập của học sinh."""
        id_tai_khoan = self.student_login.id_hs.text()
        mat_khau = self.student_login.pass_HS.text()

        try:
            with open("tk_hs_data.json", "r", encoding="utf-8") as f:
                tk_hs_data = json.load(f)
        except FileNotFoundError:
            self.msg_box.setText("Không tìm thấy file tk_hs_data.json!")
            self.msg_box.exec()
            return

        for tai_khoan in tk_hs_data.get("Danh_sach_tai_khoan", []):
            if (
                str(tai_khoan.get("id_tai_khoan", "")) == id_tai_khoan
                and str(tai_khoan.get("MK_tai_khoan", "")) == mat_khau
            ):
                self.student_login.hide()
                self.HocSinhClicked(tai_khoan)  # Truyền thông tin tài khoản
                return

        self.msg_box.setText("Sai ID tài khoản hoặc mật khẩu!")
        self.msg_box.exec()

    def HocSinhClicked(self, tai_khoan):
        """Hiển thị giao diện chính của học sinh."""

        # Luôn khởi tạo các thành phần UI
        self.student_main = uic.loadUi("gui/main-st.ui")
        self.tab_widget_hs = self.student_main.findChild(QTabWidget, "Semester_tab_hs")
        self.table_HK1_hs = self.student_main.findChild(QTableWidget, "student_Infor_table_HK1_hs")
        self.table_HK2_hs = self.student_main.findChild(QTableWidget, "student_Infor_table_HK2_hs")
        self.table_CN_hs = self.student_main.findChild(QTableWidget, "student_Infor_table_CN_hs")
        self.xem_hk1_hs = self.student_main.findChild(QComboBox, "xem_diem_mon_hk1_hs")
        self.xem_hk2_hs = self.student_main.findChild(QComboBox, "xem_diem_mon_hk2_hs")
        self.xem_cn_hs = self.student_main.findChild(QComboBox, "xem_diem_mon_cn_hs")

        self.student_main.ten_hoc_sinh.setText(tai_khoan.get("ten_tai_khoan", ""))
        self.student_main.so_thu_tu_hs.setText(str(tai_khoan.get("so_thu_tu", "")))
        self.student_main.id_tai_khoan.setText(str(tai_khoan.get("id_tai_khoan", "")))
        self.student_main.logOut_btn_tc.clicked.connect(self.HocSinhMain_Return)
        self.student_main.xem_bai_tap_hs.clicked.connect(self.show_xem_bai_tap_dialog_hs)
        
        self.tab_widget_hs.currentChanged.connect(self.on_tab_changed_hs)
        self.on_tab_changed_hs(self.tab_widget_hs.currentIndex()) 

        self.setup_table(self.table_HK1_hs, "Học kỳ 1")
        self.setup_table(self.table_HK2_hs, "Học kỳ 2")
        self.setup_table(self.table_CN_hs, "Cả năm")
        self.fill_tables_hs(tai_khoan)
        self.load_data()
        
        self.xem_hk1_hs.currentTextChanged.connect(lambda text: self.show_column(self.table_HK1_hs, text))
        self.xem_hk2_hs.currentTextChanged.connect(lambda text: self.show_column(self.table_HK2_hs, text))
        self.xem_cn_hs.currentTextChanged.connect(lambda text: self.show_column(self.table_CN_hs, text))

        self.student_main.show()
        
    def on_tab_changed_hs(self, index):
        """Cập nhật self.current_student_table dựa trên tab hiện tại của học sinh."""
        if index == 0:
            self.current_student_table = self.table_HK1_hs
        elif index == 1:
            self.current_student_table = self.table_HK2_hs
        elif index == 2:
            self.current_student_table = self.table_CN_hs

        # Cập nhật lại combobox môn học cho tab hiện tại
        self.update_subject_combobox_hs()
        
    def update_subject_combobox_hs(self):
        """Cập nhật combobox môn học dựa trên tab hiện tại của học sinh."""
        if self.current_student_table is self.table_HK1_hs:  # Sử dụng current_student_table
            combobox = self.xem_hk1_hs
        elif self.current_student_table is self.table_HK2_hs:
            combobox = self.xem_hk2_hs
        elif self.current_student_table is self.table_CN_hs:
            combobox = self.xem_cn_hs
        else:
            return

        combobox.clear()
        combobox.addItem("")
        combobox.addItems(
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
        
    def fill_tables_hs(self, tai_khoan):
        """Điền dữ liệu vào bảng điểm của học sinh."""
        self.table_HK1_hs.setRowCount(0)
        self.table_HK2_hs.setRowCount(0)
        self.table_CN_hs.setRowCount(0)
        
        # Lấy id_tai_khoan từ thông tin tài khoản
        student_id = tai_khoan.get("id_tai_khoan")

        # Tìm học sinh theo id_tai_khoan
        for student in self.data["Danh_sach_hoc_sinh"]:
            if student.get("Số thứ tự") == str(student_id):
                # Thêm thông tin học sinh vào các cột tương ứng
                row_position = self.table_HK1_hs.rowCount()
                self.table_HK1_hs.insertRow(row_position)
                self.table_HK2_hs.insertRow(row_position)
                self.table_CN_hs.insertRow(row_position)

                self.table_HK1_hs.setItem(0, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
                self.table_HK1_hs.setItem(0, 1, QTableWidgetItem(student.get("Họ", "")))
                self.table_HK1_hs.setItem(0, 2, QTableWidgetItem(student.get("Tên", "")))

                self.table_HK2_hs.setItem(0, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
                self.table_HK2_hs.setItem(0, 1, QTableWidgetItem(student.get("Họ", "")))
                self.table_HK2_hs.setItem(0, 2, QTableWidgetItem(student.get("Tên", "")))

                self.table_CN_hs.setItem(0, 0, QTableWidgetItem(student.get("Số thứ tự", "")))
                self.table_CN_hs.setItem(0, 1, QTableWidgetItem(student.get("Họ", "")))
                self.table_CN_hs.setItem(0, 2, QTableWidgetItem(student.get("Tên", "")))

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
                        ("Học kỳ 1", self.table_HK1_hs),
                        ("Học kỳ 2", self.table_HK2_hs),
                    ]:
                        if (
                            semester_key in student.get("Điểm trong năm", {})
                            and subject in student["Điểm trong năm"][semester_key]
                        ):
                            for j, grade_type in enumerate(
                                [
                                    "TX1",
                                    "TX2",
                                    "TX3",
                                    "TX4",
                                    "GK1" if semester_key == "Học kỳ 1" else "GK2",
                                    "HK1" if semester_key == "Học kỳ 1" else "HK2",
                                    "ĐTBM",
                                ]
                            ):
                                table.setItem(
                                    0,  # Luôn là hàng 0 vì chỉ có 1 học sinh
                                    i + 3 + j,
                                    QTableWidgetItem(
                                        str(
                                            student["Điểm trong năm"][semester_key][
                                                subject
                                            ].get(grade_type, "")
                                        )
                                    ),
                                )

                    try:
                        gk1_str = student["Điểm trong năm"]["Học kỳ 1"][subject].get("GK1", "0")
                        gk1 = float(gk1_str) if gk1_str else 0.0
                        hk1_str = student["Điểm trong năm"]["Học kỳ 1"][subject].get("HK1", "0")
                        hk1 = float(hk1_str) if hk1_str else 0.0
                        gk2_str = student["Điểm trong năm"]["Học kỳ 2"][subject].get("GK2", "0")
                        gk2 = float(gk2_str) if gk2_str else 0.0
                        hk2_str = student["Điểm trong năm"]["Học kỳ 2"][subject].get("HK2", "0")
                        hk2 = float(hk2_str) if hk2_str else 0.0

                        dtbm_cn = (gk1 + hk1 + (gk2 + hk2) * 2) / 6

                        self.table_CN_hs.setItem(0, i * 5 + 3, QTableWidgetItem(str(gk1) if gk1 else ""))
                        self.table_CN_hs.setItem(0, i * 5 + 4, QTableWidgetItem(str(hk1) if hk1 else ""))
                        self.table_CN_hs.setItem(0, i * 5 + 5, QTableWidgetItem(str(gk2) if gk2 else ""))
                        self.table_CN_hs.setItem(0, i * 5 + 6, QTableWidgetItem(str(hk2) if hk2 else ""))
                        self.table_CN_hs.setItem(0, i * 5 + 7, QTableWidgetItem(f"{dtbm_cn:.2f}"))
                    except KeyError:
                        for col in range(5):
                            self.table_CN_hs.setItem(0, i * 5 + 3 + col, QTableWidgetItem(""))
                break  # Đã tìm thấy học sinh, thoát khỏi vòng lặp

    def show_xem_bai_tap_dialog_hs(self):
        """Hiển thị hộp thoại xem bài tập cho học sinh (chỉ xem và tải về)."""
        if not self.xem_bai_tap_dialog:
            self.xem_bai_tap_dialog = QDialog(self)
            self.xem_bai_tap_dialog.setWindowTitle("Xem Bài Tập")

            layout = QVBoxLayout()
            self.btvn_list = QListWidget()
            self.update_btvn_list()  # Hiển thị danh sách file bài tập
            layout.addWidget(self.btvn_list)

            # Chỉ có nút tải về
            download_btn = QPushButton("Tải Về")
            download_btn.clicked.connect(self.download_btvn)
            layout.addWidget(download_btn)

            self.xem_bai_tap_dialog.setLayout(layout)

        self.xem_bai_tap_dialog.show()

    def HocSinhMain_Return(self):
        self.student_main.hide()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
