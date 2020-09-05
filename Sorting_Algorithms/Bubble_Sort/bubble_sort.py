def bubble_sort(collection,left,right):
    if right - left <= 1:
        return ()
    for i in range(right-1):
        if collection[i] > collection[i+1]:
            (collection[i],collection[i+1]) = (collection[i+1],collection[i])
    bubble_sort(collection,left,right-1)

l=[5,4,8,6,3,2]
bubble_sort(l,0,len(l))
print(l)

k = list(range(500,0,-2))
bubble_sort(k,0,len(k))
print(k)
