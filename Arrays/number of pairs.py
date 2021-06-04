
def solve(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    return solve(n-1)+(n-1)*solve(n-2)


def SolvethroughDP(n):

    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    temp = [0 for i in range(n+1)]
    temp[1]=1
    temp[2]=2
    for i in range(3,n+1):
        temp[i] = temp[i-1] + (i-1)*temp[i-2]
    return temp[n]




m=6
print(solve(4))
print(SolvethroughDP(m))
