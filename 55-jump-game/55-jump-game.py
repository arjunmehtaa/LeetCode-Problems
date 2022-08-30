# Greedy Solution
# Time Complexity	: O(N)
# Space Complexity	: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
# DFS + Memoization Solution
# Time Complexity	: O(N^2)
# Space Complexity	: O(N)
#
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         mem = {}
#         return dfs(nums, 0, mem)
#
# def dfs(nums, index, mem):
#     if index == len(nums) - 1:
#         mem[index] = True 
#     if index >= len(nums):
#         mem[index] = False
#     if not index in mem:
#         mem[index] = False
#         limit = index + nums[index]
#         i = index
#         while i < limit:
#             i += 1
#             if dfs(nums, i, mem):
#                 mem[i] = True
#                 mem[index] = True
#     return mem[index] 
        