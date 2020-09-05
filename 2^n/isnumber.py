import math

def log2(x):
    if x == 0:
        return False
    else:
        return (math.log10(x)/math.log10(2))

def ispowerof2(x):
    return (math.ceil(log2(x)) == math.floor(log2(x)))

if ispowerof2(32):
    print("Yes")
else:
    print("No")