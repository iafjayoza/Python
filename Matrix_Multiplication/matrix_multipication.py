x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[4,5,6,0],
     [8,9,0,5],
     [1,2,3,1]]

row = len(x)
col = len(y[0])
n = len(x[0])

result = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        for k in range(n):
            result[i][j] += x[i][k]*y[k][j]

for i in result:
    print(i)

