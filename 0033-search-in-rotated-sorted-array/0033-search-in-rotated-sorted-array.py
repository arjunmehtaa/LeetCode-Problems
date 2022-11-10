# Time Complexity	: O(LOG(N))
# Space Complexity	: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
                
                
        