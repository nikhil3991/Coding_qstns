import heapq
class Cell:
    def __init__(self,a,b):
        self.i = a
        self.j = b
def solve(A, B):
    m = len(A)
    n = len(B)
    temp = {}
    arr=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            arr[i][j] = Cell(i,j)
    q = []
    ans = {}
    q.append(arr[0][0])
    visited = {}
    for i in range(m + 1):
        for j in range(n + 1):
            visited[arr[i][j]] = False
            ans[arr[i][j]] = 9999999
    while q:
        node = q.pop(0)
        x = node.i
        y=node.j
        if (x + 1) <= m:
            try:
                temp[arr[x][y]][arr[x+1][y]] = A[x]
            except:
                temp[arr[x][y]]= {}
                temp[arr[x][y]][arr[x + 1][y]] = A[x]

            try:
                temp[arr[x+1][y]][arr[x][y]] = A[x]
            except:
                temp[arr[x + 1][y]] = {}
                temp[arr[x + 1][y]][arr[x][y]] = A[x]
            q.append(arr[x+1][y])

        if (y + 1) <= n:
            try:
                temp[arr[x][y]][arr[x][y+1]] = B[y]
            except:
                temp[arr[x][y]] = {}
                temp[arr[x][y]][arr[x][y + 1]] = B[y]

            try:
                temp[arr[x][y+1]][arr[x][y]]= B[y]
            except:
                temp[arr[x][y + 1]] = {}
                temp[arr[x][y + 1]][arr[x][y]] = B[y]
            q.append(arr[x][y+1])
    ans[arr[0][0]]=0
    q.clear()
    count = (m + 1) * (n + 1)
    q.append((0, (0,arr[0][0])))
    cost = 0
    index=1
    heapq.heapify(q)
    while count > 0 and q:
        dist, m = heapq.heappop(q)
        cell = m[1]
        if visited[cell]:
            continue
        count -= 1
        visited[cell] = True
        cost += dist
        if cell not in temp:
            continue
        for neighbour in temp[cell]:
            if visited[neighbour]:
                continue
            # heapq.heappush(q,(temp[cell][neighbour], (index,neighbour)))
            # index+=1
            if ans[neighbour] > temp[cell][neighbour]:
                heapq.heappush(q,(temp[cell][neighbour],(index,neighbour)))
                index+=1
                ans[neighbour] = temp[cell][neighbour]
    print(cost)
A=[1,3]
B=[5,4]
solve(A,B)
