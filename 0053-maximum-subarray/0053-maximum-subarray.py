class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        return maxSum
    
    