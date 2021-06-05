def solve(A, B):
    n = len(A)
    m = len(B)
    if n == 0:
        return 0
    temp = {}
    for i in range(m):
        try:
            temp[B[i][0]].add(B[i][1])
        except:
            temp[B[i][0]] = set()
            temp[B[i][0]].add(B[i][1])


    def utility(root, ans, temp,visited):
        print(A[root-1])
        if root not in temp:
            return A[root - 1], A[root - 1]
        visited[root] =True
        x = 9999999
        y = -999999
        for i in temp[root]:
            if visited[i]:
                continue
            tempx, tempy = utility(i, ans, temp,visited)
            ans[0] = max(abs(A[root - 1] - tempx), abs(A[root - 1] - tempy), ans[0])
            x = min(tempx, A[root - 1], x)
            y = max(tempy, A[root - 1], y)
        return x, y

    ans = [-999999]
    visited =[False]*(n+1)
    for i in range(1,n+1):
        if visited[i]:
            continue
        utility(i, ans, temp, visited)

    print(ans[0])

A = [10, 5, 12, 6]
B= [  [1, 2],
        [1, 4],
        [4, 3]
     ]
solve(A,B)
