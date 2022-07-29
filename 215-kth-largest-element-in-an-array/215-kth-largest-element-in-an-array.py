def quickSelect(nums, start, end, k):
    pivot = end
    i = start
    j = start
    for j in range(start, pivot):
        if nums[j] < nums[pivot]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[pivot] = nums[pivot], nums[i]
    if i == (len(nums)-k):
        return
    if i < (len(nums)-k):
        quickSelect(nums, i+1, end, k)
    else:
        quickSelect(nums, start, i-1, k)
            

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        quickSelect(nums, 0, len(nums)-1, k)
        return nums[len(nums) - k]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        