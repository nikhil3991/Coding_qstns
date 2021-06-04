def isInterleave(s1,s2,s3):
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)

    def utility(s1, s2, s3, index1, index2, dp):
        if n1 <= index1 or n2 <= index2:
            return s1[index1:] + s2[index2:] == s3[index1 + index2:]
        if (index1, index2) in dp:
            return dp[(index1, index2)]
        ans = False
        if s1[index1] == s3[index1 + index2] and utility(s1, s2, s3, index1 + 1, index2, dp):
            ans = True
        elif s2[index2] == s3[index1 + index2] and utility(s1, s2, s3, index1, index2 + 1, dp):
            ans = True
        dp[(index1, index2)] = ans
        return ans

    if (n1 + n2) != n3:
        return False
    return utility(s1, s2, s3, 0, 0, {})

    # -------Java 2D program for interleaving string ---------------
    # public boolean isInterleave(String s1, String s2, String s3) {
    #     if (s3.length() != s1.length() + s2.length()) {
    #         return false;
    #     }
    #     boolean dp[][] = new boolean[s1.length() + 1][s2.length() + 1];
    #     for (int i = 0; i <= s1.length(); i++) {
    #         for (int j = 0; j <= s2.length(); j++) {
    #             if (i == 0 && j == 0) {
    #                 dp[i][j] = true;
    #             } else if (i == 0) {
    #                 dp[i][j] = dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1);
    #             } else if (j == 0) {
    #                 dp[i][j] = dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1);
    #             } else {
    #                 dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) || (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));
    #             }
    #         }
    #     }
    #     return dp[s1.length()][s2.length()];
    # }


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1,s2,s3))