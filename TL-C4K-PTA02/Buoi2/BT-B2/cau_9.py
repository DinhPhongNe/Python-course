class QuanLyDiemHS:
    def __init__(self, ho_ten, lop, truong, diem_toan, diem_van, diem_anh):
        self.HoTen = ho_ten
        self.Lop = lop
        self.Truong = truong
        self.DiemToan = diem_toan
        self.DiemVan = diem_van
        self.DiemAnh = diem_anh

    def diem_trung_binh(self):
        return (self.DiemToan + self.DiemVan + self.DiemAnh) / 3

# Tạo đối tượng cho 3 học sinh
hs1 = QuanLyDiemHS("Nguyen Van A", "10A", "Truong A", 8.5, 7.5, 9.0)
hs2 = QuanLyDiemHS("Tran Thi B", "10B", "Truong A", 9.0, 8.0, 8.5)
hs3 = QuanLyDiemHS("Le Van C", "10C", "Truong B", 8.0, 9.0, 8.5)

# Tạo danh sách học sinh
danh_sach_hoc_sinh = [hs1, hs2, hs3]

# Tìm điểm trung bình cao nhất
diem_trung_binh_cao_nhat = max(hs.diem_trung_binh() for hs in danh_sach_hoc_sinh)

# In ra thông tin học sinh có điểm trung bình cao nhất
print("Thông tin học sinh có điểm trung bình cao nhất:")
for hs in danh_sach_hoc_sinh:
    if hs.diem_trung_binh() == diem_trung_binh_cao_nhat:
        print(f"Tên: {hs.HoTen}, Lớp: {hs.Lop}, Trường: {hs.Truong}, Điểm TB: {hs.diem_trung_binh()}")

# In ra thông tin các học sinh có điểm trung bình bằng nhau
print("\nThông tin các học sinh có điểm trung bình bằng nhau:")
for hs in danh_sach_hoc_sinh:
    if hs.diem_trung_binh() == diem_trung_binh_cao_nhat:
        print(f"Tên: {hs.HoTen}, Lớp: {hs.Lop}, Trường: {hs.Truong}, Điểm TB: {hs.diem_trung_binh()}")
