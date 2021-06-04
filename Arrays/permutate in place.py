def solve(A,B):
    print(A)
    n=len(A)
    for i in range(n):
        index = B[i]
        while index <i:
            index= B[index]
        A[i],A[index] = A[index],A[i]
    print(A)



A = [4,6,2,1,8,9]
B = [2,5,1,0,4,3]
solve(A,B)
