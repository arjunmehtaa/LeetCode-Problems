def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
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
        position = binarySearch(nums, target)
        if position == -1:
            return [-1, -1]
        left = position
        right = position
        while left >= 0 and nums[left] == target:
            left -= 1
        while right <= len(nums)-1 and nums[right] == target:
            right += 1
        return [left + 1, right - 1]
        