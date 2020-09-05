# Stack used for tracking recursive calls
# Last in first out

x = [1,2]

def push(e,x):
    x.append(e)
    print(x)
    return x

def pop(x):
    x.pop()
    print(x)
    return x

push(3,x)
pop(x)