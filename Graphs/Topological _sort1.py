def solve(A, B,C):
    m = len(B)
    temp = {}
    indegree = [0] * (A + 1)
    # for i in range(m):
    #     try:
    #         temp[B[i][0]].add(B[i][1])
    #     except:
    #         temp[B[i][0]] = set()
    #         temp[B[i][0]].add(B[i][1])
    #     indegree[B[i][1]] += 1
    for i in range(m):
        try:
            temp[B[i]].add(C[i])
        except:
            temp[B[i]] = set()
            temp[B[i]].add(C[i])
        indegree[C[i]] += 1

    q = []
    for i in range(1, A + 1):
        if indegree[i] == 0:
            q.append(i)

    # def utility(temp,node,visited,res):
    #     if visited[node]:
    #         return
    #     visited[node] = True
    #     # res.append(node)
    #     if node not in temp:
    #         return
    #     for i in temp[node]:
    #         utility(temp,i,visited,res)
    #     res.insert(0,node)
    # visited = [False]*(A+1)
    # res=[]
    # for i in q:
    #     if visited[i]==False:
    #         utility(temp,i,visited,res)
    # print(res)
    count = A
    visited = [False] * (A + 1)
    res = []
    while q:
        x = q.pop(0)
        if visited[x]:
            continue
        new_q = [x]
        while new_q:
            y = new_q.pop(0)
            if visited[y]:
                continue
            # print(y)
            res.append(y)
            visited[y] = True
            if y not in temp:
                continue
            for i in temp[y]:
                if visited[i]:
                    continue
                if indegree[i]>0:
                    indegree[i]-=1
                if indegree[i]==0:
                    new_q.append(i)
    print(len(res))
    print(res)


    # while count > 0 and q:
    #     x = q.pop(0)
    #     if visited[x]:
    #         continue
    #     print(x)
    #     res.append(x)
    #     visited[x] = True
    #     count -= 1
    #     if x not in temp:
    #         continue
    #     for i in temp[x]:
    #         if visited[i]:
    #             continue
    #         if indegree[i] > 0:
    #             indegree[i] -= 1
    #         if indegree[i] == 0:
    #             q.insert(0,i)
A =5
B = [ 1, 3, 4, 5 ]
C = [ 2, 1, 5, 3 ]

solve(A,B,C)