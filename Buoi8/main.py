# scores = [9, 7, 8]
student_list = ["dũng", "hoàng minh", "khải minh",
                "khang", "long", "phong", "hoàng minh"]
print(student_list)
# Thêm phần tử vào danh sách
# append: thêm vào cuối danh sách
# student_list.append("thiên")
# Xoá phần tử trong danh sách
# remove: xoá theo giá trị của phần tử
student_list.remove("hoàng minh")
# pop: xoá theo vị trí của phần tử
# student_list.pop(4)
print(student_list)

# Trong danh sách thì vị trí đầu tiên là 0
# Truy cập phần tử trong danh sách
# print(student_list[2])
# print(student_list)
# # Cập nhật, chỉnh sửa phần tử trong danh sách
# student_list[2] = ""
# print(student_list)
# print(len(student_list))
# Duyệt các phần tử trong danh sách bằng vòng lặp
# for i in range(len(student_list)):
#     print(student_list[i])
# numbers = [19, 20, 5, 42, 66, 38, 19, 78, 48, 69]
# tong = 0
# for i in range(len(numbers)):
#     # Tìm kiếm các phần tử là số chẵn
#     # if numbers[i] % 2 == 0:
#     #     print(numbers[i])
#     tong += numbers[i]

# print(f"Tổng các phần tử trong danh sách = {tong}")
# numbers = []
# for i in range(1, 100):
#     numbers.append(i)
# print(numbers)