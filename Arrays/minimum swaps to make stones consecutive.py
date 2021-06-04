def solve(A):
    A.sort()
    n = len(A)
    if n == 1:
        return [0, 0]
    total_gaps = A[-1] - A[0] - n + 1
    q = []
    res = n
    for i in A:
        q.append(i)
        while i - q[0] >= n:
            q.pop(0)
        rem = n - len(q)
        if rem == 1 and q[0] != i - n + 1:
            rem = 2

        res = min(res, rem)
    temp = min(A[1] - A[0] - 1, A[-1] - A[-2] - 1)
    maxi = total_gaps - temp
    return [res, maxi]
A=[1,3,8,17]
print(solve(A))