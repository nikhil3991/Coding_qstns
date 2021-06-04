def minCut(s: str):
    n = len(s)
    temp = [(i - 1) for i in range(n + 1)]
    print(temp)
    for i in range(n):
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            temp[right + 1] = min(temp[right + 1], temp[left] + 1)
            left -= 1
            right += 1
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            temp[right + 1] = min(temp[right + 1], temp[left] + 1)
            left -= 1
            right += 1
        print(temp)

    print(temp[-1])
s= "aba"
minCut(s)