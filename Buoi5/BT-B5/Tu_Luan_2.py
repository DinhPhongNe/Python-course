print("---------------------===Tự luận - Câu 2===---------------------")

# Nhập lượng kWh tiêu thụ
kWh = float(input("Nhập lượng kWh tiêu thụ: "))

# Tính tiền điện
if kWh < 50:
  tien_dien = kWh * 1700
elif kWh <= 100:
  tien_dien = 50 * 1700 + (kWh - 50) * 1900  
elif kWh <= 200: 
  tien_dien = 50 * 1700 + 50 * 1900 + (kWh - 100) * 2100
else:
  tien_dien = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kWh - 200) * 3000
  
print(f"Số tiền điện phải trả là: {tien_dien} đồng")