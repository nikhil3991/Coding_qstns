def solve(A):
    n = len(A)
    A.insert(0, 1)
    A.append(1)
    print(A)
    dp = [[0] * (n + 2) for i in range(n + 1)]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                curr = A[i - 1] * A[k] * A[j + 1]
                dp[l][i] = max(dp[l][i], curr + dp[k - i][i] + dp[j - k][k + 1])
        print(dp)
    print(dp[-1][1])
A=[3,1,5,8]
solve(A)