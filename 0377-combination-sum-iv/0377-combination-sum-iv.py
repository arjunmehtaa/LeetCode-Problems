class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def traverse(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if t not in memo:
                possible = 0
                for n in nums:
                    possible += traverse(t - n)
                memo[t] = possible
            return memo[t]
        
        return traverse(target)
            