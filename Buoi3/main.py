#import thư viện math để làm các toán tử khó hơn
import math 

print("---------------------===Math library===---------------------")
print(math.sqrt(3))
print(math.cos(90))
print(math.sin(30))
print(math.tan(50))

print("---------------------===Information===---------------------")
#lấy tên người dùng từ input

name = input("Tên bạn là gì: ")
print("tên bạn là: ", name)


age = input("Tuổi: ")
print(f"Bạn {age} tuổi")


print("---------------------===Math===---------------------")
#phương trình bậc 1 - lấy từ người dùng qua lệnh input
a = int(input("vui lòng nhập giá trị biến a: "))
b = int(input("vui lòng nhập giá trị biến b: "))
c = int(input("vui lòng nhập giá trị biến c: "))
x = ( c - b ) / a

print("kết quả phương trình: ", a, "x + ", b, " = ", c)
print("x = ", x)



print("---------------------===Chu vi - Diện tích===---------------------")
#Tính chu vi hình tròn

# Nhập bán kính hình tròn
r = float(input("Nhập bán kính hình tròn: "))

# Hằng số pi
pi = 3.14

# Công thức tính chu vi - diện tích hình tròn
chu_vi_hinh_tron = 2 * pi * r
dien_tich_hinh_tron = r * r * pi

# Hiển thị kết quả
print("Chu vi hình tròn với bán kính =", r, "là:", chu_vi_hinh_tron)
print("Diện tích hình tròn với bán kính =", r, "là:", dien_tich_hinh_tron)

print("---------------------===Toán tử===---------------------")
#print ra các toán tử sẵn có trong python

print("Toán tử +, ví dụ: 50 + 50 = ", 50 + 50)
print("Toán tử -, ví dụ: 150 - 50 = ", 150 - 50)
print("Toán tử *, ví dụ: 50 x 2 = ", 50 * 2)
print("Toán tử /, ví dụ: 150 : 50 = ", 50 / 50)
print("Toán tử %, ví dụ: 7 % 3 = ", 7 % 3)
print("Toán tử //, ví dụ: 7 // 2 = ", 7 // 2)
print("Toán tử **, ví dụ: 5^2 = ", 5**2)

print("lưu ý: 2**(2**3)= ", 2**(2**3))

print("---------------------===Currency Converter===---------------------")

# mệnh giá 1 Đô la Mỹ -> Việt Nam Đồng
VietnamDong = 24000

Dollar = int(input("Vui lòng nhập tiền cần chuyển ( Đô la Mỹ ): "))
print("Sô tiền sẽ được quy đổi đang Việt Nam đồng ( VNĐ )")

# công thức quy đổi Đô la Mỹ -> Việt Nam Đồng
quy_doi = Dollar * VietnamDong

print( Dollar ,f"Đô la Mỹ quy đổi ra được: {quy_doi} VNĐ")