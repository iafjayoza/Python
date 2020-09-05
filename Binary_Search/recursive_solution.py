def binary_search_recursive_solution(collec,v,l,r):
    if (r - l == 0):
        if (collec[r] == v):
            print("value {} is present under sorted collection".format(v))
            return (True)
        else:
            print("Value not found!")
            return (False)
    midpoint = (l + r) // 2
    if (collec[midpoint] == v):
        print("value {} is present under sorted collection".format(v))
        return (True)
    if (collec[midpoint] < v):
        return (binary_search_recursive_solution(collec,v,midpoint+1,r))
    else:
        return (binary_search_recursive_solution(collec,v,l,midpoint))

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

binary_search_recursive_solution(x,8,4,11)








