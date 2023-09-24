print("---------------------===phân chia tháng===---------------------")

# Nhập tháng muốn kiểm tra từ người dùng
month = int(input("Nhập tháng (1-12): "))

# Kiểm tra số ngày của từng tháng
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  print(f"tháng {month} có 31 ngày")
elif month == 4 or month == 6 or month == 9 or month == 11:
  print(f"tháng {month} có 30 ngày")  
elif month == 2:
  print(f"tháng 2{month} có 28 hoặc 29 ngày (tùy năm nhuận)")
else:
  print("Không phải là tháng trong năm")