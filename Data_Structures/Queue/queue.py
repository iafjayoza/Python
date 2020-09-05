# Queue are first-in first out sequence

# Queue can be used to systematically explore through a search space

x = [2,1]

def addq(e,x):
    x.insert(0,e)
    print(x)
    return x

def removeq(x):
    x.pop()
    print(x)
    return x

addq(3,x)
removeq(x)
