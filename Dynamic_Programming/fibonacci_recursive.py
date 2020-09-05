def fibonacci(n):
    if n == 0 or n == 1:
        return n
    value = fibonacci(n-1) + fibonacci(n-2)
    print(value)
    return value

fibonacci(12)