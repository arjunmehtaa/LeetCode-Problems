class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        mini = 1
        maxi = 1
        for n in nums:
            temp = n * maxi
            maxi = max(n, n*maxi, n*mini)
            mini = min(temp, n, n*mini)
            ans = max(ans, maxi)
        return ans
    
# 1 0 2 -1 3 2 -2
