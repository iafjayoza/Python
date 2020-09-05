def quick_sort(collection,left,right):
    if right - left <= 1:
        return ()
    yellow = left + 1

    for green in range(left+1,right):
        if collection[green] <= collection[left]:
            (collection[yellow],collection[green]) = (collection[green],collection[yellow])
            yellow += 1

    (collection[left],collection[yellow-1]) = (collection[yellow-1],collection[left])

    quick_sort(collection,left,yellow-1)
    quick_sort(collection,yellow,right)

k =[43,32,51,41,58]
quick_sort(k,0,len(k))
print(k)

l = list(range(500,0,-2)) + list(range(1,99,2))
quick_sort(l,0,len(l))
print(l)


