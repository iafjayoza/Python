#Finding sum of subsets dynamic programming

#Empty dictionary for memoization
memo = {}

#Recursive function to compute the solution
def rec_solution(s,total,i,memo):
    key = str(total) + "-" + str(i)
    if key in memo:
        return memo[key]
    if total == 0:
        print(1)
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < s[i]:
        mem_sol =  rec_solution(s,total,i-1,memo)
    else:
        mem_sol = (rec_solution(s,total-s[i],i-1,memo) + rec_solution(s,total,i-1,memo))
    memo[key] = mem_sol
    return mem_sol

#main callung function
def sum_of_subset(s,total):
    return rec_solution(s,total,len(s)-1,memo)

s = [1,2,3,5,8]
sum_of_subset(s,8)