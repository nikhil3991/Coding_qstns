def find(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        table = [0]*(n+1)
        table[1] = 1
        for i in range(2,n+1):
            if i%2 ==0:
                table[i] = table[i//2]
            else:
                table[i] = table[i-1] +1
    print(table)


a = 10
find(a)