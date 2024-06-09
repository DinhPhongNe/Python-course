#== TRẮC NGHIỆM ==
# cau 1: C
# cau 2: B
# cau 3: B
# cau 4: C
# cau 5: D


import json

class Animal:
    def __init__(self, name, species, age, color, birth, gender, weight):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.birth = birth
        self.gender = gender
        self.weight = weight

    def __str__(self):
        return f" Tên: {self.name} \n Giống loài: {self.species} \n {self.age} tuổi \n Màu lông: {self.color} \n Ngày sinh: {self.birth} \n Giới tính: {self.gender} \n Cân nặng: {self.weight} kg \n ------------------"

animals = [
    Animal("Mèo", "Chó", 2, "Đen", "20/11/2022", "Đực", 5),
    Animal("Chó", "Mèo", 1, "Trắng", "01/01/2023", "Cái", 4.5),
    Animal("Ngáo", "Husky", 3, "Trắng - Đen", "10/07/2021", "Đực", 20),
    Animal("Hổ", "Sư tử", 3, "Vàng", "12/05/2021", "Đực", 50),
    Animal("Bình", "Chuột hamster", 0.5, "không biết", "01/12/2023", "Cái", 0.2)
]

def sort_by_weight(animals):
    animals.sort(key=lambda animal: animal.weight, reverse=True)
    print("\nDanh sách động vật sau khi sắp xếp theo cân nặng:")
    for animal in animals:
        print(animal)
        
def sort_by_name(animals):
    animals.sort(key=lambda animal: animal.name)
    print("\nDanh sách động vật sau khi sắp xếp theo tên:")
    for animal in animals:
        print(animal)

def sort_zoo(animals):
    animals.sort(key=lambda animal: animal.name, reverse=False)
    print("\nDanh sách động vật sau khi sắp xếp:")
    for animal in animals:
        print(animal)
        
def sort_by_weight(animals):
    animals.sort(key=lambda animal: animal.weight, reverse=False)
    print("\nDanh sách động vật sau khi sắp xếp theo cân nặng:")
    for animal in animals:
        print(animal)

def filter_zoo(begin):
    filtered_animals = [animal for animal in animals if animal.name.startswith(begin)]
    if filtered_animals:
        print(f"\nĐộng vật bắt đầu bằng chữ cái '{begin}' là:")
        for animal in filtered_animals:
            print(animal)
    else:
        print(f"\nKhông có động vật nào bắt đầu bằng chữ cái '{begin}'.")

def save_to_json(animals, filename):
    animals.sort(key=lambda animal: animal.weight, reverse=True)
    print("\nDanh sách động vật sau khi sắp xếp theo cân nặng (từ cao xuống thấp):")
    for animal in animals:
        print(animal)
    if not filename.endswith(".json"):
        filename += ".json"
    data = [{"Tên": animal.name, "Cân nặng": animal.weight} for animal in animals]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print(f"Dữ liệu đã được lưu vào tệp {filename}.")


def add_animal():
    name = input("Nhập tên động vật: ")
    species = input("Nhập loài: ")
    age = input("Nhập tuổi: ")
    color = input("Nhập màu lông: ")
    birth = input("Nhập ngày sinh (dd/mm/yyyy): ")
    gender = input("Nhập giới tính (đực/cái): ")
    weight = float(input("Nhập cân nặng (kg): "))
    animals.append(Animal(name, species, age, color, birth, gender, weight))
    print(f"Đã thêm động vật {name} vào danh sách.")

def update_animal():
    name = input("Nhập tên động vật cần cập nhật: ")
    for animal in animals:
        if animal.name == name:
            species = input("Nhập loài mới: ")
            age = input("Nhập tuổi mới: ")
            color = input("Nhập màu sắc mới: ")
            weight = float(input("Nhập cân nặng mới (kg): "))
            print("Màu lông - ngày sinh - giới tính là những dữ liệu không thể thay đổi")
            animal.species = species
            animal.age = age
            animal.color = color
            animal.weight = weight
            print(f"Đã cập nhật thông tin cho động vật {name}.")
            return
    print(f"Không tìm thấy động vật có tên {name} trong danh sách.")

def delete_animal():
    name = input("Nhập tên động vật cần xóa: ")
    for animal in animals:
        if animal.name == name:
            animals.remove(animal)
            print(f"Đã xóa động vật {name} khỏi danh sách.")
            return
    print(f"Không tìm thấy động vật có tên {name} trong danh sách.")


while True:
    print("\nMenu:")
    print("1. Sắp xếp danh sách động vật theo tên")
    print("2. Tìm kiếm động vật")
    print("3. Thêm động vật")
    print("4. Cập nhật thông tin động vật")
    print("5. Xóa động vật")
    print("6. Hiển thị danh sách động vật")
    print("7. Sắp xếp danh sách động vật theo cân nặng")
    print("8. Lưu danh sách động vật vào file JSON")
    print("9. Thoát")
    
    choice = input("Chọn chức năng (1/2/3/4/5/6/7/8/9): ")

    if choice == "1":
        sort_by_name(animals)
    elif choice == "2":
        begin = input("Nhập chữ cái đầu tiên của tên động vật cần tìm: ")
        filter_zoo(begin)
    elif choice == "3":
        add_animal()
    elif choice == "4":
        update_animal()
    elif choice == "5":
        delete_animal()
    elif choice == "6":
        sort_zoo(animals)
    elif choice == "7":
        sort_by_weight(animals)
    elif choice == "8":
        filename = input("Nhập tên tệp JSON: ")
        save_to_json(animals, filename)
    elif choice == "9":
        break
    else:
        print("Chọn không hợp lệ. Vui lòng chọn lại.")
