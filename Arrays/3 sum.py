import sys
def threeSumClosest(A, B):
    n = len(A)
    A.sort()
    ans = sys.maxsize
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            temp = A[i] + A[left] + A[right]
            if B - temp == 0:
                return temp
            if (abs(B - temp) < abs(B - ans)):
                ans = temp
            if temp > B:
                right -= 1
            else:
                left += 1
    return ans

A= [-1,2,1,-4]
B=1
s=threeSumClosest(A,B)
print(s)

