class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curr_min = 1
        curr_max = 1
        for n in nums:
            if n == 0:
                curr_min = 1
                curr_max = 1
                continue
            temp = n * curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(temp, n * curr_min, n)
            ans = max(ans, curr_max)
        return ans