def quickSelect(nums: List[int], start, end, k):
    if end <= start:
        return
    mid = (end + start) // 2
    pivot = end
    nums[mid], nums[pivot] = nums[pivot], nums[mid]
    i = start
    j = start
    while(j != pivot):
        if(nums[j] < nums[pivot]):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            j += 1
    nums[i], nums[pivot] = nums[pivot], nums[i]
    if i == len(nums) - k:
        return
    elif i > len(nums) - k:
        quickSelect(nums, start, i-1, k)
    else: 
        quickSelect(nums, i+1, end, k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        quickSelect(nums, 0, len(nums) - 1, k)
        return nums[len(nums) - k]
