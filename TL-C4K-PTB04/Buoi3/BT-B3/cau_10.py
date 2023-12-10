can_doi = int(input("Nhập số giây bạn cần đổi: "))

# Chuyển đổi số giây thành giờ, phút và giây
gio = can_doi // 3600
phut = (can_doi % 3600) // 60
giay = (can_doi % 3600) % 60

# In kết quả ra màn hình
print(can_doi, "giây chuyển thành: {} giờ, {} phút, {} giây".format(gio, phut, giay))