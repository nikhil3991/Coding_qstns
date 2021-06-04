def solve(str):
    n=len(str)
    left =right =0
    for i in range(n):
        if str[i] == ')':
            if left==0:
                right+=1
            else:
                left-=1
        else:
            left+=1
    print(right,left)



m = "(())))()(()"
print(solve(m))