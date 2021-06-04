def wordBreak(A, B):
    n = len(A)
    print(A)
    m = len(B)
    temp = set()
    for i in range(m):
        temp.add(B[i])
    print(temp)
    dp = [0]*(n + 1)
    dp[0] = 1
    for i in range(1,n + 1):
        for j in range(i):
            if dp[j] and (A[j:i] in temp):
                print(A[j:i])
                dp[i] = 1
    print(dp)
A = "myinterviewtrainer"
B = ["trainer", "my", "interview"]
wordBreak(A,B)
