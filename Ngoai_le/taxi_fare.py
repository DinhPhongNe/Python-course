loai_xe = int(input("nhập loại xe: "))
so_km = float(input("Nhập số km: "))
waiting = int(input("Nhập thời gian chờ: "))
tien_cho = 0
tien_diChuyen = 0

if waiting > 5:
    tien_cho=(waiting - 5)*750
if loai_xe == 4:
    if so_km < 0.5:
        tien_diChuyen = 11000
    elif 0.5 < so_km < 30:
        tien_diChuyen = int(11000+(so_km*17600))
    else:
        tien_diChuyen = int(11000 + 29.5 * 17600 + (so_km - 30)*14500)
elif loai_xe == 7 and so_km < 0.5:
    tien_diChuyen = 12500
    if 0.5 < so_km < 30:
        tien_diChuyen = int(12000+(so_km*19600))
    else:
        tien_diChuyen = int(12000 + 29.5 * 19600+(so_km -30)*17100)
else:
    print("loại xe không phù hợp")
    
tong_tien = tien_cho + tien_diChuyen

print(f"Tổng tiền: {tong_tien} VND")