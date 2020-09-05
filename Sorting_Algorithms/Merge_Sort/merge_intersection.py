def merge_intersection(a,b):
    (C,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)

    while i + j < m + n:
        if i == m:
            j += 1
        elif j == n:
            i += 1
        elif a[i] < b [j]:
            i += 1
        elif a[i] > b [j]:
            j += 1
        elif a[i] == b[j]:
            C.append(a[i])
            i += 1
            j += 1
    print(C)
    return(C)

a = [1,1,2,2,3]
b = [1,2,3,3,4]
merge_intersection(a,b)





