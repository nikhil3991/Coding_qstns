def heapsort(A):
    buildheap(A)
    n=len(A)
    # for i in range(n):


    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        minheapify(A,0,i)

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i +1

def right(i):
    return 2*i + 2

def buildheap(A):
    length = len(A)
    start = parent(length-1)
    while start>0:
        minheapify(A,start,length)
        start -=1

def minheapify(A,index,size):
    l = left(index)
    r = right(index)
    if l<size and A[l]<A[index]:
        smallest = l
    else:
        smallest = index
    if r<size and A[r]<A[smallest]:
        smallest = r
    if smallest != index:
        A[smallest],A[index] = A[index],A[smallest]
        minheapify(A,smallest,size)




arr = [1,5,9,8,6,7,4,3,2]
print(arr)
heapsort(arr)
print(arr)