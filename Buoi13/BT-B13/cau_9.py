def tinh_trung_binh_diem(diem):
    if len(diem) == 0:
        return 0.0

    tong_diem = sum(diem)
    trung_binh = tong_diem / len(diem)
    return trung_binh

def tim_diem_lon_thu_hai(diem):
    if len(diem) < 2:
        return None

    diem_sap_xep = sorted(diem, reverse=True)
    return diem_sap_xep[1]

def kiem_tra_diem_duoi_trung_binh(diem):
    trung_binh = tinh_trung_binh_diem(diem)
    for diem_mon in diem:
        if diem_mon < trung_binh:
            return True
    return False

def cai_thien_diem_duoi_sau_sau(diem):
    diem_cai_thien = [diem_mon if diem_mon >= 6 else 6 for diem_mon in diem]
    return diem_cai_thien

# Khởi tạo danh sách điểm môn Tin học của An
diem = [7, 8, 6, 4, 9, 7]

# Tính trung bình điểm Tin học
trung_binh = tinh_trung_binh_diem(diem)
print(f"Trung bình điểm Tin học {round(trung_binh)}") # -> dùng round để làm tròn, dtb ra 6.8333333333333333.. nhìn nó kì lắm:))))

# Tìm điểm lớn thứ hai trong danh sách
diem_lon_thu_hai = tim_diem_lon_thu_hai(diem)
print(f"Điểm lớn thứ hai: {diem_lon_thu_hai}")

# Kiểm tra danh sách điểm có điểm dưới trung bình hay không
co_diem_duoi_trung_binh = kiem_tra_diem_duoi_trung_binh(diem)
if co_diem_duoi_trung_binh:
    print("Có điểm dưới trung bình.")
else:
    print("Không có điểm dưới trung bình.")

# Cải thiện các điểm dưới 6 thành 6
diem_cai_thien = cai_thien_diem_duoi_sau_sau(diem)
print(f"Danh sách điểm sau khi cải thiện: {diem_cai_thien}")