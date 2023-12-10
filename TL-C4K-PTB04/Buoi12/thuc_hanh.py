#Viết chương trình nhập vào 4 số nguyên lần lượt là tử và mẫu của hai phân số, 
#khởi tạo hàm tính tổng và rút gọn phân số và xuất ra màn hình
def rut_gon_phan_so(tu, mau):
    #tìm ước chung lớn nhất của tử và mẫu
    ucln = 1
    for i in range(2, min(abs(tu), abs(mau)) + 1):
        if tu % i == 0 and mau % i == 0:
            ucln = i
            
    # rút gọn
    tu_rut_gon = tu // ucln
    mau_rut_gon = mau // ucln
    
    # xuất phân số đã rút gọn
    print(tu,"/",mau,"=", tu_rut_gon,"/",mau_rut_gon)
    
def tinh_tong_phan_so(tu1, mau1, tu2, mau2):
    # tính tổng phân số
    tu_tong = tu1 * mau2 + tu2 * mau1
    mau_tong = mau1 * mau2
    
    #rút gọn và xuất ra phân số tổng
    rut_gon_phan_so(tu_tong, mau_tong)
    
# nhập các tử và mẫu của hai phân số
tu1 = int(input("Nhập tử số thứ nhất: "))
mau1 = int(input("Nhập mẫu số thứ nhất: "))
tu2 = int(input("Nhập tử số thứ hai: "))
mau2 = int(input("Nhập mẫu số thứ hai: "))

#tính và xuất tổng phân số
print("\nTổng các phân số: ")
tinh_tong_phan_so(tu1, mau1, tu2, mau2)

#=======================================================

#viết chương trình nhập vào hai nguyên dương a,b(a<b), 
#khởi tạo hàm tìm và xuất ra màn hình các số chia hết cho 
# 3 và 5 trong khoảng từ a đến b

def find_number(a,b):
    #kiểm tra nếu a không chia hết cho 3, ta tăng giá trị
    # của a lên bằng cách làm tròn lên số chia hết tiếp theo
    
    if a % 3 != 0:
        a = (a//3 + 1)*3
        
    #duyệt qua các số trong khoảng từ a đến b
    for num in range(a, b + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num)
            
#nhập hai số nguyên dương a b từ user
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b ( b > a); "))

# gọi hàm để tìm và xuất ra các số chia hết cho 3 và 5 trong
# khoảng từ a đến b
find_number(a, b)

#=======================================================

#viết chương trình cho phép người dùn chọn đăng nhập và đăng ký tài khoản 
# dữ liệu sẽ được lưu trên danh sách, mỗi account là 1 phân tử lưu d
# dưới dạng "username:password"

# List lưu tài khoản
accounts = []

while True:
  print("1. Đăng nhập")
  print("2. Đăng ký")
  print("3. Xuất danh sách tài khoản")
  print("4. Thoát")

  choice = int(input("Chọn chức năng: "))

  if choice == 1:
    # Login logic
    print("Đang đăng nhập")

  elif choice == 2:  
    # Signup logic
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    # Store account as string in list
    accounts.append(f"{username}:{password}")
    print("Đăng ký thành công")
  
  elif choice == 3:
    # Print list of accounts
    print("Danh sách tài khoản:")
    for account in accounts:
      print(account)

  elif choice == 4:
    break

  else:
    print("Vui lòng chọn từ 1-4")