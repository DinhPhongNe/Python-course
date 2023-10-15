def fibonacci(n):
    fib_seq = [0, 1]

    if n <= 1:
        return fib_seq[:n+1]

    while len(fib_seq) <= n:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)

    return fib_seq

n = int(input("Hãy nhập số nguyên bất kì: "))
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)