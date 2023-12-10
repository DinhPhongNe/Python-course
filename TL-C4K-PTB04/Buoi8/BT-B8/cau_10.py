A = []

n = int(input("Nhập số phần tử của danh sách: "))
print("="*10)
for i in range(n):
    num = int(input("Nhập giá trị cho phần tử thứ {}: ".format(i+1)))
    A.append(num)

min_num = min(A)
max_num = max(A)
print("="*10)
print("Số nhỏ nhất trong danh sách là:", min_num)
print("Số lớn nhất trong danh sách là:", max_num)