class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(0, len(nums)):
            temp = nums[i]
            ans[i] = pre
            pre *= temp
        print(ans)
        for i in range(len(nums) - 1, -1, -1):
            temp = nums[i]
            ans[i] *= post
            post *= temp
        return ans