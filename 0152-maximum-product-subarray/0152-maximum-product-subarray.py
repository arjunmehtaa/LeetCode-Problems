class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = 1
        minNum = 1
        ans = max(nums)
        for num in nums:
            if num == 0:
                minNum = 1
                maxNum = 1
                continue
            temp = num * maxNum
            maxNum = max(num, num * maxNum, num * minNum)
            minNum = min(num, temp, num *minNum)
            ans = max(ans, maxNum)
        return ans