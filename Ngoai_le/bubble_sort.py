import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
# numbers.sort()
# thuật toán sắp xếp nổi bọt
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1):
        if (numbers[j] > numbers[j + 1]):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)