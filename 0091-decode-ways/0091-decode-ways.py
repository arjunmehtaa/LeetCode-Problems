class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i + 1]
            if i < len(s) - 1 and int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]
        
        
#     def numDecodings(self, s: str) -> int:
#         memo = {}
#         return traverse(s, 0, memo)
    
# def traverse(s, index, memo):
#     if index == len(s):
#         return 1
#     if index > len(s):
#         return 0
#     if index not in memo:
#         res = 0
#         if int(s[index]) != 0:
#             res += traverse(s, index + 1, memo)
#             if index < len(s) - 1 and int(s[index:index+2]) <= 26:
#                 res += traverse(s, index + 2, memo)
#         memo[index] = res
#     return memo[index]

# Time Complexity	: O(N)
# Space Complexity	: O(N)

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         memo = {}
#         return dfs(s, 0, memo)
        
# def dfs(s, i, memo):#     if int(s[0]) == 0:
#         return 0
#     if (len(s) == 1 and int(s[:1]) >= 1):
#         return 1
#     if (len(s) == 2 and int(s[:2]) <= 26):
#         return 1 + dfs(s[1:], i + 1, memo)
#     if i not in memo:	
#         value1 = int(s[:1])
#         value2 = int(s[:2])
#         one, two = 0, 0
#         if value1 >= 1:
#             one = dfs(s[1:], i + 1, memo)
#         if value2 <= 26:
#             two = dfs(s[2:], i + 2, memo)
#         memo[i] = one + two
#     return memo[i]
        
        