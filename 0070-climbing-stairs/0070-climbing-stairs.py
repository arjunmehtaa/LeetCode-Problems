class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def traverse(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i not in memo:
                memo[i] = traverse(i - 1) + traverse(i - 2)
            return memo[i]
        
        return traverse(n)