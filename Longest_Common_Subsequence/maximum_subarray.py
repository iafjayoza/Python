# Kadane's algorithm for maximum sub-array problem.

def max_subarray(a):
    current_max = global_max = a[0]
    subarray = []
    for i in range(1,len(a)):
        current_max = max(a[i],current_max + a[i])
        if current_max > global_max:
            global_max = current_max
            subarray.append(a[i])
    print("Maximum sum of subarray is ",global_max)
    print("Maximum subarray is ",subarray)
    return (global_max)

a = [1,-3,2,3,1]
b = [-2,3,2,-1]
max_subarray(b)
