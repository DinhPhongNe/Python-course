# Phần trắc nghiệm
# Câu 1: B
# Câu 2: C
# Câu 3: C
# Câu 4: A
# Câu 5: C



# phần tự luận
class Animal:
    def __init__(self, name, species, age, color, birth, gender):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.birth = birth
        self.gender = gender

    def __str__(self):
        return f" Tên: {self.name} \n Giống loài: {self.species} \n {self.age} tuổi \n Màu lông: {self.color} \n Ngày sinh: {self.birth} \n Giới tính: {self.gender} \n ------------------"

animals = [
    Animal("Mèo", "Chó", 2, "Đen", "20/11/2022", "Đực"),
    Animal("Chó", "Mèo", 1, "Trắng", "01/01/2023", "Cái"),
    Animal("Ngáo", "Husky", 3, "Trắng - Đen", "10/07/2021", "Đực"),
    Animal("Hổ", "Sư tử", 3, "Vàng", "12/05/2021", "Đực"),
    Animal("Bình", "Chuột hamster", 0.5, "không biết", "01/12/2023", "Cái")
]

def sort_zoo(animals):
    animals.sort(key=lambda animal: animal.name, reverse=False)
    print("\nDanh sách động vật sau khi sắp xếp:")
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

def add_animal():
    name = input("Nhập tên động vật: ")
    species = input("Nhập loài: ")
    age = input("Nhập tuổi: ")
    color = input("Nhập màu lông: ")
    birth = input("Nhập ngày sinh ( dd/mm/yyyy ): ")
    gender = input("Nhập giới tính ( đực/cái ): ")
    animals.append(Animal(name, species, age, color, birth, gender))
    print(f"Đã thêm động vật {name} vào danh sách.")

def update_animal():
    name = input("Nhập tên động vật cần cập nhật: ")
    for animal in animals:
        if animal.name == name:
            species = input("Nhập loài mới: ")
            age = input("Nhập tuổi mới: ")
            color = input("Nhập màu sắc mới: ")
            print("Màu lông - ngày sinh - giới tính là những dữ liệu không thể thay đổi")
            animal.species = species
            animal.age = age
            animal.color = color
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
    print("1. Sắp xếp danh sách động vật")
    print("2. Tìm kiếm động vật")
    print("3. Thêm động vật")
    print("4. Cập nhật thông tin động vật")
    print("5. Xóa động vật")
    print("6. Hiển thị danh sách động vật")
    print("7. Thoát")
    
    choice = input("Chọn chức năng (1/2/3/4/5/6/7): ")

    if choice == "1":
        sort_zoo(animals)
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
        break
    else:
        print("Chọn không hợp lệ. Vui lòng chọn lại.")
