mylist = []

def iscycle(s,l):
    if l == (len(vo)) and s[vo[l-1]][vo[0]] == 1:
        if vo[1:][::-1] not in mylist:
            mylist.append(vo[1:].copy())
            print(vo)
    else:
        for i in range(l,len(vo)):
            if l == 0:
                (vo[l], vo[i]) = (vo[i], vo[l])
                if vo[0] == first:
                    iscycle(s, l + 1)
                    (vo[l], vo[i]) = (vo[i], vo[l])
            elif s[vo[i]][vo[l-1]] == 1:
                (vo[l], vo[i]) = (vo[i], vo[l])
                if vo[0] == first:
                    iscycle(s, l + 1)
                    (vo[l], vo[i]) = (vo[i], vo[l])
            else:
                pass




vo = [1,2,3,4,5]
first = vo[0]

s = [[0 for j in range(6)] for i in range(6)]
(s[1][2],s[1][3],s[1][5]) = (1,1,1)
(s[2][1],s[2][3],s[2][4],s[2][5]) = (1,1,1,1)
(s[3][1],s[3][2],s[3][4]) = (1,1,1)
(s[4][2],s[4][3],s[4][5]) = (1,1,1)
(s[5][1],s[5][2],s[5][4]) = (1,1,1)

iscycle(s,0)
print(mylist)

x = [1,2,3]
