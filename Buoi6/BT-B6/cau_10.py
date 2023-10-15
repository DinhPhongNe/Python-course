n = int(input("Nhập một số nguyên dương n: "))

print("Các số chẵn từ 1 đến", n, "là:")

for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, end=" ")