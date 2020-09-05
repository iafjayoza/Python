mydict = {}

def shortest_path(s,i,k):
    for j in range(1,len(s[0])):
        if s[i][j] > 0:
            x = str(1) + "-" + str(j)
            if str(x) not in mydict.keys() or mydict[x] > k + s[i][j]:
                mydict[x] = k + s[i][j]
                shortest_path(s,j,k + s[i][j])


s = [[0 for j in range(7)] for i in range(7)]

(s[1][2],s[1][3]) = (2,4)
(s[2][3],s[2][4]) = (1,7)
(s[3][5],s[4][6])= (3,1)
(s[5][4],s[5][6])= (2,5)

shortest_path(s,1,0)
print(mydict)