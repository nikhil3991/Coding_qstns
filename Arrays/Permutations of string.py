
def solve(str,l,r,temp):
    if l==r:
        # temp.append(str)

        print("".join(k for k in str))

    for i in range(l,r+1):
        str[l],str[i] = str[i],str[l]
        solve(str,l+1,r,temp)

        str[l],str[i] = str[i],str[l]




str = "ABC"
res=set()
a = list(str)
n=len(a)
temp = []
solve(a,0,n-1,temp)
print(temp)

# print(res)