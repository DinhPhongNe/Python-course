#========== Phan trac nghiem
#Cau 1: C
#Cau 2: D
#Cau 3: C
#Cau 4: A
#Cau 5: A
#Cau 6: C
#Cau 7: B
#Cau 8: A
#Cau 9: C
#Cau 10: D 

#========== Phan thuc hanh
import sys
import json
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QPushButton, QMessageBox

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            'name': self.name,
            'priority': self.priority,
            'completed': self.completed
        }

class HomeworkList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_completed(self):
        completed = True
        for item in self.items:
            if not item.completed:
                completed = False
                print(item.name)
        if completed:
            print("All finished!")
    
    def to_list(self):
        return [item.to_dict() for item in self.items]

class HomeworkManagerDialog(QDialog):
    def __init__(self, hw_list):
        super().__init__()
        self.hw_list = hw_list
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Homework Manager")

        self.layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.export_button = QPushButton("Export Data")
        self.export_button.clicked.connect(self.export_data)
        self.layout.addWidget(self.export_button)

        self.setLayout(self.layout)

        self.populate_list()

    def populate_list(self):
        for hw in self.hw_list.items:
            self.list_widget.addItem(hw.name)

    def export_data(self):
        data = self.hw_list.to_list()
        with open('new_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        QMessageBox.information(self, "Thành công!", "Dữ liệu bài tập đã được thêm vào file new_data.json !")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    hw_list = HomeworkList()
    hw_list.add_item(Homework("Lap trinh App Producer", 3))
    hw_list.add_item(Homework("Lam van", 2, True))
    hw_list.add_item(Homework("Lap trinh GameMaker", 3))

    dialog = HomeworkManagerDialog(hw_list)
    dialog.show()

    sys.exit(app.exec())
