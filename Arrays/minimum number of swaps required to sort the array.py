def minswaps(arr,n):
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it:it[1])
    print(arrpos)
    visited = [False]*n
    res=0
    for i in range(n):
        if visited[i] or arrpos[i][0]==i:
            continue
        j=i
        cycle_size = 0
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0]
            cycle_size+=1
        if cycle_size>0:
            res+=cycle_size-1
    return res

arr = [1,5,4,3,2]
print(minswaps(arr,len(arr)))
