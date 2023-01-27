class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            toFind = target - nums[i]
            if toFind in map:
                return [map[toFind], i]
            map[nums[i]] = i
