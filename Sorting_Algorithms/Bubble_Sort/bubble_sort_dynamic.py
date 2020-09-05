def bubble_sort_dynamic(collection):
    l = len(collection)
    for k in range(l-1):
        flag = 0
        for i in range(l-k-1):
            if collection[i] > collection[i + 1]:
                (collection[i], collection[i + 1]) = (collection[i + 1], collection[i])
                flag += 1
        if flag == 0:
            break


m = [2,6,5,3,4,1]
bubble_sort_dynamic(m)
print(m)

j = list(range(500,0,-2))
bubble_sort_dynamic(j)
print(j)

n = list(range(500))
bubble_sort_dynamic(n)
print(n)