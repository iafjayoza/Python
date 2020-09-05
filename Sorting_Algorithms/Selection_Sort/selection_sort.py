def selection_sort(collection):
    for first in range(len(collection)):
        # seq into 0 len(collection) , 1 to len(colletion) ... etc
        for i in range(first,len(collection)):
            minval = first
            if collection[i] < collection[minval]:
                minval = i
                # swaping the min value with first value in collection
                (collection[first],collection[minval]) = (collection[minval],collection[first])

l = [5,4,3,2,1]
selection_sort(l)
print(l)

k=list(range(300,0,-3))
selection_sort(k)
print(k)

