def solve(A, B, C, D, E, F):
    n = len(E)
    visited = [[False]*(B + 1) for i in range(A + 1)]
    print(visited)
    queue = []
    for i in range(n):
        queue.append(((E[i], F[i]), (E[i], F[i])))
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def isSafe(x, y):
        if x >= 0 and x < A and y >= 0 and y < B:
            return True
        return False

    def dist(x, y, a, b):
        return (a - x) ** 2 + (b - y) ** 2

    while queue:
        temp, node = queue.pop(0)
        print(temp)
        if visited[temp[0]][temp[1]]:
            continue
        visited[temp[0]][temp[1]] = True
        for i in range(8):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if isSafe(nx, ny) and visited[nx][ny] and dist(nx, ny, node[0], node[1]) <= D * D:
                queue.append(((nx, ny), node))
    if visited[A][B] == True:
        return "NO"
    q = [(0, 0)]
    while q:
        temp = q.pop(0)
        if visited[temp[0]][temp[1]]:
            continue
        x = temp[0]
        y = temp[1]
        if x == A and y == B:
            return "YES"
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if isSafe(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
    if visited[A][B]:
        return "YES"
    else:
        return "NO"

A = 2
B =3
C = 1
D = 1
E = [ 2 ]
F = [ 3 ]
print(solve(A,B,C,D,E,F))







