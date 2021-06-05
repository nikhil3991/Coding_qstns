def makeConnected(n,connections):
    m = len(connections)
    visited = [False] * n
    g = [[] for i in range(n)]
    arr=set()
    for i in range(m):
        arr.add(connections[i][0])
        arr.add(connections[i][1])
        g[connections[i][0]].append(connections[i][1])
        g[connections[i][1]].append(connections[i][0])

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for j in g[node]:
            dfs(j)

    count = 0
    s= len(arr)
    print(arr)
    print(g)
    visited = [False]*s
    for i in range(s):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)

A=[[0,1],[0,2],[0,3],[1,2]]
makeConnected(6,A)
