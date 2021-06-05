def findCircleNum(M):
    n = len(M)
    parent = [i for i in range(n)]
    parent = [-1]*n
    def utility1(x):
        if parent[x]==-1:
            return x
        a = utility1(parent[x])
        parent[x] = a
        return a
    #
    def utility(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(1, n):
        for j in range(i):
            if M[i][j] == 1:
                parent[utility1(i)] = utility1(j)
    print(parent)
    count = 0
    res = set()
    for i in range(n):
        res.add(utility1(i))
    print(res)
A=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
findCircleNum(A)