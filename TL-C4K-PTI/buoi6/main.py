import json
import os
print(os.getcwd())


# Class definition
class Me:
    def __init__(self, name, age, gender, hobbies):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobbies = hobbies

# Đọc dữ liệu từ tệp JSON
with open('C:/Users/PC/Desktop/Python-course/TL-C4K-PTI/buoi6/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Tạo một đối tượng của lớp Me với dữ liệu từ JSON
me_instance = Me(data[0]["Name"], data[0]["Age"], data[0]["Gender"], data[0]["Hobbies"])


# In thông tin ra màn hình
print(f"Name: {me_instance.name}")
print(f"Age: {me_instance.age}")
print(f"Gender: {me_instance.gender}")
print(f"Hobbies: {', '.join(me_instance.hobbies)}")