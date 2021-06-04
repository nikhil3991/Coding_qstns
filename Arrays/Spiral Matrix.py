
def Spiral(a):
    m= a
    n=a
    B =[[0]*a for j in range(a)]
    k= 0
    l=0
    val=1
    while k<m and l<n:
        for i in range(l,n):
            B[k][i] = val
            val+=1

        k+=1
        for i in range(k,m):
            B[i][n-1] = val
            val+=1
        n-=1

        if k<m:
            for i in range(n-1,(l-1),-1):
                B[m-1][i] = val
                val+=1
            m-=1
        if l<n:
            for i in range(m-1,k-1,-1):
                B[i][l] = val
                val+=1
            l+=1
    print(B)

Spiral(2)



