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




# Hình bình hành
print("------------=======Diện tích hình bình hành=======------------")
def S_hbh(a, h):
    S_hbh = a*h
    return S_hbh

a = float(input("Hãy nhập chiều dài: "))
h = float(input("Hãy nhập chiều cao: "))

S_hbh = S_hbh(a,h)

print(f"Diện tích hình bình hành là: {S_hbh}")




# Hình hình thoi
print("------------=======Diện tích hình thoi=======------------")
def S_HinhThoi(cd_thoi, cr_thoi):
    S_HinhThoi = (cd_thoi * cr_thoi)/2
    return S_HinhThoi

cd_thoi = float(input("Hãy nhập chiều dài hình thoi: "))
cr_thoi = float(input("Hãy nhập chiều rộng hình thoi: "))

S_HinhThoi(cd_thoi, cr_thoi)

print(f"Diện tích hình thoi là: {S_HinhThoi}")




# Hình thang
print("------------=======Diện tích - hình thang=======------------")
def S_hinhThang(daylon, daybe, chieucao):
    S_hbh = (((daylon + daybe)*chieucao)/2)
    return S_hbh

daylon = float(input("Hãy nhập chiều dài đáy lớn: "))
daybe = float(input("Hãy nhập chiều dài đáy bé: "))
chieucao = float(input("Hãy nhập chiều cao: "))

S_hinhThang = S_hinhThang(daylon, daybe, chieucao)

print(f"Diện tích hình bình hành là: {S_hinhThang}")





# Hình hộp chữ nhật
print("------------=======Diện tích xung quanh - thể tích hộp chữ nhật=======------------")
def Sqx_HHCN(acd, acr, ah):
    Sqx_HHCN = 2(acd * acr)*ah
    return Sqx_HHCN

def V_HHCN(acd, acr, ah):
    V_HHCN = acd*acr*ah
    return V_HHCN

acd = float(input("Hãy nhập chiều dài: "))
acr = float(input("Hãy nhập chiều rộng:"))
ah = float(input("Hãy nhập chiều cao: "))

Sqx_HHCN = Sqx_HHCN(acd, acr, ah)
V_HHCN = V_HHCN(acd, acr, ah)

print(f"Diện tích xung quanh hộp chữ nhật là: {Sqx_HHCN}")
print(f"Thể tích hình hộp chữ nhật là: {V_HHCN}")




# Hình lập phương
print("------------=======Diện tích xung quanh - thể tích lập phương=======------------")
def Sxq_HLP(canh_a):
    Sxq_HLP = 4*canh_a**2
    return Sxq_HLP

def V_HLP(canh_a):
    V_HLP = canh_a**3
    return V_HLP

canh_a = float(input("Hãy nhập cạnh a: "))

Sxq_HLP = Sxq_HLP(canh_a)
V_HLP = V_HLP(canh_a)

print(f"Diện tích xung quanh lập phương là: {Sxq_HLP}")
print(f"Thể tích hình lập phương là: {V_HLP}")





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



# chuyển chữ thường sang full in hoa
print("------------=======chuyển chữ thường sang full in hoa=======------------")
def chuyen_viethoa(chuoi):
    return chuoi.upper()

x = input("Hãy nhập một đoạn chuỗi chữ thường: ")
ket_qua = chuyen_viethoa(x)
print(f"Chuỗi viết hoa: {ket_qua}")



# dãy fibonnancy
print("------------=======tạo ra dãy fibonacci=======------------")
def tao_danh_sach_fibonacci(n):
    danh_sach = [0, 1]
    while len(danh_sach) < n:
        so_moi = danh_sach[-1] + danh_sach[-2]
        danh_sach.append(so_moi)
    return danh_sach

inter = int(input("Hãy nhập số nguyên bất kỳ: "))
ket_qua = tao_danh_sach_fibonacci(inter)
print(f"Danh sách {inter} số Fibonacci đầu tiên: {ket_qua}")



#năm nhuận
print("------------=======in ra năm nhuận=======------------")
def la_nam_nhuan(nam):
    if nam % 4 == 0:
        if nam % 100 == 0:
            if nam % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

