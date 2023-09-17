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
a1 = 5
b1 = 10
c1 = a1 > b1 - 5
print(c)

a = 5
b = 10
c = a * a + b * b <= 100
print(c)

A = 5
B = 10
C = ( A < B) and (A + 5 != B)
D = not ( A * A + B * B <= 100)
E = ( 3 * A > B) or (2 * A == B)
print(C , D, E)

A1 = 3
B1 = 7
C1 = 12
if not A1 + B1 < C1:
    print("condition 1")
elif A1 * B1 <= B1 + C1:
    print("condition 2")
else:
    print("condition 3")

