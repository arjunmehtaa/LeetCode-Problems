class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        memo = {}
        return max(dfs(nums, 0, memo), dfs(nums, 1, memo))
        
def dfs(nums, index, memo):
    if index == len(nums) - 1 or index == len(nums) - 2:
        return nums[index]
    if index not in memo:
        answer = 0
        if index + 2 < len(nums):
            answer = max(answer, dfs(nums, index + 2, memo))
        if index + 3 < len(nums):
            answer = max(answer, dfs(nums, index + 3, memo))
        memo[index] = answer
    return nums[index] + memo[index]