nam = int(input("Hãy nhập một năm bất kì: "))
if la_nam_nhuan(nam):
    print(f"{nam}là năm nhuận")
else:
    print(f"{nam} không là năm nhuận")



#tính tổng mũ
print("------------=======tính tổng các số mũ=======------------")
def tinh_tong_cac_chu_so_mu(n):
    tong = 0
    for i in range(1, n + 1):
        so_mu = i**i
        chu_so = so_mu % 10
        tong += chu_so
    return tong

tong_mu = int(input("Hãy nhập một số bất kỳ: "))
ket_qua = tinh_tong_cac_chu_so_mu(tong_mu)
print(f"Tổng các chữ số mũ từ 1 đến {tong_mu} là {ket_qua}")



#tìm từ giống nhau
print("------------=======tìm từ giống nhau=======------------")
def tim_kiem_tu_giong_nhau(danh_sach_chuoi):
    tu_giong_nhau = []
    for i in range(len(danh_sach_chuoi)):
        for j in range(i + 1, len(danh_sach_chuoi)):
            if danh_sach_chuoi[i] == danh_sach_chuoi[j]:
                if danh_sach_chuoi[i] not in tu_giong_nhau:
                    tu_giong_nhau.append(danh_sach_chuoi[i])
    return tu_giong_nhau

def sap_xep_tang_dan(danh_sach_chuoi):
    for i in range(len(danh_sach_chuoi)):
        for j in range(len(danh_sach_chuoi) - i - 1):
            if danh_sach_chuoi[j] > danh_sach_chuoi[j + 1]:
                danh_sach_chuoi[j], danh_sach_chuoi[j + 1] = danh_sach_chuoi[j + 1], danh_sach_chuoi[j]
    return danh_sach_chuoi

def tach_chuoi_thanh_tu(danh_sach_chuoi):
    tu = []
    for chuoi in danh_sach_chuoi:
        tu.extend(chuoi.split())
    return tu

def in_cac_tu_theo_chu_so(tu):
    tu_sap_xep = sap_xep_tang_dan(tu)
    for i in range(1, 10):
        tu_theo_chu_so = [tu for tu in tu_sap_xep if tu.startswith(str(i))]
        if tu_theo_chu_so:
            print("Các từ bắt đầu bằng chữ số", i, ":")
            print(tu_theo_chu_so)
            print()

chuoi_1 = "hello world"
chuoi_2 = "hi there"
chuoi_3 = "how are you"
chuoi_4 = "hello python"
chuoi_5 = "hi there"
danh_sach_chuoi = [chuoi_1, chuoi_2, chuoi_3, chuoi_4, chuoi_5]

tu_giong_nhau = tim_kiem_tu_giong_nhau(danh_sach_chuoi)
print("Các từ giống nhau trong danh sách chuỗi:")
print(tu_giong_nhau)
print()

tu = tach_chuoi_thanh_tu(danh_sach_chuoi)
print("Các từ trong danh sách chuỗi:")
print(tu)
print()

in_cac_tu_theo_chu_so(tu)



#tổng đường chéo ma trận
print("------------=======tính tổng đường chéo ma trận=======------------")
def tinh_tong_tu_duong_cheo_ma_tran(ma_tran):
    tong = 0
    for i in range(len(ma_tran)):
        for j in range(len(ma_tran[i])):
            if i == j:
                tong += ma_tran[i][j]
    return tong

def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_lon_nhat(mang):
    so_nguyen_to_max = None
    for so in mang:
        if kiem_tra_so_nguyen_to(so):
            if so_nguyen_to_max is None or so > so_nguyen_to_max:
                so_nguyen_to_max = so
    return so_nguyen_to_max

ma_tran = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

tong_duong_cheo = tinh_tong_tu_duong_cheo_ma_tran(ma_tran)
print("Tổng các phần tử trên đường chéo chính của ma trận:")
print(tong_duong_cheo)
print()

mang_so = [2, 3, 4, 5, 6, 7, 8, 9, 10]
so_nguyen_to_lon_nhat = tim_so_nguyen_to_lon_nhat(mang_so)
print("Số nguyên tố lớn nhất trong mảng:")
print(so_nguyen_to_lon_nhat)



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