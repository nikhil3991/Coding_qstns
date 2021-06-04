def solve(A, B, C, D):
    n = len(A)
    for i in range(n):
        B[i]*= A[i]
    # ---------------------------------
    A=D
    profit = [0] * (A + 1)
    for i in range(A + 1):
        for j in range(n):
            if C[j] <= i:
                profit[i] = max(profit[i], profit[i - C[j]] + B[j])
    print(profit)
    print(profit[A])
A = [1, 2, 3]
B = [2, 2, 10]
C = [2, 3, 9]
D = 8
solve(A,B,C,D)