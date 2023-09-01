class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            ans = max(ans, currMax)
        return ans
        