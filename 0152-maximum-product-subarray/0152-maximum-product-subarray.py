class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        minProd = 1
        maxProd = 1
        for num in nums:
            temp = minProd
            minProd = min(num, num * minProd, num * maxProd)
            maxProd = max(num, num * temp, num * maxProd)
            ans = max(ans, maxProd)
        return ans