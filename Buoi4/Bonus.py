print("---------------------===so sánh tổng số học sinh từ khối 1 - 5===---------------------")

# biến học sinh
tong_hoc_sinh = int(input("hãy nhập tổng số học sinh trường bạn: "))
# nhập dữ liệu
khoi_1 = int(input("Hãy nhập tổng số học sinh khối 1: "))
khoi_2 = int(input("Hãy nhập tổng số học sinh khối 2: "))
khoi_3 = int(input("Hãy nhập tổng số học sinh khối 3: "))
khoi_4 = int(input("Hãy nhập tổng số học sinh khối 4: "))
khoi_5 = int(input("Hãy nhập tổng số học sinh khối 5: "))

# so sánh số học sinh các lớp
if khoi_1 > khoi_2 and khoi_1 > khoi_3 and khoi_1 > khoi_4 and khoi_1 > khoi_5:
    print(f"số học sinh khối 1 đông nhất trong tổng số {tong_hoc_sinh} em học sinh")
elif khoi_2 > khoi_1 and khoi_2 > khoi_3 and khoi_2 > khoi_4 and khoi_2 > khoi_5:
    print(f"số học sinh khối 2 đông nhất trong tổng số {tong_hoc_sinh} em học sinh")
elif khoi_3 > khoi_1 and khoi_3 > khoi_2 and khoi_3 > khoi_4 and khoi_3 > khoi_5:
    print(f"số học sinh khối 3 đông nhất trong tổng số {tong_hoc_sinh} em học sinh")
elif khoi_4 > khoi_1 and khoi_4 > khoi_2 and khoi_4 > khoi_3 and khoi_4 > khoi_5:
    print(f"số học sinh 4 một đông nhất trong tổng số {tong_hoc_sinh} em học sinh")
else:
    print(f"số học sinh 5 một đông nhất trong tổng số {tong_hoc_sinh} em học sinh")

# tính chênh lệch mỗi khối
chenh_lech_1 = abs(khoi_1 - (tong_hoc_sinh / 5))
chenh_lech_2 = abs(khoi_2 - (tong_hoc_sinh / 5))
chenh_lech_3 = abs(khoi_3 - (tong_hoc_sinh / 5))
chenh_lech_4 = abs(khoi_4 - (tong_hoc_sinh / 5))
chenh_lech_5 = abs(khoi_5 - (tong_hoc_sinh / 5))

ti_le_1 = chenh_lech_1 / (tong_hoc_sinh / 5) * 100
ti_le_2 = chenh_lech_2 / (tong_hoc_sinh / 5) * 100
ti_le_3 = chenh_lech_3 / (tong_hoc_sinh / 5) * 100
ti_le_4 = chenh_lech_4 / (tong_hoc_sinh / 5) * 100
ti_le_5 = chenh_lech_5 / (tong_hoc_sinh / 5) * 100

print(f"Phần trăm chênh lệch số học sinh khối 1: {ti_le_1}%")
print(f"Phần trăm chênh lệch số học sinh khối 2: {ti_le_2}%")
print(f"Phần trăm chênh lệch số học sinh khối 3: {ti_le_3}%")
print(f"Phần trăm chênh lệch số học sinh khối 4: {ti_le_4}%")
print(f"Phần trăm chênh lệch số học sinh khối 5: {ti_le_5}%")