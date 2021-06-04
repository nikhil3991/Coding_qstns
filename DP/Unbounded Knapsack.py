def solve(A, B, C):
    n = len(B)
    profit = [0] * (A + 1)
    for i in range(A + 1):
        for j in range(n):
            if C[j] <= i:
                profit[i] = max(profit[i], profit[i - C[j]] + B[j])
        print(profit)
    print(profit[A])


A = 10
# B contains value for ith weight
B = [6, 7]
# C contains weight i
C = [5, 5]
solve(A,B,C)