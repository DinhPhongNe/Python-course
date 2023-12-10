# Viết chương trình nhập vào một danh sách điểm số, mỗi điểm được cách nhau bởi một dấu khoảng trắng. 
# Hãy kiểm tra xem trong danh sách điểm số vừa nhập có tồn tại điểm 10 hay không, nếu có thì in ra số lượng điểm 10, 
# nếu không thì xuất ra màn hình thông báo "Bạn chưa có điểm 10".

print("hãy làm tròn điểm trước khi nhập, tránh báo lỗi")
scores = input("Nhập danh sách điểm: ").split() 

count = 0
for score in scores:
  if int(score) == 10:  
    count += 1
    
if count > 0:
  print(f"Số lượng điểm 10 là: {count}")
else: 
  print("Bạn chưa có điểm 10")