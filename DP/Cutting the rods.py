def cutting(price):
    n= len(price)
    table = [0 for i in range(n+1)]
    # print(table)
    for i in range(1,n+1):
        maxval = 0
        for j in range(i):
            maxval = max(maxval,price[j] + table[i-j-1])
        table[i] = maxval
    print(table)
    print(table[n])





arr = [1, 5, 8, 9, 10, 17, 17, 20]
cutting(arr)