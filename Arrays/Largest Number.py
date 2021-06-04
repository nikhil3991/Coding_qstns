from collections import defaultdict


def largestNumber(A):
    n = len(A)
    A = list(A)
    max_ele = A[0]
    for i in range(1, n):
        max_ele = max(max_ele, A[i])
    print(max_ele)
    l = len(str(max_ele)) + 1
    print(l)
    # temp = [0] * n
    temp = {}
    for i in range(n):

        try:
            val = temp[A[i]]
        except:

            temp[A[i]] = str(A[i]) * l
            a=temp[A[i]]
            temp[A[i]] = a[:l]
    for i in temp.keys():
        print(i,temp[i])

    A.sort(key=lambda m: temp[m], reverse=True)
    return "".join(str(i) for i in A)



Arr = [121,12,5]

print(largestNumber(Arr))

