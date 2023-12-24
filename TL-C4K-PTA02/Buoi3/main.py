class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chu_vi = (width + height) * 2
        self.dien_tich = width * height

ABCD = Rectangle(200, 50)
print(f"Chu vi là {ABCD.chu_vi}")
print(f"Diện tích là {ABCD.dien_tich}")

#=====================================================================
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.type = self.determine_triangle_type()

    def determine_triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Tam giác đều"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Tam giác cân"
        elif self.side1**2 + self.side2**2 == self.side3**2 or self.side1**2 + self.side3**2 == self.side2**2 or self.side2**2 + self.side3**2 == self.side1**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        # Sử dụng công thức Heron để tính diện tích tam giác từ độ dài các cạnh
        s = self.calculate_perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

# Kiểm tra các loại tam giác và tính chu vi, diện tích
triangle1 = Triangle(3, 4, 5)
print("Tam giác 3-4-5:", triangle1.type)
print("Chu vi:", triangle1.calculate_perimeter())
print("Diện tích:", triangle1.calculate_area())

triangle2 = Triangle(5, 5, 5)
print("Tam giác 5-5-5:", triangle2.type)
print("Chu vi:", triangle2.calculate_perimeter())
print("Diện tích:", triangle2.calculate_area())

triangle3 = Triangle(5, 12, 13)
print("Tam giác 5-12-13:", triangle3.type)
print("Chu vi:", triangle3.calculate_perimeter())
print("Diện tích:", triangle3.calculate_area())

print("="*10)
#=====================================================================
#=====================================================================
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
class Teacher(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def teach(self):
        print(f"{self.name} is teaching.")

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def attend_class(self):
        print(f"{self.name} is attending class.")


# Sử dụng kế thừa trong chương trình điểm danh
teacher = Teacher("Mr. Thang", 35)
student1 = Student("Phong", 15)
student2 = Student("Ân", 16)
student3 = Student("Uyên", 16)

teacher.teach()
student1.attend_class()
student2.attend_class()
