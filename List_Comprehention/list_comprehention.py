#List comprehention with map and filter

def iseven(x):
    return (x%2 ==0)

def square(x):
    return (x*x)

result = [square(i) for i in range(100) if iseven(i)]
print(result)

#List comprehention for initiallizing matrix

matrix = [[0 for i in range(3)] for i in range(4)]
print(matrix)
matrix[1][1]=7
print(matrix)

#Extra List operations

list1 = [1,2,3,4,5]
list2 = list1
list3 = list1.copy()
del[list1[2]]
print(list1)
print(list2)
print(list3)

list4 = list3 + list1
print(list4)

list3.append(9)
print(list3)

list3.extend(list1)
print(list3)

print(list1.index(2))

list3[2:] = [5]
print(list3)

list1[2:] = [7,8,9,0]
list1.append(2)
print(list1)

print(list1.count(2))
list1.sort()
print(list1)
list1.reverse()
print(list1)

