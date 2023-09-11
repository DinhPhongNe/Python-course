# Nhập số kẹo và số học sinh
n = int(input("Hãy nhập số kẹo mà thầy đang có: "))
m = int(input("Hãy nhập số học sinh mà lớp thầy có: "))

# phép tính 
keo_nhan_duoc = n // m
keo_con_thua = n % m

# in ra
print(f"Số kẹo mỗi bạn nhận được: {keo_nhan_duoc}")
print(f"Số kẹo còn thừa: {keo_con_thua}")