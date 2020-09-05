def findpath(l):
    grid = [[0 for i in range(6)] for j in range(11)]
    for j in range(11):
        for i in range(6):
            for x in l:
                if j == x[0] and i == x[1]:
                    grid[j][i] = 0
                    break
            else:
                if j == 0:
                    grid[j][i] = 1
                    #grid[i][j] = grid[i - 1][j]

                elif i == 0:
                    grid[j][i] = 1
                    #grid[i][j] = grid[i][j - 1]

                else:
                    grid[j][i] = grid[j - 1][i] + grid[j][i - 1]
    for i in grid:
        print(i)
    print(grid[10][5])
    return(grid[10][5])

l = [(4,1),(4,2),(4,3),(4,4),(4,5)]
findpath(l)

k = [(4,2)]
findpath(k)

m = []
findpath(m)