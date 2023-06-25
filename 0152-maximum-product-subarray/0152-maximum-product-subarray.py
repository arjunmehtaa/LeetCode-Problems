class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = 1
        maxProd = 1
        ans = max(nums)
        for num in nums:
            if num == 0:
                minProd = 1
                maxProd = 1
            temp = minProd
            minProd = min(num, minProd * num, maxProd * num)
            maxProd = max(num, temp * num, maxProd * num)
            ans = max(ans, maxProd)
        return ans
        