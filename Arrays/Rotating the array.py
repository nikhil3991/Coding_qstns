def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def rotateArr(arr,d):
    n=len(arr)
    g =gcd(d,n)
    print(g)
    for i in range(g):
        temp = arr[i]
        j=i
        while 1:
            k = j+d
            if k>=n:
                k=k-n
            if k==i:
                break
            arr[j] = arr[k]
            j=k
        arr[j] = temp


def reverse(arr,low,high):
    if low<high:
        n = (low+high)//2
        print(n)
        for i in range(n):
            arr[low+i],arr[high-i] = arr[high-i],arr[low+i]
    print(arr)








A = [1,2,3,4,5,6,7,8,9,10,11,12]
reverse(A,0,len(A)-1)

rotateArr(A,3)

print(A)




