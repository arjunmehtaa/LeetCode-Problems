class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        return len(nums) != len(numSet)