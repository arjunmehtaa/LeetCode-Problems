class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMin = 1
        currMax = 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = n * currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMin, temp, n)
            ans = max(ans, currMax)
        return ans