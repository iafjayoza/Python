def factorial(n):
    if n == 1:
        return n
    value = n * factorial(n-1)
    return value

def findpath(n,k):
    path = factorial(n) / (factorial(k) * factorial(n-k))
    print(path)
    return (path)

#Example where we have 10 column and 5 rows for destination path.
findpath(15,5)