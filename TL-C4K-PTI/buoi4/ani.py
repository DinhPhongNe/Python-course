class Animals:
    def __init__(self, name, age, type, color):
        self.name = name
        self.age = age
        self.type = type
        self.color = color

    def get_info(self):
        print("Thông tin con vật:")
        print(f"Tên con vật: {self.name}")
        print(f"Tuổi: {self.age}")
        print(f"Giống loài: {self.type}")
        print(f"Màu lông: {self.color}")


animals = [
    Animals("Mèo", 2, "Chó", "Golden"),
    Animals("Chó", 1, "Mèo", "Cam"),
    Animals("Vẹt", 4, "Chim", "Xanh"),
    Animals("Voi", 3, "Động vật hoang dã", "Xám"),
]
