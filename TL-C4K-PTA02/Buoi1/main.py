import random

# ôn  tập bài cũ - chả có gì=)))

# ôn 1 - cơ bản
a1 = "bool"
a2 = False
c = 1 + 2
d = 1.3
print(type(c))
print(type(a1))
print(type(a2))
print(type(d))



#-----------------------------------------------------------------------------------
print("="*10)
#ôn 2 - toán tử - nhập/xuất

plus = 10 + 20
minus = 100 - 7.33
time = 100 * 39.39
division = 100 / 39.39
mod = 100 % 39.39
chia_nguyen = 7 // 3
exponential = 7**3


#result of division without round(): 2.538715410002539
#result of division with round(): 3

print(f"Phép cộng: {plus}")
print(f"Phép trừ: {minus}")
print(f"Phép nhân: {time}")
print(f"Phép chia không round: {division}")
print(f"Phép chia với round: {round(division)}")
print(f"Phép chia lấy dư: {mod}")
print(f"Phép chia lấy nguyên: {chia_nguyen}")
print(f"Phép lũy thừa: {exponential}")

exponential_input = float(input("Hãy nhập số nào đó: "))
exponential_input_2 = int(input("Hãy nhập số mũ: "))
exponential_result = exponential_input ** exponential_input_2
print(f"Kết quả: {exponential_result}")


#-----------------------------------------------------------------------------------
print("="*10)
#ôn 3 - if elif else
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
    


#-----------------------------------------------------------------------------------
print("="*10)
#ôn 3 - for - while

print("-----=== For ===-----")
numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))
print("Số random ra:", end=" ")
print(*numbers, sep=", ")

# Thuật toán sắp xếp nổi bọt
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Số đã sort lại:", end=" ")
print(*numbers, sep=", ")



print("-----=== While ===-----")
while True:
    a = int(input("Nhập một số để tính toán: "))
    if a > 0:
        break
    else:
        print("Nhập một số khác > 0")

tongle = 0
strtongle = "A = "
for i in range(1, a + 1):
    if i % 2 != 0:
        tongle += i
        strtongle += str(i) + " + "

ketquatongle = strtongle.rstrip(" + ") + " ="
print(ketquatongle, tongle)





#-----------------------------------------------------------------------------------
print("="*10)
#ôn 4 - sử dụng danh sách

fruits = ["apple", "banana", "orange", "grape"]

# Sử dụng phương thức remove()
fruits.remove("orange")
print(" ".join(fruits))

# Sử dụng phương thức append()
fruits.append("mango")
print(" ".join(fruits))

# Sử dụng phương thức clear()
fruits.clear()
print(fruits)

# Sử dụng phương thức insert()
fruits.insert(0, "watermelon")
fruits.insert(1, "kiwi")
print(" ".join(fruits))




#-----------------------------------------------------------------------------------
print("="*10)
#ôn 5 - in - split

print("-----=== split ===-----")
print("hãy làm tròn điểm trước khi nhập, tránh báo lỗi")
scores = input("Nhập danh sách điểm: ").split() 

count = 0
for score in scores:
  if int(score) == 10:  
    count += 1
    
if count > 0:
  print(f"Số lượng điểm 10 là: {count}")
else: 
  print("Bạn chưa có điểm 10")


print("-----=== in ===-----")
district = "BT"
class_name = "BT-TL_C4K_PTA02"
class_name_2 = "HN-TL_C4K_PTA02"
x = district in class_name
y = district in class_name_2
print(x)
print(y)

#-----------------------------------------------------------------------------------
#ôn 6 - hàm def

print("------------=======Tính giá trị tuyệt đối=======------------")
def gia_tri_tuyet_doi(n):
    if n < 0:
        return -n
    else:
        return n
    
# vi dụ sử dụng hàm:
so_nguyen = int(input("Nhập một số nguyên: "))

ket_qua = gia_tri_tuyet_doi(so_nguyen)
print(f"Gía trị tuyệt đối của {so_nguyen} là {ket_qua}")



print("------------=======Diện tích xung quanh - thể tích lập phương=======------------")
def Sxq_HLP(canh_a):
    Sxq_HLP = 4*canh_a**2
    return Sxq_HLP

def V_HLP(canh_a):
    V_HLP = canh_a**3
    return V_HLP

canh_a = float(input("Hãy nhập cạnh a: "))

Sxq_HLP = Sxq_HLP(canh_a)
V_HLP = V_HLP(canh_a)

print(f"Diện tích xung quanh lập phương là: {Sxq_HLP}")
print(f"Thể tích hình lập phương là: {V_HLP}")
