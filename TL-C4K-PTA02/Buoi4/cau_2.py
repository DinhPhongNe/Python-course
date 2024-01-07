class HocSinh:
    def __init__(self, ho_ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi

    def cap_nhat_chieu_cao_can_nang(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi

    def xuat_thong_tin(self):
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Chiều cao: {self.chieu_cao} cm")
        print(f"Cân nặng: {self.can_nang} kg")
        print(f"Học lực: {self.hoc_luc}")

hs = HocSinh("Dinh Phong", "Thành phố Hồ Chí Minh", 170, 60, "Giỏi")
hs.xuat_thong_tin()

print("===Cập nhật lại thông tin===")
hs.cap_nhat_dia_chi("dưới lòng đất")
hs.cap_nhat_chieu_cao_can_nang(175, 65)
hs.xuat_thong_tin()
