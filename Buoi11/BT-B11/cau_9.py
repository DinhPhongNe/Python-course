#Viết chương trình nhập từ bàn phím xâu s gồm ngày tháng với định dạng dd/mm/yyyy, 
# trong đó dd là hai kí tự chỉ ngày, mm là hai kí tự chỉ tháng, yyyy là bốn chỉ tự chỉ năm. 
# Hãy xử lý và đưa ra màn hình ngày, tháng, năm dưới dạng xâu "Ngày dd tháng mm năm yyyy".
print("-"*10)
import datetime

now = str(datetime.datetime.now())
print(f"raw: {now}")
date_time = now.split(" ")

date_string = date_time[0]  
time_string = date_time[1]

date_parts = date_string.split("-")
ngay = date_parts[2]
thang = date_parts[1]  
nam = date_parts[0]

hour, minute, second = time_string.split(":")

# hàm round() để làm tròn, giây để phẩy nhìn xấu=)))
second = round(float(second)) 
print("-"*10)
print(f"Bây giờ là {hour} giờ {minute} phút {second} giây - ngày {ngay} tháng {thang} năm {nam}")
print("-"*10)