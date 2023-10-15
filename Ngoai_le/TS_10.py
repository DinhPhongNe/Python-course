import time
import random

print("=== CHƯƠNG TRÌNH TÍNH ĐIỂM CHUẨN ĐẬU VÀO TRƯỜNG CẤP 3 ===\n")
time.sleep(1)

# đăng nhập
print(" === VUI LÒNG ĐĂNG NHẬP === ")
def generate_captcha():
    # Generate a random string of letters and digits
    captcha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7))
    
    # Display the CAPTCHA and ask the user to enter it
    print('Hãy nhập theo CAPTCHA sau đây: ' + captcha)
    user_input = input('Nhập nó ở đây -->: ')
    
    # Check if the user entered the correct CAPTCHA
    if user_input == captcha:
        print('Duyệt thành công CAPTCHA')
        return True
    else:
        print('Duyệt không thành công CAPTCHA')
        return False

def login():
    # Ask the user for their username and password
    username = input('Nhập tên tài khoản: ')
    password = input('Nhập mật khẩu tài khoản: ')
    
    # Verify the CAPTCHA
    while not generate_captcha():
        pass
    
    # Verify the username and password
    if username == 'student1' and password == 'password1':
        print('Đăng nhập thành công')
    else:
        print('Đăng nhập không thành công')

login()

print("="*50)

# Nhập thông tin thí sinh
print(" === Vui lòng nhập thông tin thí sinh === ")
so_bao_danh = input("Nhập số báo danh: ")
ten = input("Nhập họ và tên: ")
tinh_thanh = input("Nhập tỉnh/ Thành phố: ")
truong_du_thi = input("Nhập tên trường dự thi: ")
phong_du_thi = input("Nhập số phòng dự thi: ")

print("="*50)
print("\n=== ĐIỂM MÔN THƯỜNG ===")
# Nhập điểm các môn học
print(" === Vui lòng nhập điểm từng môn === ")
toan = float(input("Nhập điểm môn Toán: "))
if toan < 0 or toan > 10:
    print("Điểm môn Toán không hợp lệ. Vui lòng nhập lại!")
    toan = float(input("Nhập lại điểm môn Toán: "))
    
van = float(input("Nhập điểm môn Văn: "))
if van < 0 or van > 10:
    print("Điểm môn Văn không hợp lệ. Vui lòng nhập lại!")
    van = float(input("Nhập lại điểm môn Văn: "))
    
anh = float(input("Nhập điểm môn Anh: "))
if anh < 0 or anh > 10:
    print("Điểm môn Anh không hợp lệ. Vui lòng nhập lại!")
    anh = float(input("Nhập lại điểm môn Anh: "))
    
su = float(input("Nhập điểm môn Sử: "))
if su < 0 or su > 10:
    print("Điểm môn Sử không hợp lệ. Vui lòng nhập lại!")
    su = float(input("Nhập lại điểm môn Sử: "))

print("="*50)
# Nhập điểm môn chuyên
print("=== ĐIỂM MÔN CHUYÊN ===")
print("Chọn môn chuyên của bạn:")
print("1. Toán")
print("2. Văn")
print("3. Anh")
print("4. Sử")

mon_chuyen = input("Nhập lựa chọn của bạn (1-4): ")
while mon_chuyen not in ["1", "2", "3", "4"]:
    mon_chuyen = input("Lựa chọn không hợp lệ. Vui lòng nhập lại (1-4): ")
if mon_chuyen == "1":
    ten_mon_chuyen = "Toán"
elif mon_chuyen == "2":
    ten_mon_chuyen = "Văn"
elif mon_chuyen == "3":
    ten_mon_chuyen = "Anh"
else:
    ten_mon_chuyen = "S"
diem_mon_chuyen = float(input(f"Nhập điểm môn {ten_mon_chuyen}: "))

# Tính tổng điểm
tong_diem = toan + van + anh + su + diem_mon_chuyen
print("="*50)
# Nhập thông tin nguyện vọng
print("=== NGUYỆN VỌNG VÀ ĐIỂM CHUẨN ===")
nguyen_vong = []
for i in range(3):
    ten_nv = input(f"Nhập tên trường nguyện vọng {i+1}: ")
    diem_chuan_nv = float(input(f"Nhập điểm chuẩn nguyện vọng {i+1}: "))
    print("="*25)
    nguyen_vong.append({"ten": ten_nv, "diem_chuan": diem_chuan_nv})

print("Chúng tôi đang chuẩn bị kết quả cho bạn")
time.sleep(3)
# Hiển thị kết quả

print("\n=== THÔNG TIN - KẾT QUẢ THI ===")
print(f"Số báo danh: {so_bao_danh}")
print(f"Họ và tên: {ten}")
print(f"Tỉnh/ Thành phố: {tinh_thanh}")
print(f"Trường dự thi: {truong_du_thi}")
print(f"Số phòng dự thi: {phong_du_thi}")
print(f"Điểm môn chuyên: {diem_mon_chuyen}")
print(f"Điểm tổng: {tong_diem}")

# Kiểm tra xem thí sinh đậu vào nguyện vọng nào
for i, nv in enumerate(nguyen_vong):
    print(f"Nguyện vọng {i+1}: {nv['ten']} (Điểm chuẩn: {nv['diem_chuan']})")
    if tong_diem >= nv["diem_chuan"]:
        print(f"Kết quả xét tuyển: Đậu nguyện vọng {i+1}!")
        break
else:
    print("Kết quả xét tuyển: Không đậu vào bất kỳ nguyện vọng nào!")
    print("Hẹn gặp bạn vào kì thi năm sau, chúc may mắn!")

# Tính và hiển thị điểm chênh lệch giữa điểm chuẩn và tổng điểm của thí sinh
for nv in nguyen_vong:
    chenh_lech = nv["diem_chuan"] - tong_diem
    print(f"Điểm chênh lệch với nguyện vọng {nv['ten']}: {chenh_lech}")

# Sắp xếp nguyện vọng theo thứ tự giảm dần của điểm chuẩn
nguyen_vong.sort(key=lambda x: x["diem_chuan"], reverse=True)
print("\n=== THÔNG TIN NGUYỆN VỌNG ===")
for i, nv in enumerate(nguyen_vong):
    print(f"{i+1}. {nv['ten']} (Điểm chuẩn: {nv['diem_chuan']})")