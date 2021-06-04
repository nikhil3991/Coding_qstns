
def steps(arr):
    n = len(arr)
    if n<=1:
        return 0
    jump = 1
    max_reach = arr[0]
    step = arr[0]
    for i in range(1,n):
        if i == n-1:
            return jump
        max_reach=max(max_reach,i+arr[i])
        step = step-1
        if step == 0:
            jump=jump+1
            if i >= max_reach:
                return -1
            step = max_reach-i
    return -1

arr = [1,3,5,8,9,2,6,7,6,8,9]
print(steps(arr))