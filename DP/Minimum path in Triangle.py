def minimumTotal(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    dp = [[-1] * n for i in range(1, n + 1)]
    # dp[-1][-1] = A[-1][-1]
    for i in range(n - 1, -1, -1):
        dp[-1][i] = A[-1][i]
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            dp[i][j] = A[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    # return dp[0][0]


    print(dp[0][0])

A= [[2],[3,4],[6,5,7],[4,1,8,3]]
minimumTotal(A)
