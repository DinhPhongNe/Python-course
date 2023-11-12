# Nhập thông tin từ người dùng
thu_nhap = float(input("Nhập tổng thu nhập trong năm: "))
nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc: "))

# Tính số tiền giảm trừ
muc_giam_tru = 11 * 12  # 11 triệu đồng mỗi tháng
tien_giam_tru_nguoi_phu_thuoc = 4.4 * nguoi_phu_thuoc * 12  # 4.4 triệu đồng mỗi người phụ thuộc mỗi tháng
tien_giam_tru = muc_giam_tru + tien_giam_tru_nguoi_phu_thuoc

# Tính thu nhập tính thuế (TNTT)
thu_nhap_tinh_thue = thu_nhap - tien_giam_tru

# Tính thuế theo bậc thuế
if thu_nhap_tinh_thue <= 5:
    thue_suat = 0.05
    tien_thue = thu_nhap_tinh_thue * thue_suat
elif thu_nhap_tinh_thue <= 10:
    thue_suat = 0.1
    tien_thue = thu_nhap_tinh_thue * thue_suat
elif thu_nhap_tinh_thue <= 18:
    thue_suat = 0.15
    tien_thue = thu_nhap_tinh_thue * thue_suat
elif thu_nhap_tinh_thue <= 32:
    thue_suat = 0.2
    tien_thue = thu_nhap_tinh_thue * thue_suat
elif thu_nhap_tinh_thue <= 52:
    thue_suat = 0.25
    tien_thue = thu_nhap_tinh_thue * thue_suat
elif thu_nhap_tinh_thue <= 80:
    thue_suat = 0.3
    tien_thue = thu_nhap_tinh_thue * thue_suat
else:
    thue_suat = 0.35
    tien_thue = thu_nhap_tinh_thue * thue_suat

# làm tròn các kết quả, dùng hàm round()
tien_giam_tru = int(round(tien_giam_tru))
thu_nhap_tinh_thue = int(round(thu_nhap_tinh_thue))
tien_thue = int(round(tien_thue))

# Xuất kết quả
print("--------------------------------------")
print(f"Số tiền giảm trừ: {tien_giam_tru} triệu đồng")
print(f"Số tiền chịu thuế: {thu_nhap_tinh_thue} triệu đồng")
print(f"Tiền thuế: {tien_thue} triệu đồng")