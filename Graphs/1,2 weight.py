def solve(A, B, C, D):
    n = len(B)
    index = A
    E = []
    for i in range(n):
        if B[i][2] == 2:
            E.append([B[i][0],index,1])
            E.append([index,B[i][1],1])
            index+=1
        else:
            E.append(B[i])
    print(E)
    B=E
    n=len(B)

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

    visited = [False] * (index+ 1)
    parent = [-1] * (index + 1)
    flag = False
    queue = [C]
    print(queue)
    print(temp)
    while queue:
        x = queue.pop(0)
        visited[x] = True
        if x==D:
            flag = True
            break
        if x not in temp.keys():
            continue
        for i in temp[x].keys():
            print(i)
            if not visited[i]:
                queue.append(i)
                if parent[i]==-1:
                    parent[i] = x

                # if i==D:
                #     queue.clear()
                #     break




    if flag == False:
        print(-1)
        return
    count = 0
    node = D
    while node != C:
        x = parent[node]
        print(parent[node],node)
        if x == -1:
            print(count)
            return
        count += temp[x][node]
        node = x
    print(count)
    return


A = 6
B = [   [2, 5, 1],
        [1, 3, 1] ,
        [0, 5, 2] ,
        [0, 2, 2] ,
        [1, 4, 1] ,
        [0, 1, 1] ]
C = 3
D = 2
solve(A,B,C,D)



