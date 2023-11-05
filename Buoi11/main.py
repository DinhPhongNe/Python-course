name = "Phong"

#in ra từng kí tự trong biến name
for char in name:
  print(char)

print(name.upper()) #upper -> biến chuỗi thành chữ hoa => PHONG
print(name.lower()) #upper -> biến chuỗi thành chữ thường => phong


print("=-------------------------------------=")
classname = "TL C4K PTB04"

# split -> tách một xâu thành mảng ký tự => ['TL', 'C4K', 'PTB04']
o = classname.split()
print(o)

# replace -> thay đổi giá trị => TL C4K ptb04
u = classname.replace("PTB04", "ptb04")
print(u)


district = "BT"
class_name = "BT-TL_C4K_PTB04"
class_name_2 = "HN-TL_C4K_PTB04"
x = district in class_name
y = district in class_name_2
print(x)
print(y)