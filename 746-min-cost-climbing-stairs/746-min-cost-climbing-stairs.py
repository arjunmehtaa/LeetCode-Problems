    # Most Optimal Solution (Bottom-up approach)

# Time Complexity   : O(N)
# Space Complexity  : O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None] * n
        for i in range(0, len(cost)):
            if i <= 1:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

# Optimal Solution (Same as Brute Force + Memoization) (Top-down approach)
#
# Time Complexity   : O(N)
# Space Complexity  : O(N)
#
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dp = [None] * n
#         return min(minCost(n-1, cost, dp), minCost(n-2, cost, dp))
#   
# def minCost(i, cost, dp):
#     if i < 0:
#         return 0
#     if i == 0 or i == 1:
#         return cost[i]
#     if dp[i] != None:
#         return dp[i]
#     dp[i] = cost[i] + min(minCost(i-1, cost, dp), minCost(i-2, cost, dp))
#     return dp[i]

# Brute Force Solution
#
# Time Complexity   : O(2^N)
# Space Complexity  : O(N)
#
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         return min(minCost(n-1, cost), minCost(n-2, cost))
#    
# def minCost(i, cost):
#     if i < 0:
#         return 0
#     if i == 0 or i == 1:
#         return cost[i]
#     return cost[i] + min(minCost(i-1, cost), minCost(i-2, cost))
        