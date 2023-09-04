class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                wordLen = len(word)
                if (i + wordLen) <= len(s) and s[i:i + wordLen] == word and dp[i + wordLen]:
                    dp[i] = True
        return dp[0]
        