class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)
            
        def traverse(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i not in memo:
                memo[i] = 0
                if int(s[i]) > 0:
                    memo[i] = traverse(i + 1)
                    if i < n - 1 and int(s[i:i + 2]) <= 26:
                        memo[i] += traverse(i + 2)
            return memo[i]
                                  
        return traverse(0)
        
        
        
        
        
        
        
        
        
        
        # n = len(s)
        # dp = [1] * (n + 1)
        # dp[n] = 1
        # if s[0] == "0" or "00" in s:
        #     return 0
        # for i in range(n - 1, -1, -1):
        #     int_val = int(s[i])
        #     if (i < n - 1 and (int_val == 1 or (int_val == 2 and int(s[i + 1]) <= 6))):
        #         if int(s[i + 1]) == 0:
        #             dp[i] = dp[i + 1]
        #         else:
        #             dp[i] = 1 + dp[i + 1]
        #     elif int(s[i]) > 0:
        #         dp[i] = dp[i + 1]
        # return dp[0]
        