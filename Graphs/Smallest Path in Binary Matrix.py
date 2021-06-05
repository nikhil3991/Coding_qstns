def shortestPathBinaryMatrix(grid):
    m = len(grid)
    n = len(grid[0])
    print(A)
    dp = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j]=-1
            else:
                dp[i][j] = 0

    if grid[-1][-1] == 1:
        return -1
    # if grid[-1][-2] and grid[-2][-1] and grid[-2][-1] == 1:
    #     return -1
    dp[-1][-1] = 1
    for i in range(n - 2, -1, -1):
        if grid[-1][i] == 0 and dp[-1][i + 1] > 0:
            dp[-1][i] = dp[-1][i + 1] + 1
    for i in range(m - 2, -1, -1):
        if grid[i][-1] == 0 and dp[i+1][-1] > 0:
            dp[i][-1] = dp[i+1][-1] + 1
    print(dp)
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    print(dp)
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            print(i,j)
            if grid[i][j] == 1:
                continue
            dp[i][j] = 9999999
            for x in range(3):
                if dp[i + dx[x]][j + dy[x]] > 0:
                    dp[i][j] = min(dp[i][j], dp[i + dx[x]][j + dy[x]]+1)

            if dp[i][j] ==9999999:
                dp[i][j]=-1
            print(dp[i][j])

    x = dp[0][0]
    if x > 0:
        print(x)
    else:
        print(-1)

# A= [[0,1],[1,0]]
# A= [[0,0,0],[1,1,0],[1,1,0]]
A= [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]

shortestPathBinaryMatrix(A)