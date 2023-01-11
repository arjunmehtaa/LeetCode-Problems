class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in seen:
                return [i, seen[num_to_find]]
            seen[nums[i]] = i