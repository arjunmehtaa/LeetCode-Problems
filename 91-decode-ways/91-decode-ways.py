# Time Complexity	: O(N)
# Space Complexity	: O(N)

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return dfs(s, 0, memo)
        
def dfs(s, i, memo):
    if int(s[0]) == 0:
        return 0
    if (len(s) == 1 and int(s[:1]) >= 1):
        return 1
    if (len(s) == 2 and int(s[:2]) <= 26):
        return 1 + dfs(s[1:], i + 1, memo)
    if i not in memo:
        value1 = int(s[:1])
        value2 = int(s[:2])
        one, two = 0, 0
        if value1 >= 1:
            one = dfs(s[1:], i + 1, memo)
        if value2 <= 26:
            two = dfs(s[2:], i + 2, memo)
        memo[i] = one + two
    return memo[i]
        
        