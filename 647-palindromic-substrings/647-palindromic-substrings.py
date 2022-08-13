class Solution:
    def countSubstrings(self, s):
        if not s:
            return 0

        n = len(s)
        table = [[False for x in range(n)] for y in range(n)]
        count = 0

        # Every isolated char is a palindrome
        for i in range(n):
            table[i][i] = True
            count += 1

        # Check for a window of size 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        # Check windows of size 3 and more
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1

        return count
    
    
    
    
    
    
    
    # def countSubstrings(self, s: str) -> int:
    #     dp = {}
    #     n = len(s)
    #     count = 0
    #     for i in range(0, len(s)):
    #         dp[(i,i)] = True
    #         count += 1
    #     for i in range(0, len(s) - 1):
    #         if s[i] == s[i+1]:
    #             dp[(i, i+1)] = True
    #             count += 1
    #         else:
    #             dp[(i, i+1)] = False
    #     for k in range(3, n + 1):
    #         for i in range(0, n - k + 1):
    #             j = i + k - 1
    #             if dp[(i+1, j-1)] and s[i] == s[j]:
    #                 dp[i, j] = True
    #                 count += 1
    #             else:
    #                 dp[i, j] = False
    #     return count
        
        