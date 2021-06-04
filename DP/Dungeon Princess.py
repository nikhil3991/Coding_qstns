def calculateMinimumHP(A):
    m = len(A)
    n = len(A[0])
    cost = [[0] * (n + 1) for i in range(m + 1)]
    if A[m - 1][n - 1] > 0:
        cost[m - 1][n - 1] = 1
    else:
        cost[m - 1][n - 1] = 1 - A[m - 1][n - 1]
    for i in range(m - 2, -1, -1):
        cost[i][n - 1] = max(cost[i + 1][n - 1] - A[i][n - 1], 1)
    for i in range(n - 2, -1, -1):
        cost[m - 1][i] = max(cost[m - 1][i + 1] - A[m - 1][i], 1)
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            temp = min(cost[i][j + 1], cost[i + 1][j])
            cost[i][j] = max(temp - A[i][j], 1)
    print(cost)
    print(cost[0][0])

A = [[-2,-3,3],
     [-5,-10,1],
     [10,30,-5]]
calculateMinimumHP(A)