class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMin = 1
        currMax = 1
        for n in nums:
            temp = n * currMax
            currMax = max(n * currMin, n * currMax, n)
            currMin = min(n * currMin, temp, n)
            ans = max(ans, currMax)
        return ans