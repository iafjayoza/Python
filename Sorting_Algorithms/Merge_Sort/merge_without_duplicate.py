def merge_wd(a,b):
    (C,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)

    while i+j < m+n:
        if i == m:
            if b[j] not in C:
                C.append(b[j])
            j+=1
        elif j == n:
            if a[i] not in C:
                C.append(a[i])
            i+=1
        elif a[i] <= b[j]:
            if a[i] not in C:
                C.append(a[i])
            i+=1
        elif a[i] > b[j]:
            if b[j] not in C:
                C.append(b[j])
            j+=1
    print(C)
    return (C)

a = [1,1,2]
b = [1,2,3,4]
merge_wd(a,b)