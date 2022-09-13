class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            if nums[i] in numsMap:
                return [i, numsMap[nums[i]]]
            numToFind = target - nums[i]
            numsMap[numToFind] = i
        return 0
        