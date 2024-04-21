class STUDENT:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class STUDENT_MANAGER:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_name):
        self.students = [s for s in self.students if s.name != student_name]

    def change_student_info(self, student_name, new_age, new_gender):
        for student in self.students:
            if student.name == student_name:
                student.age = new_age
                student.gender = new_gender
                break

    def print_students(self):
        for student in self.students:
            print(f"Tên: {student.name} \n Tuổi: {student.age} \n Giới tính: {student.gender} \n===---===")

# Example usage
student_manager = STUDENT_MANAGER()

# Add some students
student_manager.add_student(STUDENT("Phong", 14, "Nam"))
student_manager.add_student(STUDENT("Tuấn", 14, "Nam"))
student_manager.add_student(STUDENT("Ân", 14, "Nam"))
student_manager.add_student(STUDENT("Uyên", 14, "Nữ"))
student_manager.add_student(STUDENT("Nhi", 14, "Nữ"))
student_manager.add_student(STUDENT("Nghĩa", 14, "Nam"))
student_manager.add_student(STUDENT("Nam Phong", 14, "Nam"))

print("==--IN RA DANH SÁCH HỌC SINH--==")
student_manager.print_students()

print("==--XÓA 1 HỌC SINH--==")
student_manager.remove_student("Nam Phong")
student_manager.print_students()

print("==--THAY ĐỔI THÔNG TIN 1 HỌC SINH--==")
student_manager.change_student_info("Phong", 99999999, "Nam")
student_manager.print_students()










students = ["A", "B", "C", "D", "E", "F"]

# for student in students:
#     print(student)
    
#sort: sắp xếp theo thứ tự tăng dần, nếu khai báo reverse=True thì sẽ theo thứ tự tăng dần
students.sort(reverse=True)
print(students)

students.sort(reverse=False)
print(students)


#append: thêm vô list ( cuối danh sách )
students.append("G")
print(students)

#insert: thêm vô list vị trí bất kì ( vị trí phải hợp lệ)
students.insert(1, "H")
print(students)

#xóa ở vị trí bất kỳ, không vị trí thì mặc định thằng cuối cút
students.pop(0)
print(students)

#remove: xóa theo giá trị phần tử trong danh sách
if "F" in students:
    students.remove("F")

#clear: cút hết
students.clear()
print(students)



