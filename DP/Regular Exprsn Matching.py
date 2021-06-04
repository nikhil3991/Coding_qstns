class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        match = [[False for i in range(n + 1)] for j in range(m + 1)]
        match[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    if i != 0:
                        match[i][j] = match[i - 1][j - 1]
                elif p[j - 1] == '*':
                    temp = p[j - 2]
                    match[i][j] = match[i][j - 2] or (i > 0 and match[i - 1][j] and (s[i - 1] == temp or temp == '.'))
                else:
                    if i != 0 and s[i - 1] == p[j - 1]:
                        match[i][j] = match[i - 1][j - 1]

        print(match[-1][-1])
s = "mississippi"
p = "mis*is*p*."
S=Solution()
S.isMatch(s,p)

