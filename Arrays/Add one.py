def addOne(A):
    n =len(A)
    carry =1
    s=""
    for i in range(n-1,-1,-1):
        temp = A[i]+carry
        A[i]=temp%10
        carry =temp//10

    if carry == 1:
        A.insert(0,carry)
    i=0
    while (i<len(A)):
        if A[i]==0:
            A.pop((0))
        else:
            break

    for i in range(len(A)):
        s+=str(A[i])
    print(s)
    return A





arr = [ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ]
c = addOne(arr)
print(c)