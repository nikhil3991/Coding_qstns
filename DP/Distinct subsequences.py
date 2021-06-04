class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        temp = [1 for i in range(n + 1)]
        print(temp)

        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1,m+1):
            for j in range(i,n+1):
                dp[i][j] = dp[i][j-1]
                if s[j-1] == t[i-1]:
                    dp[i][j]+= dp[i-1][j-1]
        print(dp[-1][-1])
        #
        # for i in range(1, m + 1):
        #     subsequence = [0 for j in range(n + 1)]
        #     for j in range(i, n + 1):
        #         subsequence[j] = subsequence[j - 1]
        #         if s[j - 1] == t[i - 1]:
        #             subsequence[j] += temp[j - 1]
        #     print(subsequence,"-"*30)
        #
        #     temp = subsequence
        # print(temp[-1])
s= Solution()
a="rabbbirt"
b ="rabbit"

s.numDistinct(a,b)