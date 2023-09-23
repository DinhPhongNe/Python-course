print("---------------------===tính năm nhuận===---------------------")
year = int(input("hãy nhập một năm: "))

is_leap = False

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
   is_leap = True

if is_leap:
   print(f"{year} là năm nhuận")
else:
   print(f"{year} không phải năm nhuận")