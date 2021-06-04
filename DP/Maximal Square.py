class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        # print("Hello")
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            print(matrix[i])
        ans =0
        temp = [0]*n
        dp =[[0]*n for i in range(m)]
        print(temp)
        for i in range(m):

            dp[i][0] = int(matrix[i][0])
            for j in range(1,n):
                if matrix[i][j] == '1':
                    # dont check if i=0
                    dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
            ans = max(ans,max(dp[i]))

        print(ans**2)

A = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(A)
s=Solution()
s.maximalSquare(A)