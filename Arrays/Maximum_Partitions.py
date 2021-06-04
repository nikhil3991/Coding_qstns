def solve(A):
    n = len(A)
    print(A)
    if n == 1:
        return 1
    prefix = [-1] * n
    suffix = [-1] * n
    prefix[0] = A[0]
    suffix[-1] = A[-1]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], A[i])
    for i in range(n - 2, -1, -1):
        suffix[i] = min(suffix[i + 1], A[i])
    print(prefix)
    print(suffix)
    count = 0
    if A[0] <= suffix[1]:
        count += 1
    for i in range(n - 1):
        if prefix[i]<=suffix[i+1]:
            count+=1
        # if A[i] >= prefix[i - 1] and A[i] <= suffix[i + 1]:
        #     count += 1
    if n > 1:
        if A[-1] >= prefix[-2]:
            count += 1
    return count

A =[ 4, 1, 8, 8, 6, 10, 10, 10, 11, 9, 14, 15, 14, 17, 19, 17 ]
ans = solve(A)
print(ans)