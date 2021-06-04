def uniquePathsWithObstacles(obstacleGrid):
    A = obstacleGrid
    n = len(A[0])
    m = len(A)
    ways = [[0] * n for i in range(m)]
    if A[m - 1][n - 2] == 0:
        ways[m - 1][n - 2] = 1
    if A[m - 2][n - 1] == 0:
        ways[m - 2][n - 1] = 1
    for i in range(m - 3, -1, -1):
        if A[i][n - 1] == 0:
            ways[i][n - 1] = ways[i + 1][n - 1]
    for i in range(n - 3, -1, -1):
        if A[m - 1][i] == 0:
            ways[m - 1][i] = ways[m - 1][i+1]
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if A[i][j] == 0:
                ways[i][j] = ways[i][j + 1] + ways[i + 1][j]
    print(ways)
    print(ways[0][0])
A= [[0,0,0],[0,1,0],[0,0,0]]
uniquePathsWithObstacles(A)