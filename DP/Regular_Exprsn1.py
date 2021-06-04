def isMatch(A, B):
    n = len(A)
    m = len(B)
    match = [[False] * (n + 1) for i in range(m + 1)]
    match[0][0] = True
    for i in range(1, m + 1):
        if B[i - 1] == '*' and match[i - 1][0] == True:
            match[i][0] = True
        else:
            match[i][0] = False
    for i in range(1, n + 1):
        match[0][i] = False

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if B[i - 1] == '?':
                match[i][j] = match[i - 1][j - 1]
            elif B[i - 1] != '*':
                if A[j - 1] == B[i - 1]:
                    match[i][j] = match[i - 1][j - 1]
                else:
                    match[i][j] = False
            elif B[i - 1] == '*':
                match[i][j] = match[i - 1][j] | match[i][j - 1]
    print(match)
    for i in match:
        print(i)

    if match[m][n]:
        print(1)
    else:
        print(0)


A = "aaa"
B = "a*"
isMatch(A,B)
A = "acz"
B = "a?a"

