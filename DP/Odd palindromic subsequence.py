def solve(A):
    n = len(A)
    dp = [[0 for i in range(n)] for j in range(n)]
    for k in range(n - 1, -1, -1):
        for i in range(n):
            if i + k >= n:
                break
            j = i + k
            if i == 0 and j == n - 1:
                if A[i] == A[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1
            elif A[i] == A[j]:
                if (i - 1) >= 0:
                    dp[i][j] += dp[i - 1][j]
                if (j + 1 <= n - 1):
                    dp[i][j] += dp[i][j + 1]
                if (i - 1 < 0 or j + 1 >= n):
                    dp[i][j] += 1
            elif A[i] != A[j]:
                if (i - 1) >= 0:
                    dp[i][j] += dp[i - 1][j]
                if (j + 1 <= n - 1):
                    dp[i][j] += dp[i][j + 1]
                if (i - 1 >= 0 and j + 1 <= n - 1):
                    dp[i][j] -= dp[i - 1][j + 1]
            # print(dp)
    print(dp)
    res = [0] * n
    for i in range(n):
        if i == 0 or i == n - 1:
            res[i] = 1
        else:
            res[i] = (dp[i - 1][i + 1]) % (10 ** 9 + 7)
    print(res)
A ="ababzz"
solve(A)