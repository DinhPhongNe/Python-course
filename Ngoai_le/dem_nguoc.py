print("---------------------===đếm ngược===---------------------")
import time

# Nhập thời gian cần đếm ngược
hours = int(input("Nhập số giờ: ")) 
minutes = int(input("Nhập số phút: "))
seconds = int(input("Nhập số giây: "))

# Chuyển sang đơn vị giây
total_seconds = hours*3600 + minutes*60 + seconds

# Vòng lặp đếm ngược
while total_seconds > 0:

   print("Thời gian còn lại:", end=" ")
   
   hours = total_seconds // 3600
   minutes = (total_seconds % 3600) // 60 
   seconds = total_seconds % 60

   print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

   total_seconds -= 1
   time.sleep(1)

print("Hết giờ!")