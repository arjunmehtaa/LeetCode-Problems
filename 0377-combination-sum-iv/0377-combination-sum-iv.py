class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(0, target + 1):
            for num in nums:
                res = 0
                if i - num == 0:
                    dp[i] += 1
                elif num < i:
                    res = dp[i - num]
                    if res >= 1:
                        dp[i] += res
        return dp[target]