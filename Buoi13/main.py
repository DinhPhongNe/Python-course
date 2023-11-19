# Hình tam giác
print("------------=======Diện tích - Chu vi tam giác=======------------")
def S_TamGiac(a, h):
    S_TamGiac = (a*h)/2
    return S_TamGiac

def C_TamGiac(a, b, c):
    C_TamGiac = a + b + c
    return C_TamGiac

a = float(input("Hãy nhập chiều dài cạnh 1: "))
b = float(input("Hãy nhập chiều dài cạnh 2: "))
c = float(input("Hãy nhập chiều dài cạnh 3: "))
h = float(input("Hãy nhập chiều cao tam giác: "))

S_TamGiac = S_TamGiac(a, h)
C_TamGiac = C_TamGiac(a, b, c)

print(f"Diện tích tam giác là: {S_TamGiac}")
print(f"Chu vi tam giác là: {C_TamGiac}")




# Hình tròn
print("------------=======Diện tích - Chu vi hình tròn=======------------")
def S_HinhTron(r, pi):
    pi = 3.14
    S_HinhTron = r**2 * pi
    return S_HinhTron

def C_HinhTron(d, pi):
    pi = 3.14
    C_HinhTron = d * pi
    return C_HinhTron

pi = 3.14
r = float(input("Hãy nhập bán kính hình tròn: "))
d = float(input("Hãy nhập đường kính hình tròn: "))

S_HinhTron = S_HinhTron(r, pi)
C_HinhTron = C_HinhTron(d, pi)

print(f"Diện tích hình tròn là: {S_HinhTron}")
print(f"Chu vi hình tròn là: {C_HinhTron}")



# Hình chữ nhật
print("------------=======Diện tích - Chu vi hình chữ nhật=======------------")
def S_hcn(cd, cr):
    S_hcn = cd * cr
    return S_hcn

def C_hcn(cd, cr):
    C_hcn = (cd + cr)*2
    return C_hcn

cd = float(input("Hãy nhập chiều dài: "))
cr = float(input("Hãy nhập chiều rộng: "))

S_hcn = S_hcn(cd, cr)
C_hcn = C_hcn(cd, cr)

print(f"Diện tích hình chữ nhật là: {S_hcn}")
print(f"Chu vi hình chữ nhật là: {C_hcn}")
    


# Lũy thừa
print("------------=======Tính lũy thừa=======------------")
def luy_thua(a, b):
    luy_thua = a ** b
    return luy_thua

# ví dụ sử dụng hàm
A = int(input("Nhập số nguyên A: "))
B = int(input("Nhập số nguyên B: "))

ket_qua = luy_thua(A, B)
print(f"Lũy thừa của {A} mũ {B} là: {ket_qua}")

# trị tuyệt đối
print("------------=======Tính giá trị tuyệt đối=======------------")
def gia_tri_tuyet_doi(n):
    if n < 0:
        return -n
    else:
        return n
    
# vi dụ sử dụng hàm:
so_nguyen = int(input("Nhập một số nguyên: "))

ket_qua = gia_tri_tuyet_doi(so_nguyen)
print(f"Gía trị tuyệt đối của {so_nguyen} là {ket_qua}")

# tính tổng danh sách
print("------------=======Tính tổng phần tử trong danh sách=======------------")
def tinh_tong_danh_sach(danh_sach):
    tong = sum(danh_sach)
    return tong

# ví dụ sử dụng hàm:
danh_sach = [1,2,3,4,5,6,7,8,9,10]
ket_qua = tinh_tong_danh_sach(danh_sach)
print(f"Tổng các phần tử trong danh sách là {ket_qua}")

print("------------=======Thực hành 1=======------------")
def S_Can_Phong(canh):
    S_Can_Phong = canh**2
    return S_Can_Phong

def tinh_tam_gach(S_Can_Phong, S_Tam_Gach):
    so_tam_gach = S_Can_Phong / S_Tam_Gach
    return so_tam_gach

canh_can_phong = 80
S_Can_Phong = S_Can_Phong(canh_can_phong)
S_Tam_Gach = 0.0016
so_tam_gach = tinh_tam_gach(S_Can_Phong, S_Tam_Gach)

print(f"Diện tích căn phòng là: {S_Can_Phong} m^2")
print(f"số gạch cần là: {so_tam_gach} tấm")

print("------------=======Thực hành 2=======------------")
def tinhluong(giolam, luonggio):
  tongluong = giolam * luonggio
  return tongluong

def inthongtin(ten, giolam, luonggio, tongluong):
  print(f"Tên nhân viên: {ten}")
  print(f"Số giờ làm: {giolam}") 
  print(f"Mức lương/giờ: {luonggio}")
  print(f"Tổng lương: {tongluong}")
  
tongluong = tinhluong(8, 100000) 

inthongtin("Nguyễn Văn A", 8, 100000, tongluong)

print("------------=======Thực hành 3=======------------")
def check_password_length(password):
    if len(password) >= 8:
        return True
    return False

def check_password_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_password_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_password_special_char(password):
    special_chars = "!@#$%^&*()_+-=[]{}|\\;:'\"<>,./?`~"
    for char in password:
        if char in special_chars:
            return True
    return False

def evaluate_password(password):
    requirements = [
        check_password_length,
        check_password_uppercase,
        check_password_digit,
        check_password_special_char
    ]

    score = 0
    failed_requirements = []

    for requirement in requirements:
        if requirement(password):
            score += 1
        else:
            failed_requirements.append(requirement.__name__)

    return score, failed_requirements

def register():
    username = input("Nhập tên người dùng: ")
    password = input("Nhập mật khẩu: ")

    score, failed_requirements = evaluate_password(password)

    if score >= 3:
        print("Mật khẩu hợp lệ. Đăng ký thành công!")
        # Thực hiện đăng ký người dùng
    else:
        print("Mật khẩu không đáp ứng yêu cầu. Vui lòng thử lại.")
        print("Yêu cầu không đáp ứng:")
        for requirement in failed_requirements:
            print("- " + requirement)

def login():
    username = input("Nhập tên người dùng: ")
    password = input("Nhập mật khẩu: ")

    # Kiểm tra xem tài khoản đã tồn tại hay chưa
    if check_existing_account(username):
        print("Đăng nhập thành công!")
        # Thực hiện đăng nhập
    else:
        print("Tài khoản không tồn tại.")

def check_existing_account(username):
    # Kiểm tra trong cơ sở dữ liệu tài khoản
    # Trả về True nếu tài khoản đã tồn tại, False nếu không tồn tại
    return False

def main():
    while True:
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Lựa chọn của bạn: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

# Chạy chương trình
main()