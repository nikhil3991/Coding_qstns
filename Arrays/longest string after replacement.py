def solve(str,B):
    n = len(str)
    count=0
    left = right =0
    result =-1
    while right<n:
        if count<=B:
            if str[right]=='b':
                count+=1
            right+=1
        if count>B:
            if str[left]=='b':
                count-=1
            left+=1
        if (right-left)>result:
            result = right-left
    return result



m = "aabbabaabaab"
print(solve(m,2))
