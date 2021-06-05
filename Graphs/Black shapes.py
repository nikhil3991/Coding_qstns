def black(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        A[i] = list(A[i])
    print(A)
    count = 0
    visited = [[False] * n for i in range(m)]

    def isSafe(i, j):
        if (i >= 0 and i < m) and (j >= 0 and j < n):
            return True
        return False

    def dfs(A, i, j, visited):
        ri = [-1, 1, 0, 0]
        ci = [0, 0, -1, 1]
        # ri = [-1, -1, -1,  0, 0,  1, 1, 1]
        # ci = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for p in range(4):
            if isSafe(i + ri[p], j + ci[p]) and A[i + ri[p]][j + ci[p]] == "X" and not visited[i + ri[p]][j + ci[p]]:
                dfs(A, i + ri[p], j + ci[p], visited)

    for r in range(m):
        for c in range(n):
            if visited[r][c] == False and A[r][c] == "X":
                dfs(A, r, c, visited)
                count += 1
    print(count)
A = [ "XOOOOOXXOX", "OOXXXXOOXX", "XXOXXOOXXO", "OXOXXXXXXO", "XOXXOXOXXX", "OOOOOOOXOO", "XOXXXOOXOX", "XXXOXOXXXO" ]
black(A)