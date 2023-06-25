class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            numToFind = target - nums[i]
            if nums[i] in map:
                return [i, map[nums[i]]]
            map[numToFind] = i