
# --------Brute Force ----------------
def solve(B,k):
    if k==0:
        return 0
    if k==1:
        return max(B[0],B[-1])
    return max((B[0]+solve(B[1:],k-1)),(B[-1]+solve(B[:-1],k-1)))

A = [5,4,-1,100,2,4,5]
k=3
print(solve(A,3))