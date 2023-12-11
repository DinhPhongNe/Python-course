# Nhập họ và tên đầy đủ từ người dùng
full_name = input("Nhập họ và tên đầy đủ: ")

# Tách họ và tên thành danh sách các từ
name_parts = full_name.split()

# Kiểm tra xem có đủ hai từ hay không (họ và tên)
if len(name_parts) >= 2:
    # Xuất họ, tên đệm và tên
    print("Họ:", name_parts[0][0].upper() + name_parts[0][1:])
    
    # Nếu có tên đệm
    if len(name_parts) > 2:
        middle_name = " ".join(name_parts[1:-1])
        print("Tên đệm:", middle_name)
    
    # Xuất tên
    last_name = name_parts[-1]
    print("Tên:", last_name)
else:
    # Nếu chỉ có hai chữ (không có tên đệm)
    print("Họ:", name_parts[0][0].upper() + name_parts[0][1:])
    print("Tên:", name_parts[1])
