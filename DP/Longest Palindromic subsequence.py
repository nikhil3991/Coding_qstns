def LPS(A):
    n = len(A)
    if A == A[::-1]:
        return n

    # Solution 1 with space of n^2
    dp = [[0]*(n) for i in range(n+1)]
    for i in range(n):
        dp[1][i] = 1
    for i in range(2,n+1):
        for j in range(n-i+1):
            if A[j] == A[j+i-1]:
                dp[i][j] = 2 + dp[i-2][j+1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j+1])

    print(dp)
    for i in range(len(dp)):
        print(dp[i])
    print(dp[-1][0])

    temp1 = [1 for i in range(n)]
    temp2 = [0 for i in range(n)]

    # Solution 2 with space of n
    for i in range(2, n + 1):
        temp = []
        for j in range(n - i + 1):
            if A[j] == A[j + i - 1]:
                temp.append(2 + temp2[j + 1])
            else:
                temp.append(max(temp1[j], temp1[j + 1]))
        temp2 = temp1
        temp1 = temp

    print( temp[0])
A= "abac"
LPS(A)
