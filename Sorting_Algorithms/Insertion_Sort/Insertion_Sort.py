def insertion_sort(collection):
    for slideEnd in range(len(collection)):
        pos = slideEnd

        #Move the element in sorted slide till it find the correct place
        while pos > 0 and collection[pos] < collection[pos-1]:
             (collection[pos],collection[pos-1]) = (collection [pos-1],collection[pos])
             pos -= 1

j =list(range(500 ,0,-2))
insertion_sort(j)
print(j)

k = list(range(0,1000))
insertion_sort(k)
print(k)

l = list(range(0,10000))
insertion_sort(l)
print(l)

m = list(range(1000,0,-3))
insertion_sort(m)
print(m)











