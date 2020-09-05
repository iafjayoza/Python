def MMC(p):
    n = len(p)
    table = [[0 for i in range(n)] for j in range(n)]
    table_k = [[0 for i in range(n)] for j in range(n)]

    for d in range(1,n-1):
        for i in range(1,n-d):
            j = i+d
            table[i][j]=1000000
            for k in range(i,j):
                subprob = table[i][k]+table[k+1][j]+p[i-1]*p[k]*p[j]
                if subprob < table[i][j]:
                    table[i][j] = subprob
                    table_k[i][j] = k

    for i in table:
        print(i)
    print("")
    print(table[1][n-1])

    print("")
    for i in table_k:
        print(i)
    print(" ")
    print(table_k[1][n-1])

p = [5,4,6,2,7]

MMC(p)


