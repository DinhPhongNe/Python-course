print("---------------------===kiểm tra chẵn lẻ===---------------------")
chan_le = int(input("Hãy nhập số a bất kỳ: "))

if chan_le % 2 == 0:
    print(f'{chan_le} là số chẵn')
else:
    print(f'{chan_le} là số lẻ')


print("---------------------===kiểm tra dương hoặc âm===---------------------")

so_nguyen = int(input("Nhập một số nguyên: "))

if so_nguyen > 0:
    print(f"{so_nguyen} là một số nguyên dương.")
elif so_nguyen < 0:
    print(f"{so_nguyen} là một số nguyên âm.")
else:
    print("Đây là số 0.")