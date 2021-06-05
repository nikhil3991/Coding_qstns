def solve(A, B, C):
    n = len(A)
    temp = {}
    for i in range(1, n):
        try:
            temp[A[i]].add(i + 1)
        except:
            temp[A[i]] = set()
            temp[A[i]].add(i + 1)
    if C not in temp.keys():
        return 0
    visited = [False] * (n + 1)

    def dfs(s, t, visited, temp,ans):
        print(s)
        # if s not in temp:
        #     return
        if s == t:
            ans[0] = True
            return
        if s not in temp:
            return
        visited[s] = True
        for i in temp[s]:
            if not visited[i]:
                dfs(i, t, visited, temp,ans)
        return

    ans = [False]
    dfs(C, B, visited, temp,ans)
    if ans[0]:
        print(1)
    else:
        print(0)
A = [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
B=9
C=1
solve(A,B,C)