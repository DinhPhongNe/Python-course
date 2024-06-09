# == PHAN TRAC NGHIEM ==
# cau 1: A
# cau 2: B
# cau 3: A
# cau 4: D
# cau 5: C


# == PHAN TU LUAN ==
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} kêu {self.sound}")

animals = [
    Animal("Sư tử", "Có vú", "gầm gừ"),
    Animal("Bò sát", "Bò sát", "ríu ríu"),
    Animal("Cá heo", "Có vú", "tiếng huýt sáo"),
    Animal("Chó", "Có vú", "gâu gâu")
]

for animal in animals:
    print(f"Tên: {animal.name}")
    print(f"Loài: {animal.species}")
    print(f"Âm thanh: {animal.sound}")
    animal.make_sound()
    print("-------------------------")
