print("---------------------===Hệ thống book xe con - xe buýt===---------------------")

print("---------------------===Chào mừng đến hệ thống đặt xe con - xe buýt===---------------------")

# Bảng giá các loại xe
print("BẢNG GIÁ CÁC LOẠI XE")
xe = {'Xe 4 chỗ': 100000, 'Xe 5 chỗ': 150000, 'Xe 7 chỗ': 300000, 
      'Xe 16 chỗ': 450000, 'Xe 25 chỗ': 550000, 'Xe 50 chỗ': 600000,  
      'Xe giường nằm': 700000, 'Xe giường nằm VIP': 750000}
for k,v in xe.items():
  print(k, v, "VND/người")
  
# Bảng giá vali      
print("\nBẢNG GIÁ VÉ VẬN CHUYỂN VALI")  
vali = {1:10000, 2:20000, 3:30000, 4:50000, 5:75000, 6:90000, 
         7:120000, 8:150000, 9:160000, 10:170000}
for k,v in vali.items():
  print(k, "kg -", v, "VND")
  
# Nhập thông tin chuyến đi
loai_xe = int(input("Loại xe: "))
so_nguoi = int(input("Số người: ")) 
so_kg_vali = int(input("Số kg vali: "))

# Tính giá 
gia_xe = loai_xe*so_nguoi

if so_kg_vali <= 10:
  gia_vali = vali[so_kg_vali]
else: 
  gia_vali = 170000

tong_gia = gia_xe + gia_vali

# In kết quả  
print("Tổng giá:", tong_gia, "VND")