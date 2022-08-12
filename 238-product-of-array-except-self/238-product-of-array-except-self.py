class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = 1
        postfix = 1
        for i in range(0, n):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(n-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
            
            
        