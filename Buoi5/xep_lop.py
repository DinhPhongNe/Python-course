print("---------------------===phân chia lớp theo điểm trung bình năm===---------------------")

# Thư viện lớp của khối 6 7 8 9
classes = {'6': ['6A', '6B', '6C'], 
           '7': ['7A', '7B', '7C'],
           '8': ['8A', '8B', '8C'], 
           '9': ['9A', '9B', '9C']}

# Lấy tên khối từ người dùng
grade = input("Enter grade (6-9): ")

# Lấy danh sách học sinh
students = []

# Lặp lại 30 lần để nhập tên 30 hs
for i in range(30):
  
  # Lấy tên và điểm trung bình hs
  name = input("Nhap ten hoc sinh: ") 
  score = float(input("nhap diem trung binh nam truoc hoc sinh: "))
  
  # đặt tên học sinh vào
  students.append({'ten': name, 'diem': score})
  
# chia học sinh ra
students.sort(key=lambda x: x['diem'], reverse=True)

# chia học sinh ra 3 lớp
class_size = len(students)//3 

for i in range(3):

  # lấy tên lớp
  className = classes[grade][i]
  
  print(f"lop: {className}")
  
  # Add students 
  for j in range(class_size):
    print(students[j]['ten'], students[j]['diem'])