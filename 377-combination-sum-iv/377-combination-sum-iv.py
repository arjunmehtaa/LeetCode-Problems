class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]
        
# DFS + Memoization Solution
#
# Let N be the target value and M be the size of nums array
# Time Complexity	: O(N*M)
# Space Complexity	: O(N*M)
#
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         res = 0
#         ans = 0
#         memo = {}
#         for num in nums:
#             res += dfs(nums, num, ans, target, memo)
#         return res
        
# def dfs(nums, num, ans, target, memo):
#     ans += num
#     if ans == target:
#         return 1
#     elif ans > target:
#         return 0
#     if ans not in memo:
#         count = 0
#         for n in nums:
#             count += dfs(nums, n, ans, target, memo)
#         memo[ans] = count
#     return memo[ans]