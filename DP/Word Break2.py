def wordBreak(s,wordDict) -> bool:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] == 1 and s[j:i] in wordDict:
                dp[i] = 1
                break
    if dp[n] == 0:
        return []

    def break_word(s, left, wordDict, memo):
        if left >= len(s):
            return [[]]
        if left in memo:
            return memo[left]
        res = []
        for i in range(left + 1, len(s) + 1):
            if dp[i] == 0:
                continue
            prefix = s[left:i]
            suffix_res = break_word(s, i, wordDict, memo)
            if suffix_res and prefix in wordDict:
                for j in suffix_res:
                    res.append([prefix] + j)
        memo[left] = res[:]
        return res

    memo = {}
    ans = break_word(s, 0, wordDict, memo)
    return [" ".join(x) for x in ans]

# s = "applepenapple"
# wordDict = ["apple", "pen"]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
ans = wordBreak(s,wordDict)
print(ans)

