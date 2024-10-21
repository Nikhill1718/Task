def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fib_sequence = list(fibonacci(n))
print(fib_sequence)
