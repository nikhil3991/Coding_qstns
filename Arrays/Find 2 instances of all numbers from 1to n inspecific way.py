def fillutil(res,curr,n):
    if curr==0:
        return True
    for i in range(2*n -curr -1):
        if res[i]==0 and res[i+curr+1]==0:
            res[i] = res[i+curr+1] = curr

            if fillutil(res,curr-1,n):
                return True
            res[i] =0
            res[i+curr+1]=0


def fill(n):
    res = [0]*2*n
    if(fillutil(res,n,n)):
        for i in range(2*n):
            print(res[i],end=' ')
    else:
        return False



n = 7
fill(n)