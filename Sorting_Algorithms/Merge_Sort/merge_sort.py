def merge(a,b):
    (C,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)
    while i+j < m+n:
        if i == m:
            C.append(b[j])
            j += 1
        elif j == n:
            C.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            C.append(a[i])
            i += 1
        elif b[j] < a[i]:
            C.append(b[j])
            j += 1
    return(C)

def mergesort(collection,first,last):
    if last - first <= 1:
        return(collection[first:last])
    if last - first > 1:
        mid  = (first+last) // 2
        L = mergesort(collection,first,mid)
        R = mergesort(collection,mid,last)
        return(merge(L,R))

