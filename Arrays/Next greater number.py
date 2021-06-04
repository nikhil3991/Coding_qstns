def nextgreater(a):
    n = len(a)
    for i in range(n-1,-1,-1):
        if a[i]>a[i-1]:
            break
    if i==0:
        print("Not Possible")
        return
    x= a[i-1]
    smallest =i
    for j in range(i+1,n):

        if a[j]<a[smallest] and a[j]>x:
            smallest = j
    a[i-1],a[smallest] = a[smallest],a[i-1]
    X=0
    for j in range(i):
        X= X*10 + a[j]
    a = sorted(a[i:])
    for j in range(n-i):
        X=X*10 + a[j]
    print(X)
inp = "1432"
number =[0]*len(inp)
for i in range(len(inp)):
   number[i] = int(inp[i])
print(number)
nextgreater(number)


