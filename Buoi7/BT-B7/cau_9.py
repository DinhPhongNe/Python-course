n = int(input("Nhập vào một số nguyên dương n: "))

sum = 0
i = 1

while sum <= n:
    sum += i
    i += 1

print(f"Dãy số tăng dần nhỏ nhất có tổng lớn hơn {n} là:")
for j in range(1, i):
    print(j, end=" ")