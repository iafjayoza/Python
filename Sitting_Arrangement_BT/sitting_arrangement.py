#Arrange a sitting positions where 2 boys and 1 girl can sit with constrain that girl can not place in middle.

def sitting_arrangement(s,l):
    if l == len(s)-1 and s[1] != "Girl1":
        print(s)
        return (s)
    else:
        for i in range(l,len(s)):
            (s[l],s[i]) = (s[i],s[l])
            sitting_arrangement(s,l+1)
            (s[l], s[i]) = (s[i], s[l])

s = ["Boy1","Boy2","Girl1"]
sitting_arrangement(s, 0)




