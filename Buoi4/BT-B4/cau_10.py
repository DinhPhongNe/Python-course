#nhập dữ liệu
An = float(input("Nhập chiều cao của An (cm): "))
Minh = float(input("Nhập chiều cao của Minh (cm): "))
Lan = float(input("Nhập chiều cao của Lan (cm): "))

#so sánh chiều cao của các bạn
if An > Minh and An > Lan:
    print("Bạn cao nhất là An")
elif Minh > An and Minh > Lan:
    print("Bạn cao nhất là Minh")
elif Lan > An and Lan > Minh:
    print("Bạn cao nhất là Lan")
else:
    print("Chiều cao 3 bạn bằng nhau")