class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return dfs(s, memo, 0)
        
def dfs(s, memo, i):
    if int(s[0]) == 0:
        return 0
    if len(s) == 1 and int(s) > 0:
        return 1
    elif len(s) == 2 and int(s) <= 26:
        return 1 + dfs(s[1], memo, i + 1)
    if i not in memo:
        val1 = int(s[:1])
        val2 = int(s[:2])
        one, two = 0, 0
        if val1 >= 1:
            one = dfs(s[1:], memo, i + 1)
        if val2 <= 26:
            two = dfs(s[2:], memo, i + 2)
        memo[i] = one + two
    return memo[i]