password = "DinhPonBiDeadlineDi"

while True:
    input_password = input("Nhập mật khẩu: ")

    if input_password == password:
        print("Đăng nhập thành công")
        break
    else:
        print("Mật khẩu không chính xác")