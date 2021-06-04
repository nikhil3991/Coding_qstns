
def LCS(a,b,m,n):
    if m==0 or n==0:
        return 0
    table = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                table[i][j]=0
            elif a[i-1]==b[j-1]:
                table[i][j]= table[i-1][j-1] +1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    k = len(table)
    for i in range(k):
        print(table[i])
    return table[m][n]


a = 'ABCDGH'
b = 'AEDFHR'
# b = 'ACGH'
m = len(a)
n =len(b)
print(LCS(a,b,m,n))
