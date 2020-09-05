# Fiind all the subset of given set by recursion / back tracing.

def findsubsets(givenarray,subset,i):
    if i == len(givenarray):
        l = [i for i in subset if i is not None]
        print(l)
    else:
        subset[i] = None
        findsubsets(givenarray,subset,i+1)
        subset[i] = givenarray[i]
        findsubsets(givenarray,subset,i+1)

def allsubsets(givenarray):
    subset = givenarray.copy()
    findsubsets(givenarray,subset,0)

myarray = [1,2,3]
allsubsets(myarray)