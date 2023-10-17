class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        ans = nums[0]
        for i in range(len(nums)):
            temp = currMin
            currMin = min(nums[i] * currMin, nums[i] * currMax, nums[i])
            currMax = max(nums[i] * temp, nums[i] * currMax, nums[i])
            ans = max(ans, currMax)
        return ans