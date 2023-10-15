n = int(input("Nhập một số nguyên dương n: "))

num = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        num += i

print(f"Tổng các số chẵn từ 1 đến {n} là: {num}")