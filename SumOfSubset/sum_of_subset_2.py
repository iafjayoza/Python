# sum of subsets in sorted list.
def rec_solution(s,total,i):
    if total == 0:
        print(1)
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < s[i]:
        return rec_solution(s,total,i-1)
    else:
        return rec_solution(s,total - s[i],i-1) + rec_solution(s,total,i-1)

def sum_of_subset(s,total):
    return rec_solution(s,total,len(s)-1)

s = [1,2,3,5,8]
sum_of_subset(s,8)