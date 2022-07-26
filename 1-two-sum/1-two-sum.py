class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0, len(nums)): 
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                num_to_find = target - nums[i]
                dict[num_to_find] = i
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    