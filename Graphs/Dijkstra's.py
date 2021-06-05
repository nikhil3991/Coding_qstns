import heapq
def solve(A, B, C):
    n = len(B)
    temp = {}
    dist = [(999999, i) for i in range(A)]
    # ans ={}
    # for i in range(A):
    #     ans[i] = 999999
    # ans[C] = 0
    for i in range(n):
        try:
            temp[B[i][0]][B[i][1]] = B[i][2]
        except:
            temp[B[i][0]] = {}
            temp[B[i][0]][B[i][1]] = B[i][2]
        try:
            temp[B[i][1]][B[i][0]] = B[i][2]
        except:
            temp[B[i][1]] = {}
            temp[B[i][1]][B[i][0]] = B[i][2]
    if C not in temp:

        dist[C] = (0,C)
        return dist
    dist[C] = (0,C)
    visited = [False] * A

    def utility(dist, visited):
        ans = 999999
        index = 0
        for i in range(0, len(dist)):
            if visited[i]:
                continue
            if ans > dist[i]:
                ans = dist[i]
                index = i
        return index
    print(dist)
    heapq.heapify(dist)
    ans = [999999 for i in range(A)]
    ans[C] = 0

    for i in range(A):
        val, node = heapq.heappop(dist)
        visited[node] = True
        if val<ans[node]:
            ans[node] = val
        # ans[node] = val
        print(node)
        # heapq.heappush(dist,(999999,node))
        if node not in temp:
            continue
        for v in temp[node]:
            print(v,"-",end = ' ')
            if visited[v]:
                print(ans[v])
                continue
            if ans[v] > ans[node]+temp[node][v]:
                ans[v] = ans[node]+temp[node][v]
                heapq.heappush(dist,(ans[v],v))
            print(ans[v])

    print(dist)
    print(ans)


A = 8
B = [
  [0, 2, 4],
  [1, 2, 10],
  [5, 7, 4],
  [2, 3, 6],
  [3, 7, 2],
  [0, 5, 2]
]
C = 7

solve(A,B,C)