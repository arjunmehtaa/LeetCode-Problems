class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        ans = nums[0]
        for num in nums:
            temp = currMax
            currMax = max(currMin * num, currMax * num, num)
            currMin = min(currMin * num, temp * num, num)
            ans = max(ans, currMax)
        return ans