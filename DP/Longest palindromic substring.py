class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s[0]
        dp = [[0] * n for i in range(n)]
        max_ans = 1
        for i in range(n):
            dp[i][i] = 1
        res = s[0]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                if max_ans < 2:
                    max_ans = 2
                    res = s[i:i + 2]

        k = 3
        while k <= n:
            for i in range(n - k + 1):
                if s[i] == s[i + k - 1] and dp[i + 1][i + k - 2] == 1:
                    dp[i][i + k - 1] = 1
                    if max_ans < k:
                        max_ans = k
                        res = s[i:i + k]

            k += 1
        print(dp)
        print(res)

s=Solution()
A= "caaaba"
s.longestPalindrome(A)