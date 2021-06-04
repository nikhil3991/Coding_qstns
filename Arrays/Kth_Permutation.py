def getPermutation(A, B):
    A = [(i + 1) for i in range(A)]

    def factorial(x):
        count = 1
        for i in range(x, 0, -1):
            count = count * i
        return count

    def utility(A, rem):
        if rem == 0:
            return "".join(str(i) for i in A)
        n=len(A)
        m=factorial(n-1)
        temp=rem//m
        rem = rem%m
        y=A.pop(temp)
        return str(y) + utility(A,rem)




    ans = utility(A,B - 1)
    return ans

print(getPermutation(4,6))

