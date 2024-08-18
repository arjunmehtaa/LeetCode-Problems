class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        one, two = 0, 0
        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + two, one)
            two = one
            one = dp[i]
        return dp[0]
