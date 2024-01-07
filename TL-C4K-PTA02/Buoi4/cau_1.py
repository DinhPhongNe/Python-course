class HinhVuong:
    def __init__(self, canh):
        self.canh = canh

    def tinh_chu_vi(self):
        return 4 * self.canh

canh_hinh_vuong = float(input("Nhập độ dài cạnh của hình vuông: "))
hinh_vuong = HinhVuong(canh_hinh_vuong)
print(f"Chu vi của hình vuông là: {hinh_vuong.tinh_chu_vi()}")
