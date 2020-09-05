# Brute force algorithm for longest common sub-word.

def LCW(u,v):
    table = [[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
    maxLCW = 0
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r] == v[c]:
                table[r][c] = 1 + table[r+1][c+1]
            else:
                table[r][c] = 0
            if table[r][c] > maxLCW:
                maxLCW = table[r][c]
    print(maxLCW)
    for line in table:
        print(line)
    return (maxLCW)

a = "secret"
b = "secratory"
LCW(a,b)