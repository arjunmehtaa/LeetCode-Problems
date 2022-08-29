class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

# Alternate Solution
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         for i in range(2, len(nums)):
#             nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
#             if nums[i - 2] > nums[i - 1]:
#                 nums[i - 1] = nums[i - 2]
#         return max(nums[len(nums) - 2], nums[len(nums) - 1])