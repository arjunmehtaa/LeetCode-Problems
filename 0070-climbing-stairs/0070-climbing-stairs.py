class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def traverse(index):
            if index == 0:
                return 1
            if index < 0:
                return 0
            if index not in memo:
                memo[index] = traverse(index - 1) + traverse(index - 2)
            return memo[index]
        
        return traverse(n)
            