def solve(a,b):
    if a==0 and b==0:
        return 0
    if a==0:
        return 1
    if b==0:
        return 1
    return solve(a-1,b) + solve(a,b-1)

def solve1(a,b):
    if a==0 and b==0:
        return 0
    if a==0:
        return b
    if b==0:
        return a
    temp = [0 for i in range(a+b+1)]
    temp[1]=1
    for i in range(2,a+b+1):
        temp[i]=temp[i-1]*i
    return (temp[a+b])//(temp[a] + temp[b])

# def solve2(a):
#     if a==0:
#         return 0
#     temp = [0 for i in range(a+1)]
#




m=2
n=2
k=4
print(solve(m,n))
print(solve1(m,n))
# print(solve2(k))