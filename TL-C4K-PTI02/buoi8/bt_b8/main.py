#_______TRAC NGHIEM_______
#CAU 1: B
#CAU 2: A
#CAU 3: B
#CAU 4: D
#CAU 5: C




#_______TU LUAN_______
import sys
import random
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QPushButton, QListWidget, QInputDialog
from PyQt6 import uic


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("main.ui", self)

        self.Add.clicked.connect(self.add)
        self.Edit.clicked.connect(self.edit)
        self.Delete_btn.clicked.connect(self.delete)
        self.clear_btn.clicked.connect(self.clear)
        self.search_btn.clicked.connect(self.search)

        self.search_bar = self.findChild(QLineEdit, "Search_bar")
        self.list_widget = self.findChild(QListWidget, "listWidget")

        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Lỗi")
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")

        self.load_data()

        self.update_list_widget()

        self.welcome_message()

    def welcome_message(self):
        welcome_box = QMessageBox()
        welcome_box.setWindowTitle("Chào mừng")
        welcome_box.setIcon(QMessageBox.Icon.Information)
        welcome_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
        welcome_box.setText("Chào mừng đến với sở thú")
        welcome_box.exec()

    def load_data(self):
        try:
            with open("infor.txt", "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"Danh_sach_thu": []}
        except json.decoder.JSONDecodeError:
            self.data = {"Danh_sach_thu": []} 
            self.save_data()

    def save_data(self):
        with open("infor.json", "w") as f:
            f.write(json.dumps(self.data, indent=4))
            
    def add(self):
        text, ok = QInputDialog.getText(self, 'Thêm con vật', 'Nhập tên con vật:')
        if ok and text:
            self.data["Danh_sach_thu"].append({"Ten thu": text})
            print(f"Added animal: {text}")
            self.save_data()
            self.update_list_widget()
        else:
            print("Add canceled or empty input")

    def edit(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            text, ok = QInputDialog.getText(self, 'Chỉnh sửa con vật', 'Chỉnh sửa tên con vật:', QLineEdit.EchoMode.Normal, current_item.text())
            if ok and text:
                index = self.list_widget.currentRow()
                self.data["Danh_sach_thu"][index]["Tên"] = text
                self.save_data()
                self.update_list_widget()
        else:
            self.msg_box.setText("Không có con vật nào được chọn để chỉnh sửa.")
            self.msg_box.exec()

    def delete(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Xác nhận")
            confirm_box.setIcon(QMessageBox.Icon.Question)
            confirm_box.setText("Bạn có chắc chắn muốn xóa con vật này?")
            confirm_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm_box.setDefaultButton(QMessageBox.StandardButton.No)

            result = confirm_box.exec()
            if result == QMessageBox.StandardButton.Yes:
                del self.data["Danh_sach_thu"][current_row]
                self.save_data()
                self.update_list_widget()
        else:
            self.msg_box.setText("Không có con vật nào được chọn để xóa.")
            self.msg_box.exec()

    def clear(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Hệ thống thông báo")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Hệ thống đang thông báo đến tổng giám đốc. Đang chờ tổng giám đốc đồng ý hoặc không đồng ý.")
        msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
        msg_box.exec()

        decision = random.choice(["Đồng ý", "Không đồng ý"])
        if decision == "Đồng ý":
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("Tổng giám đốc đã đồng ý. Toàn bộ thú sẽ biến mất.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.exec()
            self.data["Danh_sach_thu"] = []
            self.save_data()
            self.update_list_widget()
        else:
            confirm_box = QMessageBox()
            confirm_box.setWindowTitle("Thông báo")
            confirm_box.setIcon(QMessageBox.Icon.Information)
            confirm_box.setText("Tổng giám đốc không đồng ý. Danh sách thú sẽ được giữ nguyên.")
            confirm_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            confirm_box.exec()

    def search(self):
        text = self.search_bar.text().strip().lower()
        if text:
            keywords = text.split()
            for index in range(self.list_widget.count()):
                item = self.list_widget.item(index)
                item_text = item.text().lower()
                match = any(keyword in item_text for keyword in keywords)
                item.setHidden(not match)
        else:
            for index in range(self.list_widget.count()):
                item = self.list_widget.item(index)
                item.setHidden(False)

    def update_list_widget(self):
        self.list_widget.clear()
        for animal in self.data["Danh_sach_thu"]:
            self.list_widget.addItem(animal["Ten thu"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())