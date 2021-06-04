def solve(arr,m):
    n = len(arr)
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                res.append(A[i]+A[j]+A[k])
                # if m==1:
                #     print(arr[i],arr[j],arr[k])
                #     print(arr[i] + arr[j] + arr[k])
                #
                #     return
                # else:
                #     m=m-1
    # res=list(set(res))
    return res


A = [ 22, 10, 5, 11, 16, 2, 11, 7, 16, 2, 17, 6, 15, 3, 9, 6 ]

# A.sort()
print(A)
temp=solve(A,255)
temp.sort()
print(temp[165:189])