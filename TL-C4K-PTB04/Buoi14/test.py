now = str(input("Hay nhap ngay thang nam (dd/mm/yyyy): "))
date_time = now.split("/")

ngay = date_time[0]
thang = date_time[1]  
nam = date_time[2]

if int(ngay) <= 30 and 31:
    print("Ngày hợp lệ")
if int(thang) <= 12:
    print("Tháng hợp lệ")
if 1900 <= int(nam):
    print("năm Hợp lệ")