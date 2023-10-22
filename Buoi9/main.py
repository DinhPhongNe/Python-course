# scores = [9, 7, 8]
student_list = ["dũng", "hoàng minh", "khải minh",
                "khang", "long", "phong", "hoàng minh"]
print(student_list)

#sort: sắp xếp theo thứ tự tăng dần, nếu khai báo reverse=True thì sẽ theo thứ tự tăng dần
student_list.sort(reverse=True)
print(student_list)
#append: thêm vô list ( cuối danh sách )
student_list.append("thắng")
#insert: thêm vô list vị trí bất kì ( vị trí phải hợp lệ)
student_list.insert(1, "cảnh")
#xóa ở vị trí bất kỳ, không vị trí thì mặc định thằng cuối cút
student_list.pop(0)
#remove: xóa theo giá trị phần tử trong danh sách
student_list.remove("hoàng minh")
#clear: cút hết
student_list.clear()
print(student_list)

number_list = [1,3,5,4,2,6,7,9,8,10]
number_list.sort(reverse=False)
print(number_list)

def sort_without_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

sort_without_sort(number_list)
print(number_list)