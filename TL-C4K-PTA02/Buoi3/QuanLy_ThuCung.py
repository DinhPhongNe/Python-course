class ThuCung:
    def __init__(self, ten, giong, mau_sac, tuoi, can_nang):
        self.ten = ten
        self.giong = giong
        self.mau_sac = mau_sac
        self.tuoi = tuoi
        self.can_nang = can_nang

    def xuat_thong_tin(self):
        print(f"Tên: {self.ten}")
        print(f"Giống loài: {self.giong}")
        print(f"Màu sắc: {self.mau_sac}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Cân nặng: {self.can_nang}")

class Cho(ThuCung):
    def __init__(self, ten, mau_sac, tuoi, can_nang, vaccine):
        super().__init__(ten, "Chó", mau_sac, tuoi, can_nang)
        self.vaccine = vaccine

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        if self.vaccine:
            print("Đã tiêm vaccine")
        else:
            print("Chưa tiêm vaccine")


class Meo(ThuCung):
    def __init__(self, ten, mau_sac, tuoi, can_nang, vaccine):
        super().__init__(ten, "Mèo", mau_sac, tuoi, can_nang)
        self.vaccine = vaccine

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        if self.vaccine:
            print("Đã tiêm vaccine")
        else:
            print("Chưa tiêm vaccine")

class ThuCungCoVaccine(ThuCung):
    def __init__(self, ten, giong, mau_sac, tuoi, can_nang, vaccine):
        super().__init__(ten, giong, mau_sac, tuoi, can_nang)
        self.vaccine = vaccine

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        if self.vaccine:
            print("Đã tiêm vaccine")
        else:
            print("Chưa tiêm vaccine")

    def doi_mau_long(self, mau_moi):
        self.mau_sac = mau_moi


# Sử dụng lớp Cho và Meo
cho = Cho("Mèo", "Đen", 5, 15, True)
meo = Meo("Chó", "Trắng", 3, 10, False)

# In ra thông tin của chó và mèo
print("Thông tin của chó:")
cho.xuat_thong_tin()
print("=" * 10)
print("Thông tin của mèo:")
meo.xuat_thong_tin()
