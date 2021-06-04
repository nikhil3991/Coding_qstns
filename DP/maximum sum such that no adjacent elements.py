def maxsum(arr):
    n = len(arr)
    incl = 0
    excl = 0
    for i in range(n):
        curr_max = excl if excl>incl else incl

        incl = excl + arr[i]
        excl = curr_max
    return excl if excl>incl else incl


arr = [5,5,10,100,10,5]
b=maxsum(arr)
print(b)

