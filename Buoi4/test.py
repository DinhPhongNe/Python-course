print("---------------------===Test - 1 - TH===---------------------")
x, y, z = 10, 6, 8

a = x < 12 and z > 6
b = x > 15 or y < 8
c = not b

print(a)
print(b)
# print(c)

print("---------------------===Test - 2 | kiểm tra chẵn lẻ===---------------------")
a = int(input("Hãy nhập số a bất kỳ: "))

if a % 2 == 0:
    print('a là số chẵn')
else:
    print('a là số lẻ')

print("---------------------===Test - 3 | kiểm tra dương hoặc âm===---------------------")

b = int(input("Nhập một số nguyên: "))

if b > 0:
    print("Đây là một số nguyên dương.")
elif b < 0:
    print("Đây là một số nguyên âm.")
else:
    print("Đây là số 0.")
    
print("---------------------===Test - 4 | thập cẩm - tùm lum===---------------------")
a = 5
b = 10
c = a > b - 5
print(c)

