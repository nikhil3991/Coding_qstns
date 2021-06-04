def Graycode(n):
    if n==0:
        return [0]
    prev = Graycode(n-1)
    lead = 1<<(n-1)
    curr = []
    for i in reversed(prev):
        curr.append(lead|i)
    ans = prev + curr
    return ans



def Graycode1(n):
    res = [0]
    for i in range(n):
        res+=[x + 2**i for x in reversed(res)]
    print(res)

n=4
print(Graycode1(n))
