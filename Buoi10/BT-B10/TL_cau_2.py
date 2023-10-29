#Quản lý chi tiêu: An đang là học viên tại MindX, An thường xuyên cảm thấy mình sử dụng tiền bừa bãi và rất nhanh hết tiền tiêu vặt. 
#Nhận biết được điều này, An đang có ý định xây dựng một chương trình thống kê số tiền mà An đã tiêu trong tuần (Trừ ngày chủ nhật). 
#Em hãy giúp An viết chương trình nhập vào số tiền chi tiêu mỗi ngày tuần. Hãy xử lý và đưa ra những thống kê như:
# - Tổng chi tiêu trong tuần.
# - Ngày chi tiền nhiều thứ nhất trong tuần
# - Trung bình chi tiêu của mỗi ngày trong tuần 

print("---==Chương trình thống kê chi tiêu trong tuần==---")
print("(đơn vị nghìn đồng)")
tong_chi = 0
chi_cao_nhat = 0 
ngay_chi_cao_nhat = ""

for i in range(1,8):
  if i == 7:
    continue
  print("Nhập chi tiêu ngày thứ ", i, end=": ")
  tien = float(input())
  tong_chi += tien
  if tien > chi_cao_nhat:
    chi_cao_nhat = tien
    ngay_chi_cao_nhat = i

print(f"Tổng chi tiêu trong tuần là: {tong_chi}")
print(f"Ngày chi tiền nhiều nhất là ngày thứ {ngay_chi_cao_nhat}") 
print(f"Trung bình chi tiêu mỗi ngày trong tuần là ≈ {round(tong_chi/6)}") #hàm round để làm tròn thành 51, kết quả ra 50.833333333... nhìn xấu lắm=)))