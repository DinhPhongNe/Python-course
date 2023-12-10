A = [3, 8, 6, 16, 23, 39, 40, 82]
sum = 0
for i in range(len(A)):
    if A[i] % 2 == 0:
        sum += A[i]
print(sum)