def doc_so(n):
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    nghin = ["", "một nghìn", "hai nghìn", "ba nghìn", "bốn nghìn", "năm nghìn", "sáu nghìn", "bảy nghìn", "tám nghìn", "chín nghìn"]

    a = n // 1000
    b = (n % 1000) // 100
    c = (n % 100) // 10
    d = n % 10

    result = ""

    if a > 0:
        result += nghin[a]
    if b > 0:
        result += ("" if result == "" else " ") + tram[b]
    if c > 0:
        if c == 1:
            result += ("" if result == "" else " ") + "mười"
        else:
            result += ("" if result == "" else " ") + chuc[c]
    if d > 0:
        if c == 0 and a == 0 and b == 0:
            result += don_vi[d]
        else:
            result += ("" if result == "" else " ") + don_vi[d]

    return result

# Nhập số từ người dùng
so = int(input("Nhập vào một số tự nhiên 4 chữ số: "))

# Gọi hàm để đọc số và hiển thị kết quả
print("Đọc bằng chữ là:", doc_so(so))
