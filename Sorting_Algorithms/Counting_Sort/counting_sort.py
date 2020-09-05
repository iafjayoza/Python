# Sorting algrithm fo values between 0 to 9.

def counting_sort(collection):
    l = len(collection)
    C = [0]*10
    S = [0]*len(collection)

    #Inserting the count of each number to C
    for i in collection:
        C[i] += 1
    #Adding the value of left + right values in C
    for i in range(len(C)):
        if i >= 1:
            C[i] = C[i] + C[i-1]

    #Removing the last element from C and adding [0] at beginning.
    C = [0]+ C[:-1]

    #Iterating through collection and sorrting array by refering C
    for i in collection:
        S[C[i]] = i
        C[i] += 1
    print(S)
    return (S)

k = [3,3,2,1,1,0,2,1,3,4,5,5,3,8,9,7]
counting_sort(k)
