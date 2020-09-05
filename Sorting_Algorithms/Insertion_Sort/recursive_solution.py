def insertion_sort(collection):
    isort(collection,len(collection))

def isort(collection,k):
    #Recursively calling insert from k = 1 to k = len(collection) - 1
    if k > 1:
        isort(collection,k-1)
        insert(collection,k-1)

def insert(collection,k):
    pos = k
    # Move the element in sorted slide till it find the correct place
    while pos > 0 and collection[pos] < collection[pos-1]:
        (collection[pos],collection[pos-1]) = (collection[pos-1],collection[pos])
        pos -= 1

l = list(range(500,0,-2))
insertion_sort(l)
print(l)


