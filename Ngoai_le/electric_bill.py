print("---------------------===Tự luận - Câu 2===---------------------")

# Nhập lượng kWh tiêu thụ
kWh = float(input("Nhập lượng kWh tiêu thụ: "))

# Tính tiền điện
if kWh <= 50:
    tien_dien = kWh * 1678
elif kWh <= 100:
    tien_dien = 50 * 1678 + (kWh - 50) * 1734
elif kWh <= 200:
    tien_dien = 50 * 1678 + 50 * 1734 + (kWh - 100) * 2014
elif kWh <= 300:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kWh - 200) * 2536
elif kWh <= 400:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kWh - 300) * 2834
else:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kWh - 400) * 2927

print(f"Số tiền điện phải trả là: {tien_dien} đồng")