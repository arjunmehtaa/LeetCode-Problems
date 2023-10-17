class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return [i, seen[nums[i]]]
            numToFind = target - nums[i]
            seen[numToFind] = i