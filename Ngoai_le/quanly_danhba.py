print("---------------------===Quản lý danh bạ===---------------------")
# Dictionary chứa danh sách danh bạ 
contacts = {'John': '0909999999', 'Mary': '09111111111', 'Bob': '09222222222'}

# Hàm hiển thị danh sách 
def view_contacts():
   for name, number in contacts.items():
      print(f"{name} - {number}")

# Hàm thêm mới danh bạ
def add_contact():
   name = input("Nhập tên: ")
   number = input("Nhập số điện thoại: ")
   contacts[name] = number
   print("Đã thêm thành công.")

# Hàm cập nhật số điện thoại
def update_contact():
   name = input("Nhập tên cần cập nhật: ")
   if name in contacts:
      number = input(f"Nhập số điện thoại mới cho {name}: ")  
      contacts[name] = number
      print("Cập nhật thành công.")
   else:
      print(f"Không tìm thấy {name} trong danh bạ.")

# Hiển thị menu
print("QUẢN LÝ DANH BẠ")  
print("1. Xem danh sách")
print("2. Thêm mới") 
print("3. Cập nhật")
print("4. Thoát")

choice = input("Nhập lựa chọn: ")

if choice == '1':
   view_contacts()
elif choice == '2':
   add_contact()  
elif choice == '3':
   update_contact()
elif choice == '4':
   exit()
else:
   print("Lựa chọn không hợp lệ")