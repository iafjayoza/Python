def redix_sort(collection):
    t = (len(str(max(k))))
    col = collection
    for j in range(1,t+1):
        C = [0] * 10
        S = [0] * len(col)
        # Inserting the count of each number to C
        for i in col:
            m = (list(str(i)))
            if j <= len(m):
                C[int(m[-j])] += 1
            else:
                C[0] += 1
        # Adding the value of left + right values in C
        for i in range(len(C)):
            if i >= 1:
                C[i] = C[i] + C[i - 1]

        # Removing the last element from C and adding [0] at beginning.
        C = [0] + C[:-1]

        # Iterating through collection and sorrting array by refering C
        for i in col:
            m = (list(str(i)))
            if j <= len(m):
                S[C[int(m[-j])]] = i
                C[int(m[-j])] += 1
            else:
                S[C[0]] = i
                C[0] += 1
        col = S

    print(S)
    return (S)

k = [55,23,215,108]
redix_sort(k)

n = list(range(50,0,-2)) + list(range(1,50,2))
print(n)
redix_sort(n)


p = (3.5,"Hello")
print(type (o))
print(type (p))
