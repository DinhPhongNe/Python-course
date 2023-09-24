print("---------------------===điểm trung bình===---------------------")

diem_tong_ket = float(input("Nhập điểm trung bình năm của bạn: "))

if diem_tong_ket < 5:
    print(f"với số điểm {diem_tong_ket}, bạn được danh hiệu học sinh yến")
elif diem_tong_ket >= 5 and diem_tong_ket < 6:
    print (f"với số điểm {diem_tong_ket}, bạn được danh hiệu học sinh trung bình")
elif diem_tong_ket >= 6 and diem_tong_ket < 7:
    print (f"với số điểm {diem_tong_ket}, bạn được danh hiệu học sinh khá")
elif diem_tong_ket >= 7 and diem_tong_ket < 8:
    print (f"với số điểm {diem_tong_ket}, bạn được danh hiệu học sinh giỏi")
else:
    print (f"với số điểm {diem_tong_ket}, bạn được danh hiệu học sinh xuất sắc")