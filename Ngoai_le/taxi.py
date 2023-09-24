print("---------------------===cước taxi===---------------------")
# Giá cước bắt đầu
gio_mo_cua = 12000  

# Hỏi loại xe
loai_xe= int(input("Loại xe (1. 4 chỗ, 2. 7 chỗ): "))

if loai_xe == 1:
  # Giá xe 4 chỗ
  phi_1km = 8000
elif loai_xe == 2:
  # Giá xe 7 chỗ 
  phi_1km = 9000
else:
  print("Loại xe không hợp lệ")
  exit()

# Hỏi khoảng cách 
khoang_cach = float(input("Khoảng cách (km): "))

# Tính tiền
tien_cuoc = gio_mo_cua
if khoang_cach > 0:
  tien_cuoc += phi_1km * khoang_cach

# In kết quả
print("Tiền cước: ", tien_cuoc)