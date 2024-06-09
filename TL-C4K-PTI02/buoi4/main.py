from ani import Animals, animals


def find_animal(name):
    for animal in animals:
        if animal.name.lower() == name.lower():
            return animal
    return None


def add_animal():
    name = input("Nhập tên con vật: ")
    age = int(input("Nhập tuổi con vật: "))
    animal_type = input("Nhập giống loài con vật: ")
    color = input("Nhập màu lông con vật: ")

    new_animal = Animals(name, age, animal_type, color)
    animals.append(new_animal)
    print(f"Con vật '{name}' được thêm thành công.")


def remove_animal(name):
    animal = find_animal(name)
    if animal:
        animals.remove(animal)
        print(f"Con vật '{name}' xóa thành công.")
    else:
        print(f"Con vật '{name}' không tồn tại trong hệ thống để xóa.")


def main():
    while True:
        print("\nAnimal Management System")
        print("1. Tìm con vật")
        print("2. Thêm con vật")
        print("3. Xóa con vật")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == "1":
            animal_name = input("Nhập tên con vật bạn muốn tìm kiếm: ")
            animal = find_animal(animal_name)

            if animal:
                print(f"Tìm thấy con vật")
                animal.get_info()
            else:
                print(f"Con vật không có trong hệ thống.")

        elif choice == "2":
            add_animal()

        elif choice == "3":
            animal_name = input("Nhập tên con vật bạn muốn xóa: ")
            remove_animal(animal_name)

        elif choice == "4":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không phù hợp, hãy chọn lại.")


if __name__ == "__main__":
    main()
