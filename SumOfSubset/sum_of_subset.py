validans = []
def sumofsubsets(s,l):
    if l == len(s)-1:
        for i in range(len(s)):
            if sum(s[:i + 1]) == 15:
                if sorted(s[:i + 1]) not in validans:
                    validans.append(sorted(s[:i + 1]))
                i += 1
    else:
        for j in range(l,len(s)):
            (s[j], s[l]) = (s[l], s[j])
            sumofsubsets(s,l+1)
            (s[j], s[l]) = (s[l], s[j])


s = [15,3,2,5,10]
sumofsubsets(s,0)
print(validans)


