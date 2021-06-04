import sys

def absolute(A,B):
    A=sorted(A)
    B=sorted(B)
    # m = len(A)
    # n=len(B)
    i=0
    j=0
    minimum = sys.maxsize
    while i<len(A) and j <len(B):
        if A[i]<B[j]:
            minimum = min(B[j]-A[i],minimum)
            i+=1
        else:
            minimum = min(A[i]-B[j],minimum)
            j+=1
    print(minimum)


arr1 = [1,15,11,2]
arr2 = [4,19,17,127,23,235]
absolute(arr1,arr2)