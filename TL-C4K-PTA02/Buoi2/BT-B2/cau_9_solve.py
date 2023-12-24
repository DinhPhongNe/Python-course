class Student:
    def __init__(self, ho_ten, lop, truong, diem_toan, diem_van, diem_anh):
        self.ho_ten = ho_ten
        self.lop = lop
        self.truong = truong
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_anh = diem_anh
        self.diem_trung_binh = (diem_toan + diem_anh + diem_van) / 3


student1 = Student("Minh", "PTA02", "MindX", 8, 9, 10)
print(student1.diem_trung_binh)