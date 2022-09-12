class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [None] * len(nums)
        post[-1] = 1
        for i in range(1, len(nums)):
            pre.append(pre[i-1]*nums[i-1])
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        for i in range(len(nums)):
            nums[i] = pre[i] * post[i]
        return nums