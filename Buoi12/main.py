def absolute_value():
    number = int(input("Nhập 1 số nguyên: "))
    if number < 0:
        absolute = - number
    else:
        absolute = number
    print(f"giá trị tuyệt đối của số nguyên là: {absolute}")

absolute_value()

#================================================

def sum_even_numbers():
    n = int(input("Nhập nguyên dương n: "))
    sum_even = 0
    for num in range(2, n+1, 2):
        sum_even += num
    print(f"tổng số chẵn từ 1 đến {n} là {sum_even}")

sum_even_numbers()

#================================================

def insert_information(ten, tuoi, ngay_sinh, noi_o):
    print("Thông tin cá nhân:")
    print("Tên:", ten)
    print("Tuổi:", tuoi)
    print("Ngày sinh:", ngay_sinh)
    print("Nơi ở:", noi_o)


ten = input("Nhập tên của bạn: ")
tuoi = input("nhập tuổi của bạn: ")
ngay_sinh = input("Nhập ngày sinh của bạn: ")
noi_o = input("nhập nơi ở của bạn: ")
print("="*10)
insert_information(ten, tuoi, ngay_sinh, noi_o)

#================================================

def insert_list(danh_sach):
    print("Danh sách các phân tử")
    for so in danh_sach:
        print(so)
        
    tong = sum(danh_sach)
    print(f"tổng của danh sách: {tong}")
    
danh_sach = []
n = int(input("nhập số phần tử trong danh sách: "))
for i in range(n):
    so = int(input("Nhập phân tử thứ {}:".format(i + 1)))
    danh_sach.append(so)
    
insert_list(danh_sach)

#================================================

def summary(a,b):
    tong = 0
    for i in range(a, b + 1):
        tong += i
    print(f"tổng từ {a} đến {b}: {tong}")
    
n = int(input("nhập 1 số nguyên dương: "))
summary(1, n)
summary(1, n/2)
summary(n//2, n)