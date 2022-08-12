class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = set()
        for i in range(0, len(nums)):
            if nums[i] in data:
                return True
            else:
                data.add(nums[i])
        return False
        