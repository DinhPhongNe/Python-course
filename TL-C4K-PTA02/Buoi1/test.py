def calculate(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

data = [5, 10, 15, 20, 25]
result = int(calculate(data))
print(result)