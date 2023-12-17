class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
    
#dog0 = Dog("tên chó", tuổi, "màu chó") 
Dog1 = Dog("Chó 1", 3, "màu đen")
Dog2 = Dog("Chó 2", 6, "màu vàng")
Dog3 = Dog("Chó 3", 9, "màu trắnng")

#=================================================================

class Human:
    def __init__(self, name, age, gender, height, weight, birth, nationality ):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.birth = birth
        self.nationality = nationality

#Human0 = Human("name", age, "gender", "height", "weight", "birth", "nationality")
Human1 = Human("Dinh Phong", 13, "Male", "167cm", "70kg", "24/05", "Vietnam")

Human2 = Human("Nha Uyen", 13, "Female", "165cm", "50kg", "28/02", "Vietnam")
Human3 = Human("Thien An", 13, "Male", "163cm", "50kg", "12/07", "Vietnam")

Human4 = Human("Thanh Tuan", 13, "Male", "155cm", "50kg", "23/09", "Vietnam")
Human5 = Human("Ngoc Linh", 13, "Female", "156cm", "40kg", "13/05", "Vietnam")

#=================================================================

class Car:
    def __init__(self, make, model, year, color, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type

#Car0 = Car("make", "model", "year", "color", "fuel_type")
car1 = Car("Toyota", "Camry", 2022, "Blue", "Gasoline")
car2 = Car("Honda", "Accord", 2021, "Silver", "Hybrid")
car3 = Car("Ford", "Mustang", 2023, "Red", "Petrol")


class Motorbike:
    def __init__(self, make, model, year, color, engine_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
    
#Motorbike0 = Car("make", "model", "year", "color", "engine_type")   
motorbike1 = Motorbike("Harley-Davidson", "Street Glide", 2022, "Black", "V-twin")
motorbike2 = Motorbike("Yamaha", "YZF-R6", 2021, "Blue", "Inline-4")
motorbike3 = Motorbike("Ducati", "Monster", 2023, "Yellow", "V-twin")

class Bike:
    def __init__(self, brand, model, year, color, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.type = type

#Bike0 = Car("brand", "model", "year", "color", "type")
bike1 = Bike("Giant", "Escape", 2022, "Green", "Hybrid")
bike2 = Bike("Trek", "FX", 2021, "Black", "Road")
bike3 = Bike("Cannondale", "Synapse", 2023, "White", "Mountain")

#In ra từng cái
print("Cars:")
print(f"Car 1: {car1.make} {car1.model}")
print(f"Car 2: {car2.make} {car2.model}")
print(f"Car 3: {car3.make} {car3.model}")

print("\nMotorbikes:")
print(f"Motorbike 1: {motorbike1.make} {motorbike1.model}")
print(f"Motorbike 2: {motorbike2.make} {motorbike2.model}")
print(f"Motorbike 3: {motorbike3.make} {motorbike3.model}")

print("\nBikes:")
print(f"Bike 1: {bike1.brand} {bike1.model}")
print(f"Bike 2: {bike2.brand} {bike2.model}")
print(f"Bike 3: {bike3.brand} {bike3.model}")