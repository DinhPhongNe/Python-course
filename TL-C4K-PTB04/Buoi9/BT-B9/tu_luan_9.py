#Viết chương trình nhập vào một số nguyên dương n là số bài kiểm tra mà em đã làm, 
#nhập n số tiếp lần lượt là điểm số của em cho các bài kiểm tra tương ứng. Hãy:
#1 . Sắp xếp danh sách điểm số theo chiều tăng dần
#2. Xoá số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xoá cả hai)
#3. Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2
#4. Đếm số lượng điểm lớn hơn hoặc bằng 8 và xuất ra màn hình

n = int(input("Nhập số bài kiểm tra: "))
diem = []

#---------YÊU CẦU 1---------
# Nhập điểm số cho từng bài kiểm tra
for i in range(n):
    diem.append(float(input("Nhập điểm cho bài kiểm tra {}: ".format(i+1))))

# Sắp xếp danh sách điểm số theo chiều tăng dần
diem.sort()

# Gộp danh sách điểm thành một chuỗi
chuoi_diem = " ".join(map(str, diem))

# In danh sách điểm đã sắp xếp
print(f"Danh sách điểm từ thấp đến cao là: {chuoi_diem}")

#---------YÊU CẦU 2---------
# Xoá số điểm nhỏ nhất
min_diem = min(diem)
while min_diem in diem:
    diem.remove(min_diem)

#---------YÊU CẦU 3---------
# Gộp danh sách điểm thành một hàng
danh_sach_diem = " ".join(map(str, diem))

# Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2 trên cùng một hàng
print("Danh sách điểm:", danh_sach_diem)

#---------YÊU CẦU 4---------
# Đếm số lượng điểm lớn hơn hoặc bằng 8
diem_lon_hon_8 = [x for x in diem if x >= 8]

print(f"Số lượng điểm lớn hơn hoặc bằng 8: {len(diem_lon_hon_8)}")