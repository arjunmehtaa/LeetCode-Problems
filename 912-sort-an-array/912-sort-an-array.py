def quickSort(nums: List[int], start, end):
    if end <= start:
        return
    mid = (end + start)//2
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
    quickSort(nums, start, i-1)
    quickSort(nums, i+1, end)
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quickSort(nums, 0, len(nums) - 1)
        return nums
           
# Insertion Sort
# Performs good when list is almost sorted
# Time Complexity (Best Case)   : O(N)
# Time Complexity (Worst Case)  : O(N^2)
# Space Complexity              : O(1)
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(0, len(nums)):
#             if nums[i] < nums[0]:
#                 a = nums.pop(i)
#                 nums.insert(0, a)
#             else:
#                 for j in range(0, i):
#                     if nums[i] >= nums[j-1] and nums[i] <= nums[j]:
#                         a = nums.pop(i)
#                         nums.insert(j, a)
#         return nums
        
# Selection Sort
# Time Complexity   : O(N^2)
# Space Complexity  : O(1)
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(0, len(nums)):
#             min_index = i
#             for j in range(i, len(nums)):
#                 if nums[j] < nums[min_index]:
#                     min_index = j
#             temp = nums[i]
#             nums[i] = nums[min_index]
#             nums[min_index] = temp
#         return nums
        
# Bubble Sort
# Time Complexity   : O(N^2)
# Space Complexity  : O(1)
#
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)-1, -1, -1):
#             for j in range(0, i):
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#         return nums