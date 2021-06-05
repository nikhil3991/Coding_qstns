import heapq
def solve(A, B, C, D):
    n = len(B)
    temp = {}
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

    queue = [(0,C)]
    heapq.heapify(queue)
    visited = [False] * (A + 1)
    parent = [-1] * (A + 1)
    flag = False
    next_level = []
    while queue:
        y,x= heapq.heappop(queue)
        print(x)
        visited[x] = True
        if x == D:
            flag = True
            break
        if x not in temp:
            continue
        for i in temp[x]:
            if not visited[i] :
                next_level.append((temp[x][i],i))
                parent[i] = x
        if len(queue)==0:
            queue,next_level = next_level,queue
            heapq.heapify(queue)
    if flag == False:
        print(-1)
        return
    print("-"*40)
    count = 0
    node = D
    print(parent)
    while node != C:

        x = parent[node]
        # print(x)
        count += temp[x][node]
        node = x
    return count
# A = 12
# B = [
#   [4, 5, 2],
#   [7, 11, 1],
#   [1, 4, 1],
#   [6, 9, 2],
#   [0, 2, 1],
#   [1, 7, 1],
#   [4, 10, 1],
#   [10, 11, 1],
#   [7, 9, 2],
#   [1, 11, 1]
# ]
# C = 6
# D = 5
A = 5
B = [
  [0, 2, 1],
  [0, 4, 2],
  [1, 3, 1],
  [1, 4, 1],
  [0, 1, 1],
  [2, 4, 1],
  [3, 4, 2],
  [1, 2, 1]
]
C = 1
D = 3
print(solve(A,B,C,D))