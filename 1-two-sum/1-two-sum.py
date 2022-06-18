class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            num_to_find = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == num_to_find:
                    return [i,j]
        return null