def merge_wd(a,b):
    (C,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)

    while i + j < m + n:
        if i < m-1:
            while a[i] == a[i+1]:
                i += 1
                if i == m-1:
                    break
        if j < n-1:
            while b[j] == b[j+1]:
                j += 1
                if j == n-1:
                    break
        if i == m:
            C.append(b[j])
            j += 1
        elif j == n:
            C.append(a[i])
            i += 1
        elif a[i] < b [j]:
            C.append(a[i])
            i += 1
        elif a[i] > b [j]:
            C.append(b[j])
            j += 1
        elif a[i] == b[j]:
            C.append(a[i])
            i += 1
            j += 1
    print(C)
    return(C)

a = [1,1,2,2,7,8,8]
b = [1,2,3,3,4,7,7,8]
merge_wd(a,b)





