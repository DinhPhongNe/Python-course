product_list = ["Áo", "Quần", "Giày", "Túi", "Mũ"]
cart = []

while True:
    print("=== MENU ===")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm vào giỏ hàng")
    print("3. Xem giỏ hàng")
    print("4. Thoát")
    print("============")

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == "1":
        print("Danh sách sản phẩm:")
        for product in product_list:
            print(product)
    elif choice == "2":
        product = input("Nhập tên sản phẩm muốn thêm vào giỏ hàng: ")
        cart.append(product)
        print("Đã thêm", product, "vào giỏ hàng!")
    elif choice == "3":
        if len(cart) == 0:
            print("Giỏ hàng rỗng!")
        else:
            print("Giỏ hàng:")
            for item in cart:
                print(item)
    elif choice == "4":
        print("Cảm ơn bạn đã sử dụng ứng dụng!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")