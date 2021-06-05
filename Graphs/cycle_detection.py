def solve(A, B):
    n = len(B)
    data = {}
    for i in range(n):
        try:
            data[B[i][0]].add(B[i][1])
        except:
            data[B[i][0]] = set()
            data[B[i][0]].add(B[i][1])
    print(data, end=" ")

    def dfs(data, start, visited, recurstack):
        visited[start] = True
        recurstack[start] = True
        print(start, end=" ")
        if start not in data:
            return False
        for i in data[start]:
            if visited[i] == False:
                if dfs(data, i, visited, recurstack) == True:
                    return True
            elif recurstack[i] == True:
                return True
        # visited[start] = False
        recurstack[start] = False
        return False
    visited = [False] * (A + 1)
    recurstack = [False] * (A + 1)

    for i in range(1, A + 1):
        if visited[i] == False:
            if dfs(data, i, visited, recurstack) == True:
                print(1)
                return
    print(0)

A=5
B=[  [1, 2] ,
        [4, 1],
        [2, 4] ,
        [3, 4] ,
        [5, 2] ,
        [1, 3] ]
solve(A,B)