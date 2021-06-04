def find(arr,k):
    n = len(arr)
    max_upto = [0 for i in range(n)]
    s=[]
    s.append(0)
    for i in range(1,n):
        while len(s)>0 and arr[s[-1]]<arr[i]:
            max_upto[s[-1]] = i-1
            s.pop()
        s.append(i)
    while len(s)>0:
        max_upto[s[-1]] = n-1
        s.pop()
    print(max_upto)
    j=0
    for i in range(n-k+1):
        while j<i or max_upto[j]<i+k-1:
            j+=1
        print(arr[j])
    print()





arr = [10,15,2,12,78,19,54,15,100,22,13,28]
find(arr,3)