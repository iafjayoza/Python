# Fiind all the subset of given set by recursion / back tracing.

validans = [[]]
def sumofsubsets(s,l):
    if l == len(s)-1:
        for i in range(len(s)):
            x = sorted(s[:i + 1])
            if x not in validans:
                validans.append(x)
    else:
        for j in range(l,len(s)):
            (s[j], s[l]) = (s[l], s[j])
            sumofsubsets(s,l+1)
            (s[j], s[l]) = (s[l], s[j])


s = [1,2,3]
sumofsubsets(s,0)
print(validans)
print(len(validans))


