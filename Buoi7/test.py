while True:
    n = int(input("Nhập vào một số nguyên n: "))
    if n < 0:
        break

if n <= 100:
    for i in range(n, 101):
        print(i)
else:
    print("Số n không hợp lệ.")