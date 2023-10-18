class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                r = mid
            else:
                if nums[r] < nums[l]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]