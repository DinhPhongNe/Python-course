#_______TRAC NGHIEM_______
#CAU 1: B
#CAU 2: B
#CAU 3: D
#CAU 4: D
#CAU 5: B




#_______TU LUAN_______
import sys
import random
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
        
        self.welcome_message()
        
    def welcome_message(self):
        welcome_box = QMessageBox()
        welcome_box.setWindowTitle("Chào mừng")
        welcome_box.setIcon(QMessageBox.Icon.Information)
        welcome_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
        welcome_box.setText("Chào mừng đến với sở thú")
        welcome_box.exec()
        
    def add(self):
        text, ok = QInputDialog.getText(self, 'Thêm con vật', 'Nhập tên con vật:')
        if ok and text:
            self.list_widget.addItem(text)
        
    def edit(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            text, ok = QInputDialog.getText(self, 'Chỉnh sửa con vật', 'Chỉnh sửa tên con vật:', QLineEdit.EchoMode.Normal, current_item.text())
            if ok and text:
                current_item.setText(text)
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
                self.list_widget.takeItem(current_row)
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
            self.list_widget.clear()
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
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
