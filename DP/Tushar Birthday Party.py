def solve(A, B, C):
    n = len(A)
    m = len(B)
    x=999999
    for i in range(m):
        x=min(x,C[i])

    def utility(cap, B, C):
        dp = [[99999]*(m+1) for i in range(cap + 1)]
        for i in range(m+1):
            dp[0][i] = 0
        # for i in range(1,cap+1):
        #     dp[i][0] =999999



        for i in range(1, cap + 1):
            for j in range(1,m+1):

                if B[j-1]<=i:
                    dp[i][j] = min(dp[i][j - 1], dp[i - B[j-1]][j] + C[j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[cap][j]

    count = 0
    for i in range(n):
        count+=utility(A[i],B,C)
    print(count)

A  =[ 2, 3, 1, 5, 4 ]
B  =[ 3, 2, 4, 1 ]
C = [ 1, 2, 5, 10 ]
solve(A,B,C)