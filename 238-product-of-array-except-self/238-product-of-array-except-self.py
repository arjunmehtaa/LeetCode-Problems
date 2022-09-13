class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pre, post = 1, 1
        for i in range(0, len(nums)):
            answer.append(pre)
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        return answer