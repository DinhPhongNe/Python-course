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

class HomeworkList:
    def __init__(self):
        self.items = []

    def add_homework(self, item):
        self.items.append(item)

    def all_finished(self):
        unfinished_homeworks = [homework.name for homework in self.items if not homework.completed]
        if unfinished_homeworks:
            print("Các bài tập chưa hoàn thành còn lại:")
            for homework_name in unfinished_homeworks:
                print(homework_name)
        else:
            print("All finished")

# Thang mức độ quan trọng
# 1 - mức độ quan trọng thấp
# 2 - mức độ quan trọng trung bình
# 3 - mức độ quan trọng cao
#------------------------------------
homework1 = Homework("cắt dán", 1)
homework2 = Homework("làm văn", 3)
homework3 = Homework("làm toán", 3, True) # => test nếu True
homework4 = Homework("Lập trình Gamemaker", 1, True)
homework5 = Homework("Lập trình App Producer", 3)
homework6 = Homework("Đi ngủ", 4, True)  # => test nếu mức độ quan trọng trên 3


homework_list = HomeworkList()
homework_list.add_homework(homework1)
homework_list.add_homework(homework2)
homework_list.add_homework(homework3)
homework_list.add_homework(homework4)
homework_list.add_homework(homework5)
homework_list.add_homework(homework6)

# In danh sách bài tập
for homework in homework_list.items:
    print(f"Bài tập: {homework.name} \nMức độ quan trọng: {homework.do_quan_trong()} \nHoàn thành: {homework.status()} \n-----------------")

homework_list.all_finished()