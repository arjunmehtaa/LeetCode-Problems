class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        return dfs(nums, target, memo)
        
def dfs(nums, target, memo):
    if target < 0:
        return 0
    if target == 0:
        return 1
    if target not in memo:
        answer = 0
        for num in nums:
            answer += dfs(nums, target - num, memo)
        memo[target] = answer
    return memo[target]