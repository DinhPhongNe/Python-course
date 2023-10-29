#Duyệt danh sách: Cho trước một danh sách A = [5, 12, 15, 7, 7, 30, 3, 56]. 
#Duyệt qua từng phần tử của danh sách, tính tổng các phần tử là số chẵn có trong danh sách.

A = [5, 12, 15, 7, 7, 30, 3, 56]
tong_chan = 0

for i in A:
    if i % 2 == 0:
        tong_chan += i

print(f"Tổng các phần tử là số chẵn trong danh sách A là: {tong_chan}")