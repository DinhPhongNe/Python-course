#------------=============== KIỂM TRA TAM GIÁC ===============------------
def triangle_type(a, b, c):
    # Kiểm tra xem có phải là tam giác hay không
    if a + b > c and b + c > a and c + a > b:
        # Kiểm tra tam giác đều
        if a == b == c:
            return "Tam giác đều"
        # Kiểm tra tam giác cân
        elif a == b or b == c or c == a:
            return "Tam giác cân"
        # Kiểm tra tam giác vuông
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "Tam giác vuông"
        # Trường hợp còn lại là tam giác thường
        else:
            return "Tam giác thường"
    else:
        return "Không phải tam giác"

# Nhập vào ba cạnh của tam giác
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Xác định và in loại tam giác
result = triangle_type(a, b, c)
print(result)


#------------=============== GIÁ TRỊ LỚN NHẤT - BÉ NHẤT ===============------------
# Nhập danh sách các số nguyên từ người dùng
input_numbers = input("Nhập danh sách các số nguyên, cách nhau bởi dấu khoảng trắng: ")

# Tách các số nguyên từ xâu đầu vào và chuyển đổi thành danh sách số nguyên
numbers = [int(x) for x in input_numbers.split()]

# Kiểm tra xem danh sách có phần tử hay không
if len(numbers) > 0:
    # In giá trị lớn nhất và bé nhất của danh sách
    print("Giá trị lớn nhất:", max(numbers))
    print("Giá trị bé nhất:", min(numbers))
else:
    print("Danh sách không có phần tử.")


#------------=============== HỌ TÊN ===============------------
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




#------------=============== NGÀY THÁNG NĂM ===============------------
def is_valid_date(day, month, year):
    # Kiểm tra năm nhuận
    leap_year = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
    
    # Kiểm tra tháng và ngày
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if leap_year:
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:
        return False

# Nhập ngày, tháng, năm từ người dùng
date_input = input("Nhập ngày, tháng, năm theo định dạng dd/mm/yyyy: ")
day, month, year = map(int, date_input.split('/'))

# Kiểm tra và xuất kết quả
if is_valid_date(day, month, year):
    print("ngày / tháng / năm hợp lệ")
else:
    print("ngày / tháng / năm không hợp lệ")
