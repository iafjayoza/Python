fibtable = {}

def fibonaccim(n):
    if n in fibtable.keys():
        return (fibtable[n])
    if n == 0 or n == 1:
        return n
    value = fibonaccim(n-1) + fibonaccim(n-2)
    fibtable[n] = value
    print(value)
    return value

fibonaccim(5)
print(fibtable)
