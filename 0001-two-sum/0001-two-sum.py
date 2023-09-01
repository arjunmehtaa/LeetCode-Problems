class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [i, map[nums[i]]]
            numToFind = target - nums[i]
            map[numToFind] = i
            
        