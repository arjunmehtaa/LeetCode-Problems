class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            maxSum = max(nums[i], nums[i] + sums[i-1])
            sums.append(maxSum)
        return max(sums)