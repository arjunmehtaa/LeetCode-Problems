class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            if nums[i - 2] > nums[i - 1]:
                nums[i - 1] = nums[i - 2]
        return max(nums[len(nums) - 2], nums[len(nums) - 1])