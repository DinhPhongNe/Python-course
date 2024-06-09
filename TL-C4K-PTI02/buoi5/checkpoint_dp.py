# ===-- Trac Nghiem --===
# Cau 1: D
# Cau 2: C
# Cau 3: B
# Cau 4: B
# Cau 5: C
# Cau 6: B
# Cau 7: A
# Cau 8: D
# Cau 9: B
# Cau 10: D
  
# ===-- Tu Luan --===

import json
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

    def do_quan_trong(self):
        if self.priority == 1:
            return "Thấp"
        elif self.priority == 2:
            return "Trung bình"
        elif self.priority == 3:
            return "Cao"
        else:
            return "Không xác định"

    def status(self):
        return "Đã hoàn thành" if self.completed else "Chưa hoàn thành"

    def to_dict(self):
        return {
            'name': self.name,
            'priority': self.priority,
            'completed': self.completed
        }

class HomeworkList:
    def __init__(self):
        self.items = []

    def add_homework(self, item):
        self.items.append(item)

    def to_list(self):
        return [item.to_dict() for item in self.items]

    def all_finished(self):
        unfinished_homeworks = [homework.name for homework in self.items if not homework.completed]
        if unfinished_homeworks:
            print("Các bài tập chưa hoàn thành còn lại:")
            for homework_name in unfinished_homeworks:
                print(homework_name)
        else:
            print("All finished")
