# Time Complexity   : O(LOG(N))
# Space Complexity  : O(1)

def binarySearch(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = binarySearch(nums, target, 0, len(nums)-1)
        if position == -1:
            return [-1, -1]
        left = position
        right = position
        temp_l = 0
        temp_r = 0
        while left != -1:
            temp_l = left
            left = binarySearch(nums, target, 0, left-1)
        left = temp_l
        while right != -1:
            temp_r = right
            right = binarySearch(nums, target, right+1, len(nums)-1)
        right = temp_r
        return [left, right]
        
        