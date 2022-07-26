class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_find = {}
        for i in range(0, len(nums)):
            if nums[i] in nums_to_find:
                return [i, nums_to_find[nums[i]]]
            else:
                diff = target - nums[i]
                nums_to_find[diff] = i
        return None
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for i in range(0, len(nums)): 
#             if nums[i] in dict:
#                 return [dict[nums[i]], i]
#             else:
#                 num_to_find = target - nums[i]
#                 dict[num_to_find] = i
#         return None
    
    
    
    
    
    
    
    
    
    
    
    
    