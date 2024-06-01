import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QPushButton, QListWidget, QInputDialog
from PyQt6 import uic

class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("main.ui", self)
        
        self.Add.clicked.connect(self.add)
        self.Edit.clicked.connect(self.edit)
        self.Delete.clicked.connect(self.delete)
        self.Search_btn.clicked.connect(self.search)
        
        self.list_widget = self.findChild(QListWidget, "listWidget")
        self.search_bar = self.findChild(QLineEdit, "Search_bar")
        
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("Lỗi")
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
        
    def add(self):
        text, ok = QInputDialog.getText(self, 'Add Item', 'Enter item:')
        if ok and text:
            self.list_widget.addItem(text)
        
    def edit(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            text, ok = QInputDialog.getText(self, 'Edit Item', 'Edit item:', QLineEdit.EchoMode.Normal, current_item.text())
            if ok and text:
                current_item.setText(text)
        else:
            self.msg_box.setText("No item selected to edit.")
            self.msg_box.exec()
    
    def delete(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            self.list_widget.takeItem(current_row)
        else:
            self.msg_box.setText("No item selected to delete.")
            self.msg_box.exec()
    
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

