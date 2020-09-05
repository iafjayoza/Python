# Brute force algorithm for longest common subsequence.

def LCS(u,v):
    table = [[0 for i in range(len(v)+1)] for j in range(len(u)+1)]

    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r] == v[c]:
                table[r][c] = 1 + table[r+1] [c+1]
            else:
                table[r][c] = max(table[r+1][c],table[r][c+1])
    print(table[0][0])
    return (table[0][0])

a = "secretly"
b = "secratory"
LCS(a,b)