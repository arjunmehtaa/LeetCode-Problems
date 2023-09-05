class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return traverse(s, 0, memo)
    
def traverse(s, index, memo):
    if index == len(s):
        return 1
    if index > len(s):
        return 0
    if index not in memo:
        res = 0
        if int(s[index]) != 0:
            res += traverse(s, index + 1, memo)
            if index < len(s) - 1 and int(s[index:index+2]) <= 26:
                res += traverse(s, index + 2, memo)
        memo[index] = res
    return memo[index]