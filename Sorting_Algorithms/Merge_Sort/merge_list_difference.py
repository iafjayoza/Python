def merge_list_difference(a,b):
    (C,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)

    while i + j < m+n:
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
            j += 1
        elif j == n:
            C.append(a[i])
            i += 1
        elif a[i] < b[j]:
            C.append(a[i])
            i += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] == b[j]:
            i+=1
            j+=1
    print(C)
    return (C)

a = [1,1,2,3,6,7,8,9,11,14]
b = [1,3,4,5,7,9,14,15,18]
merge_list_difference(a,b)



