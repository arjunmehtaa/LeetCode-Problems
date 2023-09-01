class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        ans = nums[0]
        for num in nums:
            temp = minProd
            minProd = min(minProd * num, maxProd * num, num)
            maxProd = max(temp * num, maxProd * num, num)
            ans = max(ans, maxProd)
        return ans